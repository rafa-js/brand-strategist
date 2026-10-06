#!/usr/bin/env python3
"""Stoke ember mark (direction M): builds the SVG masters, the lockups with an outlined wordmark,
the state set and the PNG export job list, from the parameters in ../README.md.

Usage:
    pip install fonttools brotli uharfbuzz
    STOKE_FONT=/path/to/Rubik[wght].ttf python3 build_logo.py     # Rubik variable font, Google Fonts (OFL)
    node export_png.js "$TMPDIR/stoke-logo-jobs.json"              # PNGs, needs Playwright
"""
import io, json, math, os, tempfile
from pathlib import Path
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

SCR = Path(__file__).resolve().parent
OUT = SCR.parent                                                 # brands/stoke/logo
FONT = Path(os.environ.get("STOKE_FONT", SCR / "Rubik[wght].ttf"))  # Rubik (variable), outlined at wght 900
(OUT / "states").mkdir(parents=True, exist_ok=True)

# ---------------- tokens ----------------
CRIMSON, BLOOM, CORE, HEAT = "#E0245E", "#FF4D7D", "#FFC98A", "#FFF1DC"
CRUST_TOP, CRUST_BASE = "#3B1B26", "#1E0F14"
EMBER_BLACK, BONE, COAL_TEXT = "#1C1517", "#F4F1EC", "#1C1C21"

# ---------------- geometry (100-unit grid) ----------------
VERTS = [(12, 44), (30, 17), (66, 12), (90, 34), (89, 70), (60, 89), (19, 79)]
RADII = [9, 10, 10, 9, 11, 10, 9]
MAIN_C = [(3, 31), (22, 38), (36, 34), (47, 46), (70, 50), (99, 47)]
MAIN_W = [2.4, 3.8, 4.4, 5.0, 4.0, 2.4]
FORK_C = [(70, 50), (80, 62), (93, 93)]
FORK_W = [3.6, 2.8, 1.8]
SMALL_SCALE = (1.8, 1.9)    # 16-32 px: the same cracks, thickened (main, fork), so the mark stays asymmetric

def rounded_poly(pts, radii, k=0.62):
    n, d = len(pts), []
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        v1 = (p0[0] - p1[0], p0[1] - p1[1]); l1 = math.hypot(*v1)
        v2 = (p2[0] - p1[0], p2[1] - p1[1]); l2 = math.hypot(*v2)
        r1, r2 = min(radii[i], l1 / 2.05), min(radii[i], l2 / 2.05)
        a = (p1[0] + v1[0] / l1 * r1, p1[1] + v1[1] / l1 * r1)
        b = (p1[0] + v2[0] / l2 * r2, p1[1] + v2[1] / l2 * r2)
        c1 = (a[0] + (p1[0] - a[0]) * k, a[1] + (p1[1] - a[1]) * k)
        c2 = (b[0] + (p1[0] - b[0]) * k, b[1] + (p1[1] - b[1]) * k)
        d.append(("M" if i == 0 else "L") + f"{a[0]:.2f} {a[1]:.2f}")
        d.append(f"C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {b[0]:.2f} {b[1]:.2f}")
    return "".join(d) + "Z"

def ribbon(center, widths, miter_limit=2.4):
    """Tapered crack around a centerline, with true miter joins (crisp corners, no notches)."""
    def unit(dx, dy):
        L = math.hypot(dx, dy); return dx / L, dy / L
    left, right, n = [], [], len(center)
    for i, (x, y) in enumerate(center):
        w = widths[i] / 2
        if i == 0 or i == n - 1:
            a, b = (center[0], center[1]) if i == 0 else (center[i - 1], center[i])
            dx, dy = unit(b[0] - a[0], b[1] - a[1]); mx, my, m = -dy, dx, w
        else:
            d1 = unit(x - center[i - 1][0], y - center[i - 1][1])
            d2 = unit(center[i + 1][0] - x, center[i + 1][1] - y)
            n1, n2 = (-d1[1], d1[0]), (-d2[1], d2[0])
            mx, my = unit(n1[0] + n2[0], n1[1] + n2[1])
            m = min(w / max(mx * n1[0] + my * n1[1], 1e-6), w * miter_limit)
        left.append((x + mx * m, y + my * m)); right.append((x - mx * m, y - my * m))
    return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in left + right[::-1]) + "Z"

def polyline(c):
    return "M" + " L".join(f"{x} {y}" for x, y in c)

COAL = rounded_poly(VERTS, RADII)
CRACKS = [ribbon(MAIN_C, MAIN_W), ribbon(FORK_C, FORK_W)]
LINES = [polyline(MAIN_C), polyline(FORK_C)]
SMALL_CRACKS = [ribbon(MAIN_C, [w * SMALL_SCALE[0] for w in MAIN_W]), ribbon(FORK_C, [w * SMALL_SCALE[1] for w in FORK_W])]
BBOX = (12, 12, 90, 89)          # coal extents on the grid (x0, y0, x1, y1)
CENTER = ((BBOX[0] + BBOX[2]) / 2, (BBOX[1] + BBOX[3]) / 2)

STATES = {
    #         crust top, crust base, edge, edge op, crack, bloom, bloom op, core op
    "hot":    (CRUST_TOP, CRUST_BASE, CRIMSON, .95, HEAT, BLOOM, .9, .95),
    "warm":   ("#35191F", CRUST_BASE, CRIMSON, .7, "#FF8FA9", CRIMSON, .55, .45),
    "banked": ("#2C161C", "#1B0E12", "#9E1645", .55, "#C2486B", "#9E1645", .35, .2),
    "cold":   ("#3A3A40", "#25252A", "#6B6B73", .5, "#8B8B94", "#8B8B94", 0, 0),
    "fading": ("#3A2C31", "#241B1F", "#8E5A6A", .45, "#B98A97", "#8E5A6A", .25, .08),
}

def blur(fid, sd):
    return (f'<filter id="{fid}" filterUnits="userSpaceOnUse" x="-30" y="-30" width="160" height="160">'
            f'<feGaussianBlur stdDeviation="{sd}"/></filter>')

def live(state="hot", p="e"):
    """Returns (defs, body) for the live ember in 100-unit space; p prefixes ids."""
    top, base, edge, edge_op, crack, bloom, bloom_op, core_op = STATES[state]
    defs = (f'<clipPath id="{p}c"><path d="{COAL}"/></clipPath>'
            f'<linearGradient id="{p}g" x1="0" y1="0" x2=".25" y2="1"><stop offset="0" stop-color="{top}"/>'
            f'<stop offset="1" stop-color="{base}"/></linearGradient>'
            + blur(f"{p}w", 5.5) + blur(f"{p}n", 2) + blur(f"{p}x", 2.6))
    glow = "".join(f'<path d="{l}" fill="none" stroke="{bloom}" stroke-width="20" stroke-linejoin="round" stroke-linecap="round" '
                   f'opacity="{bloom_op}" filter="url(#{p}w)"/>'
                   f'<path d="{l}" fill="none" stroke="{CORE}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round" '
                   f'opacity="{core_op}" filter="url(#{p}n)"/>' for l in LINES) if bloom_op else ""
    body = (f'<path d="{COAL}" fill="url(#{p}g)"/><g clip-path="url(#{p}c)">'
            f'<path d="{COAL}" fill="none" stroke="{edge}" stroke-width="9" opacity="{edge_op}" filter="url(#{p}x)"/>'
            f'{glow}' + "".join(f'<path d="{c}" fill="{crack}"/>' for c in CRACKS) + '</g>')
    return defs, body

def knockout(ink, p="k", small=False):
    holes = "".join(f'<path d="{c}" fill="#000"/>' for c in (SMALL_CRACKS if small else CRACKS))
    defs = (f'<mask id="{p}m" maskUnits="userSpaceOnUse" x="-10" y="-10" width="120" height="120">'
            f'<rect x="-10" y="-10" width="120" height="120" fill="#fff"/>{holes}</mask>')
    return defs, f'<path d="{COAL}" fill="{ink}" mask="url(#{p}m)"/>'

def svg_doc(defs, body, w, h, vb="0 0 100 100", title="Stoke ember"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{vb}" role="img" aria-label="{title}">'
            f'<title>{title}</title><defs>{defs}</defs>{body}</svg>\n')

def app_icon(size=1024, p="a"):
    """Square master (iOS and Android apply their own masks). Coal at 62% of the tile, optically centered."""
    d, b = live("hot", p)
    s = 0.62 * 100 / (BBOX[3] - BBOX[1])      # coal height = 62% of the tile
    tx, ty = 50 - CENTER[0] * s, 50 - CENTER[1] * s + 0.6
    defs = (d + f'<radialGradient id="{p}amb" cx="50" cy="50.6" r="44" gradientUnits="userSpaceOnUse">'
            f'<stop offset="0" stop-color="{CRIMSON}" stop-opacity=".30"/><stop offset=".55" stop-color="{CRIMSON}" stop-opacity=".09"/>'
            f'<stop offset="1" stop-color="{CRIMSON}" stop-opacity="0"/></radialGradient>')
    body = (f'<rect width="100" height="100" fill="{EMBER_BLACK}"/><rect width="100" height="100" fill="url(#{p}amb)"/>'
            f'<g transform="translate({tx:.3f} {ty:.3f}) scale({s:.4f})">{b}</g>')
    return svg_doc(defs, body, size, size, title="Stoke app icon")

# ---------------- wordmark (outlined Rubik 900, HarfBuzz kerning, -0.035 em tracking) ----------------
def wordmark_paths(text="stoke", tracking=-35):
    tt = TTFont(str(FONT))
    gs = tt.getGlyphSet(location={"wght": 900})
    order = tt.getGlyphOrder()
    raw = TTFont(str(FONT)); raw.flavor = None              # HarfBuzz cannot read WOFF2: shape a decompressed TTF
    data = io.BytesIO(); raw.save(data)
    face = hb.Face(hb.Blob(data.getvalue())); font = hb.Font(face)
    font.set_variations({"wght": 900})
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {"kern": True, "liga": True})
    x, paths = 0, []
    for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
        name = order[info.codepoint]
        pen = SVGPathPen(gs)
        gs[name].draw(TransformPen(pen, (1, 0, 0, -1, x + pos.x_offset, -pos.y_offset)))
        paths.append(pen.getCommands())
        x += pos.x_advance + (tracking if i < len(buf.glyph_infos) - 1 else 0)
    return " ".join(paths), x       # path in font units, baseline at y=0, y up flipped; total advance

def lockup(on="dark", p="l"):
    text_path, adv = wordmark_paths()
    ink = BONE if on == "dark" else COAL_TEXT
    asc = 710                                   # ascender of t and k in Rubik, font units
    coal_h = 1.15 * asc                         # coal height relative to the ascenders
    s = coal_h / (BBOX[3] - BBOX[1])
    gap = 0.30 * coal_h
    pad = 0.25 * coal_h
    mx = pad - BBOX[0] * s                      # mark: left edge at pad
    my = (pad + coal_h) - BBOX[3] * s           # mark: bottom of coal at pad + coal_h
    baseline = pad + coal_h / 2 + asc / 2       # center the ascender band on the coal's center
    tx = pad + (BBOX[2] - BBOX[0]) * s + gap
    w = tx + adv + pad
    h = pad * 2 + coal_h
    d, b = live("hot", p)
    body = (f'<g transform="translate({mx:.2f} {my:.2f}) scale({s:.4f})">{b}</g>'
            f'<path transform="translate({tx:.2f} {baseline:.2f})" d="{text_path}" fill="{ink}"/>')
    return svg_doc(d, body, round(w / 4), round(h / 4), vb=f"0 0 {w:.1f} {h:.1f}", title="Stoke"), (w, h)

def construction():
    """Construction drawing on the 100-unit grid: vertices, radii, crack centerlines, clear space."""
    grid = "".join(f'<line x1="{i}" y1="-20" x2="{i}" y2="120" stroke="#d9d4cf" stroke-width=".25"/>'
                   f'<line x1="-20" y1="{i}" x2="120" y2="{i}" stroke="#d9d4cf" stroke-width=".25"/>' for i in range(0, 101, 10))
    cs = 0.25 * (BBOX[3] - BBOX[1])
    clear = (f'<rect x="{BBOX[0] - cs:.1f}" y="{BBOX[1] - cs:.1f}" width="{BBOX[2] - BBOX[0] + 2 * cs:.1f}" '
             f'height="{BBOX[3] - BBOX[1] + 2 * cs:.1f}" fill="none" stroke="#2F7DD1" stroke-width=".5" stroke-dasharray="2 1.4"/>'
             f'<rect x="{BBOX[0]}" y="{BBOX[1]}" width="{BBOX[2] - BBOX[0]}" height="{BBOX[3] - BBOX[1]}" fill="none" '
             f'stroke="#2F7DD1" stroke-width=".35"/>')
    poly = "M" + " L".join(f"{x} {y}" for x, y in VERTS) + "Z"
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="1.1" fill="#C0392B"/><text x="{x + (2 if x > 50 else -2)}" y="{y - 2}" '
                   f'font-size="3.4" font-family="monospace" fill="#5a5860" text-anchor="{"start" if x > 50 else "end"}">P{i + 1} ({x},{y}) r{RADII[i]}</text>'
                   for i, (x, y) in enumerate(VERTS))
    lines = "".join(f'<path d="{l}" fill="none" stroke="#C0392B" stroke-width=".45" stroke-dasharray="1.6 1"/>' for l in LINES)
    body = (f'<rect x="-22" y="-22" width="144" height="144" fill="#fff"/>{grid}{clear}'
            f'<path d="{COAL}" fill="{CRIMSON}" opacity=".16"/><path d="{poly}" fill="none" stroke="#9a96a0" stroke-width=".3"/>'
            f'<path d="{COAL}" fill="none" stroke="{CRIMSON}" stroke-width=".7"/>{lines}{dots}'
            f'<text x="{BBOX[0] - cs + 1}" y="{BBOX[3] + cs + 4.6}" font-size="3.4" font-family="monospace" fill="#2F7DD1">'
            f'clear space = 1/4 coal height</text>')
    return svg_doc("", body, 720, 720, vb="-22 -22 144 144", title="Stoke ember construction")

# ---------------- write masters ----------------
def write(name, text):
    (OUT / name).write_text(text)

def main():
    d, b = live("hot", "e"); write("stoke-ember.svg", svg_doc(d, b, 512, 512))
    d, b = knockout(CRIMSON, "f"); write("stoke-ember-flat.svg", svg_doc(d, b, 512, 512, title="Stoke ember, flat"))
    d, b = knockout(EMBER_BLACK, "k"); write("stoke-ember-black.svg", svg_doc(d, b, 512, 512, title="Stoke ember, one color"))
    d, b = knockout(BONE, "w"); write("stoke-ember-white.svg", svg_doc(d, b, 512, 512, title="Stoke ember, one color reversed"))
    d, b = knockout(CRIMSON, "s", small=True); write("stoke-ember-small.svg", svg_doc(d, b, 32, 32, title="Stoke ember, small sizes"))
    write("stoke-app-icon.svg", app_icon())
    for st in STATES:
        d, b = live(st, st[0]); write(f"states/stoke-ember-{st}.svg", svg_doc(d, b, 256, 256, title=f"Stoke ember, {st}"))
    dark, wh = lockup("dark", "ld"); write("stoke-lockup-on-dark.svg", dark)
    light, _ = lockup("light", "ll"); write("stoke-lockup-on-light.svg", light)
    write("stoke-ember-construction.svg", construction())
    jobs = [
        ("stoke-app-icon.svg", "stoke-app-icon-1024.png", 1024, 1024, False),
        ("stoke-ember.svg", "stoke-ember-1024.png", 1024, 1024, True),
        ("stoke-ember-flat.svg", "stoke-ember-flat-512.png", 512, 512, True),
        ("stoke-ember-small.svg", "favicon-32.png", 32, 32, True),
        ("stoke-ember-small.svg", "favicon-16.png", 16, 16, True),
        ("stoke-lockup-on-dark.svg", "stoke-lockup-on-dark.png", round(wh[0] / 2), round(wh[1] / 2), True),
        ("stoke-lockup-on-light.svg", "stoke-lockup-on-light.png", round(wh[0] / 2), round(wh[1] / 2), True),
    ]
    jobs_path = Path(tempfile.gettempdir()) / "stoke-logo-jobs.json"
    jobs_path.write_text(json.dumps([{"svg": str(OUT / a), "png": str(OUT / b), "w": w, "h": h, "transparent": t}
                                               for a, b, w, h, t in jobs]))
    print("wrote masters to", OUT, "| PNG jobs:", jobs_path)

if __name__ == "__main__":
    main()
