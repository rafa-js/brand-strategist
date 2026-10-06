// Renders each SVG master to PNG at exact pixel size (Playwright). Usage: node export_png.js <jobs.json from build_logo.py>
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: 1 });
    const svg = fs.readFileSync(j.svg, 'utf8').replace(/width="[^"]*" height="[^"]*"/, `width="${j.w}" height="${j.h}"`);
    await page.setContent(`<!doctype html><html><body style="margin:0;background:transparent">${svg}</body></html>`);
    await page.screenshot({ path: j.png, omitBackground: j.transparent, clip: { x: 0, y: 0, width: j.w, height: j.h } });
    await page.close();
    console.log('png', j.png.split('/').pop(), `${j.w}x${j.h}`);
  }
  await browser.close();
})();
