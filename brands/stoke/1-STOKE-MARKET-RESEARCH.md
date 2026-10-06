# Fueling for Real Life: Market Research Report
### The strategic case for bringing proven adaptive fueling to athletes who train around full lives, with fewer pains, a fairer price and different distribution
### 5 October 2026 (positioning inputs updated 6 October 2026)

## DISCOVERY (Inputs)

| Question | Answer |
|----------|--------|
| **What is the product or service?** (category, function, target user) | A mobile food-tracking app for people who train. Three proposed value props: effortless food tracking (AI photo logging), science-based food scores, and food swaps based on the user's goal. Target users: amateur athletes with ambitious goals: building muscle, training for a marathon, training for HYROX. |
| **Who is the competition?** (who occupies nearby rungs on the mental ladder) | Initial answer from the brief: AI calorie-tracking apps. Part 2 widens it to five fronts: calorie counters (MyFitnessPal, which now owns Cal AI), lifter macro coaches (MacroFactor), sports nutrition plans (Fuelin, Hexis), general-health food scores and swap scanners (Yuka, ZOE, Nutri-Score, Apple; Swapd, NutriSwap), and wearables adding food logging (Garmin, Google, Oura). Founder priority: a clear, consistent difference from Fuelin, the closest competitor. |
| **What position, if any, does the brand currently hold?** | None. New brand, pre-launch: no name, no audience, no claims in market. |
| **What is the business goal?** (launch, reposition, defend, extend, fix) | Launch. Differentiate from AI calorie trackers by serving people who train and applying modern sports-nutrition science to their goals. Founder clarifications (5 October 2026): the app exists to help amateurs eat better to reach ambitious goals through science-based recommendations, and the food score is there to gamify and teach, not as a goal in itself. Then: "the base of fueling is right." Stoke uses the same fundamentals as the fueling apps (calorie and macronutrient goals that adapt to planned activity), copies what already works, and differentiates on user complaints, pricing and distribution. Founder clarification (6 October 2026): the target users stay ambitious amateurs, but the positioning never calls them that: "Nobody wants to be told they are an amateur. They want to aspire to become a pro." |

Working assumptions not stated in the brief, to confirm: an English-language launch with the US and UK as lead markets, and a product still in development rather than live.

## EXECUTIVE SUMMARY

Adaptive fueling works, and its users say so. The science is settled: athletes should eat "in relation to sport rather than general daily targets" (Thomas, Erdman and Burke, 2016), and non-elite marathoners who followed a science-based race carbohydrate strategy ran 4.7% faster (Hansen et al., 2014). Fuelin, the closest competitor, turns that science into daily targets that adapt to training, and its five-star reviews praise it for taking "the guesswork out." But the fueling apps were built for the committed few. Fuelin offers no free trial ("Fuelin works best when you're all in"), charges $139 a year, features Ironman world champions and sells coaching for up to $1,500 a month. In 142 hand-coded low-rated reviews, 61% raise price, the missing trial or billing, and the top product complaints are logging (28%) and integrations (24%). The category has reached few people: Fuelin reported about 3,000 monthly age-group athletes (2025), while HYROX reports more than 1.5 million participants and London drew 1.34 million ballot applications. Distribution, not accuracy, decided the last round of food apps: Cal AI drew about twenty times the monthly downloads of the better-validated SnapCalorie (Sensor Tower estimates). Yet **no product combines proven adaptive fueling with a free start, a price near the trackers', sync with the plans athletes already follow and distribution through the communities where they train.** The science is copyable; the access is the gap.

## PART 1: WHY TODAY'S TOOLS FAIL PEOPLE WHO TRAIN

### 1.1 The Numbers Are Wrong: the calorie is the least reliable thing a photo reads

- **Photo logging undercounts by about a third.** In an NIH/NIDDK test of 102 meals with every ingredient weighed, photo features underestimated energy by 252 kcal (Appediet), 327 (MyFitnessPal), 333 (Lose It!) and 345 kcal per meal (Cal AI), about 33%, and fat by about 30 g per meal (ASN Nutrition 2026 abstract, preliminary; reported by Healio and EurekAlert).
- **Naming the food is largely solved; measuring it is not.** MyFitnessPal identified 97% of food components and Foodvisor 87%, yet energy errors on mixed dishes ran from -76% (pearl milk tea) to +270% (bibimbap) (Li et al., *Nutrients*, 2024). Carbohydrate error fell from 56.6% to 20.2% when the model was told the true weight: portion is the bottleneck (Mu et al., ACM BCB 2025).
- **General AI models miss protein worst.** GPT-4o and Claude 3.5 Sonnet estimated energy with 35.8% mean absolute percentage error and protein with about 61%; the authors call them "not yet suitable for precise dietary assessment in clinical or athletic populations" (Fridolfsson et al., *Current Developments in Nutrition*, 2025).
- **The label itself is approximate by law.** US rules treat a food as misbranded only if its calories run more than 20% above the label, and accept "reasonable deficiencies" below it (21 CFR 101.9(g)(5)-(6)). Reduced-energy restaurant meals measured 18% above stated values on average, with wide variability (Urban et al., 2010); standard Atwater factors overestimate the energy in almonds by 32% (Novotny et al., 2012).
- **Both sides of the budget are noisy.** Athletes under-report intake by 19% against doubly labeled water (Capling et al., 2017, 11 studies), and no wrist device estimated energy expenditure within 20% (Shcherbina et al., 2017). A fixed daily budget subtracts one noisy number from another, which is why useful targets are ranges that learn from weight trend over weeks, not precise daily quotas.
- **Fair counterpoint.** Careful manual entry works: MyFitnessPal energy values correlated with a national reference database at r = 0.96 after cleaning (Evenepoel et al., 2020) and came within 3.7% of weighed intake in a supervised trial (Diktas et al., 2025). The NIH team called the photo error "similar to previously reported underestimation using self-report." The verdict is not that counting is useless; it is that the calorie total is fragile exactly where apps use it as a precise budget, and weaker still in athletes: in endurance athletes MyFitnessPal "showed poor validity for total energy, carbohydrates, protein" (Morello et al., 2025).

### 1.2 The Concept Is Wrong: a fixed weight-loss budget answers a dieter's question

- **Sports nutrition is periodized to sessions, not budgeted by day.** The joint position of the American College of Sports Medicine, the Academy of Nutrition and Dietetics and Dietitians of Canada: "Nutrition goals and requirements are not static," and support "needs to be periodized, taking into account the needs of daily training sessions" (Thomas, Erdman and Burke, 2016).
- **The same athlete needs very different fuel on different days.** Daily carbohydrate targets run from 3-5 g/kg for light, skill-based days to 8-12 g/kg for very high loads; during exercise, 30-60 g/h for sessions of 1 to 2.5 hours and up to 90 g/h beyond 2.5-3 hours (Thomas et al., 2016). For a 70 kg athlete that is roughly 210-350 g of carbohydrate on a light day and 560-840 g on a very heavy one.
- **The same food earns opposite verdicts by context.** The same position stand recommends "nutrient-rich carbohydrate sources" for daily fueling, sources "low in fibre/residue" for carbohydrate loading, and avoiding "choices high in fat/protein/fibre" before events to reduce gastrointestinal risk (Thomas et al., 2016). The Australian Institute of Sport lists white bread, jam, rice cakes, honey and flat cola among food-first alternatives to gels (Forbes, Burke et al., *Sports Medicine Open*, 2026).
- **Health scores were not built for this, by their makers' own account.** Nutri-Score "cannot be used" for sport nutrition products because it "was developed in regard to the needs of the general population, whereas sport nutrition must meet particular needs" (Santé publique France, Nutri-Score Q&A, 17 March 2025). Nutri-Score rates a food per 100 g and NOVA classifies it by degree of processing; neither has an input for the eater, the training day or the timing (Sarda et al., 2024).
- **Calories still matter to athletes: as targets that move with training, and as a floor.** The sport's own under-fueling measure, energy availability, is calculated in kcal per kg of fat-free mass, and chronic values below about 30 are associated with impairment (Thomas et al., 2016). The defensible claim is not that energy is irrelevant; it is that a fixed weight-loss budget is the wrong use of it for people who train.
- **Authority quote**: "Sports nutrition guidelines should also consider the importance of the timing of nutrient intake and nutritional support over the day and in relation to sport rather than general daily targets." (Thomas, Erdman and Burke, ACSM/AND/DC joint position, 2016)

**Exhibit: how general-health scores grade common fueling foods** (Open Food Facts product pages, read 5 October 2026)

| Food | Role in training | Nutri-Score shown | NOVA group |
|------|------------------|-------------------|------------|
| Maurten Gel 100 | In-race carbohydrate | Not applicable (dietary supplement) | 4 (ultra-processed) |
| Maurten Gel 100 Caf 100 | In-race carbohydrate | D | Not shown |
| SiS GO Isotonic gel (French listing) | In-race carbohydrate | B | 4 |
| Gatorade Orange, 20 oz (US) | In-session carbohydrate and sodium | C | 4 |
| Thomas' Plain Bagels (US) | Pre-race breakfast | C | 4 |
| Quaker Lightly Salted Rice Cakes (US) | Pre-session snack | C | 3 |
| Honey (Maribel) | Pre- or in-session carbohydrate | E | 2 |
| Basmati rice (control) | Daily staple | B | 1 |

Reading it fairly: grades depend on crowd-entered categories (one SiS GO barcode scores B, another shows "not applicable"), and plain staples like basmati rice score well, so health scores do not punish all carbohydrate. The mismatch concentrates in fast, sugar-dense, processed fuel: exactly what the guidelines prescribe for hard and long sessions.

**What calorie budgets and health scores are blind to**

| Dimension | What calorie budgets and health scores miss |
|-----------|---------------------------------------------|
| **Training load** | The same daily target on a rest day and a 30 km day, although carbohydrate needs span 3-5 to 8-12 g/kg/day by load (Thomas et al., 2016) |
| **Timing** | A low-fibre, fast carbohydrate is right before a long session and wrong at a desk. ZOE scored red velvet cake 18/100 because it is "digested quickly, and with very little fibre": the property an athlete wants mid-session |
| **Protein dose** | Daily adequacy for muscle (gains plateau around 1.6 g/kg/day; Morton et al., 2018) and a dose of about 0.25-0.4 g/kg per meal (Jäger et al., 2017; Schoenfeld and Aragon, 2018) are invisible inside a calorie total |
| **In-session fuel** | Gels and sports drinks are ultra-processed by design (NOVA 4), and 95% of surveyed athletes use sports foods (Forsyth and Mantzioris, 2023) |
| **Energy availability** | In a calorie app a deficit is the goal; for an athlete in heavy training it is a health and performance risk (REDs; Mountjoy et al., 2023) |
| **The goal itself** | "Sub-4 marathon", "HYROX PR" and "build muscle" are not weight goals; MacroFactor's App Store goals are weight loss, maintenance and weight gain |

### 1.3 The Behavior Doesn't Work: amateurs under-fuel, and weight-driven tracking carries risk

- **Amateurs under-fuel the sessions that matter.** Only 2 of 38 marathoners (5.3%) in a 2025 field study at a marathon in Turkey met the study's 60-90 g/h race target, and most athletes were "often overestimating their intake" (*European Journal of Sport Science*, 2025, 60 endurance athletes). Seville marathoners averaged 35 g/h (Jiménez-Alfageme et al., 2025, n=160). Only 45.7% of non-elite multisport athletes met daily carbohydrate recommendations, while 87.1% reached at least 1.2 g/kg of protein (Masson and Lamarche, 2016): the protein message has landed, the carbohydrate message has not.
- **Following the science pays.** Non-elite marathoners following a science-based in-race strategy (gels targeting about 60 g/h) finished 10 min 55 s (4.7%) faster than matched runners eating freely (Hansen et al., 2014, n=28). In an analysis of 1.9 million marathon results, 28% of men and 17% of women "hit the wall" (Smyth, 2021).
- **Under-fueling risk is common in recreational samples.** 45% of female recreational gym exercisers (Slater et al., 2016, n=109), 43% of trail runners (Henninger et al., 2024, n=1,899) and 47.2% of non-elite male endurance athletes (Lane et al., 2019, n=108) screened at risk of low energy availability. These are screening estimates, and self-report can inflate them (McHaffie et al., 2025).
- **Knowledge is thin.** 53% of Americans don't know how many grams of protein they need and 26% are unsure (IFIC protein spotlight, 2025). Only 1.8% of amateur endurance athletes identified the carbohydrate dose for rapid glycogen refueling (Csanaky et al., 2025).
- **Weight-driven tracking carries risk.** 73% of people with an eating disorder who used MyFitnessPal perceived it as contributing to their disorder (Levinson et al., 2017, n=105). In a four-year cohort, using self-monitoring apps for weight management predicted more disordered weight-control behavior (Hahn et al., 2024). Fair counterpoint: a 12-month RCT found no rise in eating-disorder symptoms with MyFitnessPal (Jospe et al., 2018, n=250), and most harm evidence is cross-sectional (Anderberg et al., 2025).
- **Authority quote**: "the motivation for self-monitoring (e.g., for managing eating or weight) may be more important than what they are monitoring." (Hahn et al., *Journal of Eating Disorders*, 2024)

### 1.4 Adherence Is the Bottleneck: what helps people follow the science

- **Knowledge alone rarely changes intake.** In a randomized trial with 79 young endurance athletes, nutrition education raised knowledge scores (from 78 to 85-86), but "the nutrition education intervention alone was not enough to change dietary intake," carbohydrate stayed "below endurance athletes' recommendations," and the mobile app "did not improve learning further" (Heikkilä et al., 2019). A review of 28 studies found only "weak-to-moderate" links between athletes' nutrition knowledge and their diets (Janiczak et al., 2022).
- **Adherence predicts results.** In a one-year randomized weight-loss trial of four popular diets in overweight adults, weight loss was associated with self-reported adherence (r = 0.60) but not with diet type (r = 0.07), and "overall dietary adherence rates were low" (Dansinger et al., 2005). It is not a sports trial, but the lesson transfers: the best targets are the ones a person can keep hitting.
- **Logging is where adherence breaks.** New MyFitnessPal users omitted 18% of foods and only 20% said they would keep using it (Chen et al., 2019). In hand-coded low-rated App Store reviews, logging problems are among the top complaints for Fuelin (28%), Hexis (54%) and MacroFactor (40%) (Part 2).
- **Concrete swaps change choices, at least for shoppers.** In a randomized online-shopping trial (n=550), offering swaps improved the nutritional quality of baskets about three times as much as Nutri-Score labels (B = -9.58 vs. -3.28; Jansen et al., 2021). In another (n=428), swaps on top of Nutri-Score improved baskets further (d = -0.48), most of all for people who knew least about nutrition (Schruff-Lim et al., 2024). A review of 35 trials found education-only interventions ineffective in real stores, while swap interventions "appeared promising" in the two real-store studies (Hartmann-Boyce et al., 2018). Limits: every swap trial so far involves grocery shoppers aiming for less sugar, fat or energy; effects are modest and often short-term (participants accepted a median of one of about four offered swaps in Forwood et al., 2015); and we found no swap trial in athletes (PubMed search, 5 October 2026).
- **Habits form from small actions repeated in the same context.** In a 12-week study of new daily eating, drinking or activity behaviors, automaticity took a median of 66 days to plateau (range 18-254), and missing a single opportunity did not materially affect the process (Lally et al., 2010). Habit-based advice ties one small action to a consistent cue (Gardner, Lally and Wardle, 2012).
- **Game mechanics are not a proven lever on eating.** Across 16 randomized trials, gamified interventions increased physical activity with a small-to-medium effect (Hedges g = 0.42; g = 0.23 against non-gamified versions; Mazeas et al., 2022). Across 36 trials of health apps, gamification produced trivial-to-small gains in steps and adiposity and no differences in the other outcomes measured, including dietary factors (Nishi et al., 2024). In children and adolescents, game-based programs raised nutrition knowledge and fruit and vegetable intake (Suleiman-Martos et al., 2021). A score can make progress visible and teach; it cannot be the engine.
- **Authority quote**: "the nutrition education intervention alone was not enough to change dietary intake" (Heikkilä et al., *Nutrients*, 2019)

## PART 2: THE COMPETITIVE LANDSCAPE

### The Category Map

| Player | Question It Answers | Users/Scale | Rating | Price | Key Limitation |
|--------|--------------------:|-------------|--------|-------|----------------|
| **MyFitnessPal** | "How many calories did I eat?" | 280M+ members (company); #1 top-grossing US health and fitness app | 4.7 (2.37M) | Premium $79.99/yr | App Store name is "Calorie Counter"; budget and goals are weight-based |
| **Cal AI** (owned by MyFitnessPal) | "How many calories are in this photo?" | 15M+ downloads; over $30M annual revenue | 4.8 (368K) | From $29.99/yr | Worst undercount in the NIH test (345 kcal/meal); own FAQ says "about 80% accurate" |
| **MacroFactor** | "What should my macros be to move my body weight?" | 600K+ users (company) | 4.8 (23K) | $71.99/yr | Weight and body-composition goals only; no session fueling; 7-day trial, no free tier |
| **Cronometer** | "What nutrients am I actually getting?" | 13M+ users (company) | 4.8 (99K) | Gold $59.99/yr | A precise ledger with no training context |
| **Hexis** | "How many carbs does my training need today?" | Elite: claims about 40% of Tour de France riders; consumer: 29 US ratings | 2.7 (29, US) | €129.99/yr | Endurance-first; no free trial; logging "is the grind" (Roadman Cycling, 2026) |
| **Fuelin** | "What should I eat today, and when?" | 65K+ downloads; about 3,000 monthly age-group athletes (company, 2025) | 4.5 (1.3K) | $139/yr; coach tier $399/yr | No free trial by policy; premium price; logging and integration complaints (see below) |
| **Mavr** | "How should I fuel my endurance or HYROX training?" | 8 US ratings | 4.1 (8) | $79.99/yr; offers from $39.99 | Requires a subscription to use; endurance-first |
| **FoodCoach** | "What should I eat today, per my plan?" | Small | 2.6 (14) | $60/yr | Meal plans; no photo logging |
| **Yuka** | "Is this product healthy?" | About 89.5M users (company counter) | 4.8 (100K) | Freemium | 30% of the score is additives; packaged goods; no context |
| **ZOE** | "Is this food good for my long-term health?" | 200K+ gut tests; free US app | n/a | £119.88/yr (ZOE 2.0) | Health-for-everyone score; marks fast carbohydrate down |
| **Apple (iOS 27)** | "Is this plate processed, high-protein or sugary?" | Built into iPhone 15 Pro and later | n/a | Free | General-health glance; no training context |
| **MenuFit** | "What should I order to cut or bulk?" | About 200K downloads and $800K revenue last month (Sensor Tower estimate); #27 US top-grossing | 4.8 (54K) | Subscription | Restaurant orders for physique goals; no training context |
| **Healthy-swap scanners** (Swapd, NutriSwap, HealthySwap) | "Is there a healthier product than this one?" | Tiny: 0-5 US ratings each | n/a | Free or freemium | General-health swaps for packaged products; no goal or training input |
| **Garmin, Google, Oura** | "How does food relate to my body data?" | Large wearable bases | n/a | $69.99/yr (Garmin Connect+); $99/yr (Google Health) | Food is a feature; generic calorie and macro targets |

### Competitor Deep Dives

#### 1. MYFITNESSPAL (AND CAL AI)

**Overview**
- The category leader: "over 280 million members in over 120 countries" (company, 2026); #1 top-grossing US health and fitness app (Apple chart, 5 October 2026; Sensor Tower, Q3 2025); about $150M in annual EBITDA, with a sale reportedly explored at over $1B (Reuters, April 2026); 4.7 stars on 2.37M App Store ratings.
- Acquired Cal AI (closed December 2025, announced 2 March 2026). Cal AI, built by teenage founders, reached 15M+ downloads and over $30M in annual revenue (TechCrunch, 2026).
- Moving toward performance: Cal AI now runs "for performance-oriented members" (MyFitnessPal, March 2026); MyFitnessPal is title partner of HYROX Tampa, adding "Hyrox-specific recipes and fueling resources in the app" (Athletech News, August 2026); its AI Coach answers "what to eat... down to the food and portion," including pre-workout choices (Summer Release, August 2026). It also added GLP-1 medication tracking (April 2026).

**How It Works**
Users log by search, barcode, voice or photo against a 20M-food, largely crowdsourced database; the app sets a daily calorie and macro budget from a weight goal and tracks intake against it. Cal AI does the same from a photo in seconds, now on MyFitnessPal's database.

**Claims vs. Reality**
- **Company claim:** "the #1 nutrition tracking app"; Premium is like "having a dietitian and trainer at your fingertips." Cal AI claimed "90% accurate" in 2025 and now says "about 80% accurate" in its own FAQ, without defining whether that means naming the food or counting it.
- **Independent findings:** in the NIH photo test, MyFitnessPal undercounted 327 kcal and Cal AI 345 kcal per meal (preliminary, 2026). With careful manual entry, MyFitnessPal energy agrees well with reference data (r = 0.96; Evenepoel et al., 2020), but in endurance athletes it showed "poor validity for total energy, carbohydrates, protein" (Morello et al., 2025).

**User Complaints / Weaknesses**
- Cal AI App Store review (June 2025): "A small bowl of popcorn it listed at something like 8000 calories, it one time listed a candy bar at an eye popping 27 million calories."
- Real-world manual logging: new MyFitnessPal users omitted 18% of foods and undercounted 1,863 kJ (about 445 kcal) a day, and only 20% said they would keep using it (Chen et al., 2019).
- Structural: both products are named for the calorie ("MyFitnessPal: Calorie Counter"; "Cal AI"), and the newest features serve GLP-1 weight management.

**Assessment**
The leader owns "calories" and is line-extending toward performance with content, a sponsorship and a second brand. Its genuine strengths are scale, habit and a 20-million-food database. Its opening: it cannot call the calorie the wrong scoreboard without contradicting its own name.

#### 2. MACROFACTOR

**Overview**
- Built by the Stronger By Science team; grew from 35,000 users (September 2022) to "more than 600,000" (September 2026, company); 4.8 stars on about 23,000 App Store ratings; #10 top-grossing US health and fitness app (5 October 2026); $71.99/yr. Launched MacroFactor Workouts in January 2026.

**How It Works**
An adaptive algorithm estimates energy expenditure from logged intake and weight trend, then adjusts calorie and macro targets. AI photo logging (beta since March 2025) retrieves "real, lab-analyzed results" rather than relying on language models to invent entries.

**Claims vs. Reality**
- **Company claim:** "best-in-class expenditure estimate"; "smart algorithms personalize your calorie and macro intake targets."
- **Independent findings:** no independent validation found. Its listed goals are weight loss, maintenance and weight gain, and its 2026 annual report contains no content on sports performance or sports nutrition.

**User Complaints / Weaknesses**
- In 187 hand-coded low-rated reviews (four countries, 2021-2026), logging problems lead (40%), followed by price (24%) and the lack of a free tier (21%); it offers a 7-day trial but "does not offer a free subscription tier." Structural gap: targets follow body-weight trend, not the sessions ahead.

**Assessment**
The trusted brand among evidence-minded lifters and the most dangerous adjacent player: with Workouts it now holds training data, and training-aware targets would let it serve muscle-building athletes from a position of trust. Its position is the scale (body weight and composition), not the session.

#### 3. HEXIS

**Overview**
- Dublin-based performance nutrition platform; co-founders Dr David Dunne (CEO), Dr Xiaoxi Yan and Dr Sam Impey, author of the "Fuel for the Work Required" paper. Claims 200+ UCI World Tour riders, "nearly 40% of Tour de France riders" and "50% of Premier League clubs" (company, via Silicon Republic, 2026). Raised a $2.1M seed round (June 2026) to fund "a significant expansion into the direct-to-consumer market."

**How It Works**
"Carb Coding gives each meal a colour, based on the work you've just done and the work that's coming": green for high carbohydrate, amber for moderate, red for low, recalculated over a 72-hour training window from TrainingPeaks, Garmin, WHOOP and others. Photo, voice and barcode logging since November 2024. €24.99/month or €129.99/year.

**Claims vs. Reality**
- **Company claim:** "truly personalised, periodised nutrition to every athlete, at every level."
- **Independent findings:** 2.7 stars on 29 US App Store ratings. A review by a disclosed partner found logging "is the grind," an unreliable barcode scanner and judged it a fit for structured cyclists training six or more hours a week, not casual riders (Roadman Cycling, July 2026).

**User Complaints / Weaknesses**
- "food logging is just not very good... clunky and not user friendly"; "too many bugs... logging your food is a pain" (US App Store reviews). In 37 hand-coded low-rated reviews, logging problems and bugs each appear in 54%. No free trial (Roadman Cycling, 2026).

**Assessment**
Hexis owns the science of fueling and the elite proof, and Carb Coding is the closest existing analogue to context-aware meal advice: meal-level carbohydrate amounts set by training load. It is endurance-first, plan-first and hard to use, but it has fresh money pointed at amateurs.

#### 4. FUELIN

**Overview**
- "Fuelin - Performance Nutrition" on the US App Store, subtitled "Sports Nutrition Coaching," from Thrive AI Labs; co-founder and Chief Nutrition Officer Scott Tindal, a former performance nutrition advisory board member at IRONMAN; triathlete Daniela Ryf holds the title "Chief Fueling Officer." Claims 65,000+ downloads, "5,000,000+ workouts fueled" and 140+ countries; 4.5 stars on 1,267 US ratings (5 October 2026).
- Pricing: Autopilot costs $29/month or $139/year; Copilot, which adds "1:1 messaging with a Fuelin nutrition coach and bi-weekly live coaching sessions," $99/month or $399/year (App Store). On its website, 1:1 coaching costs $1,500/month and a consultation $500 for 60 minutes. Its FAQ: "We don't offer a free trial," because "Fuelin works best when you're all in."

**How It Works**
"Fuelin builds a daily nutrition plan just for you" that "automatically adjusts to your workouts" (App Store), syncing TrainingPeaks, Strava, Garmin and others; the homepage promises "exactly what, when, and how to eat to perform your best" with "precise macros and calorie targets." Carbohydrate guidance appears as a traffic light ("Red = Lower, Yellow = Moderate, Green = Higher"). Food is logged by AI photo recognition (since April 2025), voice, text or barcode, or imported from MyFitnessPal and Lose It!. Smart Meals (November 2025) suggests meals from your ingredients or a restaurant menu, aligned to "training load, macro targets, and performance goals." A Sweat Rate Tracker and Carb Capacity Testing serve endurance athletes, and "in-app lessons and videos" teach portion control, supplement use and energy balance.

**Claims vs. Reality**
- **Company claim:** "the world's first adaptive nutrition coach built for active individuals," which "tells you exactly what to eat, when to eat it, and why it matters"; goal options include "Dominate my Hyrox event", "Build muscle and get stronger" and "Improve my body composition", and its store listing says thousands of users "can recover faster, lose weight, gain muscle."
- **Independent findings:** none beyond store ratings and reviews; "over 3000 monthly age-group athletes" (company, April 2025) indicates modest scale. What its 144 four- and five-star reviews praise is the part worth copying: taking the guesswork out of what and when to eat ("Takes away the guesswork"), energy and results in training and racing, targets "planned around my Trainingpeaks sessions," Smart Meals ("The smart meals are GOAT") and access to human coaches.

**User Complaints / Weaknesses**
- In 142 hand-coded one-to-three-star reviews from nine countries (January 2023 to October 2026): price 31%, logging 28%, no free trial 28%, integrations including planned workouts 24%, targets seen as wrong, unrealistic or unsafe 20%, billing, cancellation or support 20%, bugs 18%, interface complexity 16%, AI quality 15%, rigid meal structure 13%, marketing that over-promises 10%. 61% raise price, the missing trial or billing.
- In reviewers' words: "They push you through a long quiz first, capture all your data, and then nonchalantly hit you with a $29/month paywall. No trial." "I train through runna and this app doesn't support a connection to it." "This app has wanted me to skip meals and fast through heavy training." "It wants me to eat breakfast at 7am and dinner at 6pm."

**Assessment**
The most direct overlap, and the proof that adaptive fueling sells: amateur-inclusive (HYROX, lifting and endurance goals), with targets that adapt to training, photo logging and meal guidance its users love. Its weaknesses are access and execution, not the science: no trial by policy, a premium price with a coaching ladder above it, planned-session sync centered on TrainingPeaks, and logging its users find clunky. It reaches users through champions, endurance media and, its reviewers say, paid social. A competitor that copies the fundamentals can win on everything around them.

#### 5. GENERAL-HEALTH FOOD SCORES (YUKA, ZOE, NUTRI-SCORE, APPLE)

**Overview**
- Yuka: about 89.5 million users (company counter, October 2026); #6 free US health and fitness app; scores are 60% nutritional quality (Nutri-Score based), 30% additives and 10% organic.
- ZOE: a free US photo app (May 2025) labels foods "Unprocessed, No Risk, Low Risk, Medium Risk, or Highest Risk"; the paid ZOE 2.0 scores foods 0-100.
- Nutri-Score: the European front-of-pack grade from A to E, calculated per 100 g.
- Apple: iOS 27 Visual Intelligence (September 2026) rates a photographed plate's processing, protein and sugar, free on iPhone 15 Pro and later.

**How It Works**
Each scores a food on its general-health profile per 100 g or per serving: energy, sugars, salt and saturated fat count against it; protein, fiber and plants count for it; processing and additives count against it in Yuka, ZOE and Apple.

**Claims vs. Reality**
- **Company claim:** ZOE co-founder Tim Spector: "People are crying out for clarity." Yuka: "92% of users have been buying fewer ultra-processed food" (company survey).
- **Independent findings:** Nutri-Score's owner excludes sport nutrition products by design; on Open Food Facts, Maurten's caffeinated gel grades D, Gatorade C, plain bagels C (NOVA 4) and honey E (Part 1.2 exhibit).

**User Complaints / Weaknesses**
- Yuka's additive weighting "doesn't take into consideration percentage within a formula"; "This app capitalizes on fear" (cosmetic chemist Jane Tsui, Glossy, 2024).
- ZOE's own logic marks red velvet cake 18/100 because it is "digested quickly, and with very little fibre", the exact property an athlete wants mid-session.

**Assessment**
The food-score habit is mainstream and now free at the operating-system level, so "we score food" is not a differentiator, and a position cannot rest on a score. Every existing score is a general-health score, context-blind by construction; a goal-aware score is useful only as feedback on a recommendation.

#### 6. WEARABLES ADDING FOOD (GARMIN, GOOGLE, OURA)

**Overview**
- Garmin added nutrition tracking with AI photo logging to Connect+ ($69.99/year) in January 2026; Google Health's $9.99/month AI coach (May 2026) logs meals by photo or dictation; Oura launched Meals with photo logging and Dexcom glucose data in May 2025.

**How It Works**
Food logging sits next to training and sleep data. Targets come from body size and activity: Garmin uses "height, weight, gender, activity level and average active calories"; Google sets a protein baseline of "1.2 to 1.4 grams per kilogram."

**Claims vs. Reality**
- **Company claim:** Garmin: "Users can now track their nutrition, health and fitness data in one app."
- **Independent findings:** Garmin's release includes no food-quality score, carbohydrate periodization or in-workout fueling; Google's protein baseline sits below the roughly 1.6 g/kg/day at which muscle gains plateau (Morton et al., 2018).

**User Complaints / Weaknesses**
- Not assessed; the launches are recent.

**Assessment**
The platforms own the training data and the wrist, and they are converging food into their apps as one more feature. Convergence rarely produces a category leader; it does turn photo logging into a free commodity.

### What Users Complain About

Hand-coded one-to-three-star App Store reviews, pulled from Apple's public review feeds on 5 October 2026. Each review was read and given every label that applied, so columns add up to more than 100%. Fuelin: 142 reviews from nine countries (January 2023 to October 2026). Hexis: 37 from three countries (May 2023 to August 2026). MacroFactor: 187 from four countries (September 2021 to September 2026).

| Complaint | Fuelin | Hexis | MacroFactor |
|-----------|--------|-------|-------------|
| Price or value | 31% | 27% | 24% |
| No free trial or free tier | 28% | 3% | 21% |
| Billing, cancellation or support | 20% | 24% | 11% |
| Logging (clunky entry, database gaps, units) | 28% | 54% | 40% |
| Integrations, including planned workouts | 24% | 16% | 4% |
| Targets seen as wrong, unrealistic or unsafe | 20% | 5% | 12% |
| Bugs and performance | 18% | 54% | 14% |
| Interface complexity | 16% | 22% | 13% |
| AI quality | 15% | 3% | 5% |
| Rigid structure (meal times, preferences) | 13% | 5% | 4% |
| Marketing that over-promises | 10% | 11% | 5% |

Three patterns hold. Logging is a top complaint everywhere. Access (price, the missing trial, billing) dominates the premium fueling app: 61% of Fuelin's low-rated reviews raise at least one of the three. And Fuelin's users add integrations and target quality, the two places where adaptive fueling meets an amateur's real plan and real meals. Hexis's sample is small. Inside Fuelin's target complaints, the most common are targets too low (mostly carbohydrate, 10 reviews) and targets rewritten after a workout differs from the plan, including meals already eaten (6). MacroFactor's are calories set too low for active users, and three women say it ignores female physiology.

### What Users Praise

The same review feeds, four- and five-star reviews (counts approximate):

| App | What users praise most |
|-----|------------------------|
| Fuelin (144) | Taking the guesswork out of what and when to eat, synced to the training plan (~70): "Fuelin reads my training program and gives simple, clear macro recommendations and fuelling timing for every session." Then performance, energy and recovery (~43), ease of use including the traffic-light carb guide (~27: "at a glance, you know what level of carb to aim for"), learning how to fuel (~24), body composition (~23), responsive coaches (~23), forward sync from TrainingPeaks (~21), race-day fueling and sweat tests (~16) and Smart Meals (~11) |
| Hexis (19) | Carbohydrate periodized around training (~10), quick logging once learned (~7), seeing "future sessions" from TrainingPeaks (~6) |
| MacroFactor (464) | Fast, low-friction logging (~170: "If carbs manager is a Ferrari to log food, MacroFactor is a rocket."), the adaptive expenditure algorithm (~95), switching from MyFitnessPal (~95), polish and an accurate database (~65 each), and price with no ads (~55). Users name creators (Jeff Nippard, Will Tennyson) and friends as how they found it, and one says "ChatGPT recommended I try MacroFactor." |

What works, and is worth copying: targets from the plan ahead, a glanceable carbohydrate level per meal, fast logging, an expenditure estimate that learns, and creator-led word of mouth. Caveat: Fuelin's five-star reviews arrive in bursts (nine in five days around the Smart Meals launch), which suggests some were solicited.

### Pricing and Access

Prices from each app's US App Store in-app purchase list, 5 October 2026, unless noted.

| App | Monthly | Yearly | Free tier | Free trial | Above the base plan |
|-----|---------|--------|-----------|------------|---------------------|
| Fuelin | $29.00 | $139.00 | No | No ("We don't offer a free trial") | Copilot $99/month or $399/year; 1:1 coaching $1,500/month (website) |
| Hexis | €24.99 | €129.99 | No | No (Roadman Cycling, 2026) | None listed (sold on the web) |
| MacroFactor | $11.99 | $71.99 | No | 7 days | None |
| MyFitnessPal | $19.99 | $79.99 | Yes | Yes (Premium) | None |
| Cronometer | $10.99 | $59.99 (Gold) | Yes | Not checked | None |
| Lose It! | $9.99 | $39.99 | Yes | Not checked | Lifetime $49.99-$59.99 |
| Mavr | $14.99 | $79.99 (offers from $39.99) | No ("requires an active auto-renewing subscription") | Not stated | None |
| Cal AI | Varies | $29.99 | Not checked | Not checked | None |

None of the session-based fueling apps reviewed (Fuelin, Hexis, Mavr) offers a free tier, and their listings and FAQs offer no trial. Fuelin and Hexis charge roughly twice what the large trackers do; Mavr prices near them but has 8 US ratings. Among the apps reviewed, none pairs session-based targets with a free tier, a trial and a tracker-level price.

### How They Reach Users

| Brand | How it reaches users |
|-------|----------------------|
| Fuelin | Pro endurance endorsements (Jan Frodeno, Daniela Ryf, Holly Lawrence, Ben Kanute and others on its homepage), endurance events (a gravel cyclist "discovered Fuelin at Unbound 200"), articles and the "Fuelin Sessions" podcast, its own coaches and the TrainingPeaks integration. A few reviewers mention Facebook ads ("Don't believe the FB hype"), "a high volume of marketing emails" and social-media recommendations. |
| Hexis | Elite teams (World Tour cycling, Premier League football) and coaching platforms, a disclosed media partnership (Roadman Cycling) and a funded direct-to-consumer push (June 2026). |
| MyFitnessPal | Scale and habit (280 million+ members), App Store search, the HYROX Tampa title partnership with in-app fueling content, and the Cal AI acquisition. |
| Cal AI | Influencer marketing (its COO ran it) and TikTok, credited by observers for its rise; AI search terms drove a quarter of its search downloads (Sensor Tower, 2026). |
| Strava and Runna | Community and a free tier: Strava's new clubs nearly quadrupled in 2025 to 1 million. Strava bought Runna in April 2025, and Runna is a HYROX online training partner. |

Distribution, not accuracy, decided the last round of food apps: Cal AI drew an estimated 400,000 downloads and $2 million in revenue in a month against 20,000 and $20,000 for SnapCalorie, the better-validated product (Sensor Tower, 5 October 2026). The fueling apps borrow authority from pros and buy reach; the apps that scaled earned it from creators and communities.

### Operating Approaches

**Approach 1: The calorie budget.** Used by: MyFitnessPal, Cal AI, Lose It!, Yazio. Strength: habit, scale and effortless logging. Weakness (structural): the budget is a weight tool; it treats a rest day and a race day the same and rewards eating less.

**Approach 2: The adaptive macro algorithm.** Used by: MacroFactor, RP Diet Coach, Carbon. Strength: rigorous, and trusted by evidence-minded lifters. Weakness (structural): built around body-weight trend, measured over days and weeks rather than sessions.

**Approach 3: The pro-led fueling plan.** Used by: Fuelin, Hexis, FoodCoach. Strength: periodized, guideline-based targets that users credit with taking the guesswork out. Weakness (structural for amateurs): built and sold for the committed (no free trials, premium prices, coaching upsells, pro endorsements), with planned-session sync centered on coaching platforms. Mavr, a newer endurance and HYROX app with macros that adjust to training, sits between this approach and the trackers on price ($79.99 a year) but requires a subscription to use and has 8 US ratings.

**Approach 4: The general-health score.** Used by: Yuka, ZOE, Nutri-Score, Lifesum, Apple. Strength: simple, free and habitual. Weakness (structural): a per-100 g health profile with no input for training.

**Approach 5: The wearable add-on.** Used by: Garmin, Google, Oura; WHOOP reads food from other apps. Strength: owns training data and distribution. Weakness (executional, for now): food is a feature with generic targets.

**Approach 6: The healthy-swap scanner.** Used by: Swapd, NutriSwap, HealthySwap and FoodSwitch; Yuka suggests alternatives. Strength: a concrete, low-effort action. Weakness (structural): general-health swaps (less sugar, fat or additives) with no goal or training input, and tiny reach.

### The Failure Modes

**1. Context blindness (fundamental for budgets and health scores)**
A per-day budget and a per-100 g score cannot see the session ahead, while the guidelines tie nutrition to "the needs of daily training sessions" (Thomas et al., 2016). The incumbents cannot fix this without abandoning their model.

**2. Portion error (fundamental to photo logging, shrinking)**
Photos undercount energy by about a third (NIH, 2026) while identifying foods well (Li et al., 2024). Any product that treats a photo's calorie total as precise inherits the error; ranges and a single portion question when it matters inherit less of it.

**3. Access barriers (fundamental to the premium fueling apps)**
No free trial by policy (Fuelin's FAQ; Hexis per Roadman Cycling), prices around $130-$140 a year, a paywall that appears after a long onboarding, and cancellation complaints: 61% of Fuelin's low-rated reviews raise price, the missing trial or billing.

**4. Plan blindness outside coached platforms (executional)**
Adaptive targets are only as good as the plan they read. Fuelin's planned-session sync is praised for TrainingPeaks, the coached athlete's platform, while its reviewers report Runna unsupported, Garmin plans that don't populate and Strava or Final Surge workouts that update targets only after the session (integrations, including planned workouts: 24% of low-rated reviews).

**5. Logging burden (fundamental to every tracker)**
Logging is a top complaint for Fuelin (28%), Hexis (54%) and MacroFactor (40%), and new MyFitnessPal users omitted 18% of foods (Chen et al., 2019). Adherence breaks where logging is slow.

**6. Unsafe targets and weight-loss defaults**
Calorie apps make a deficit the default success state, and weight management is the motive most associated with later disordered behavior among app users (Hahn et al., 2024). Fueling apps can fail the same way: 20% of Fuelin's low-rated reviews call its targets wrong, unrealistic or unsafe, including one told to "skip meals and fast through heavy training."

**7. Pro faces, all-in framing and pro-led distribution (solvable)**
Fueling apps sell pro proof to people with day jobs, and their consumer traction is thin: Hexis has 29 US ratings, Saturday 154 and Mavr 8, and Supersapiens shut down in February 2024 on about €1.3M of 2023 revenue (DC Rainmaker). The aspiration is not the failure: people who train for something big want what the pros have, and nobody wants to be called an amateur (founder insight, 6 October 2026). The failure is selling it through the pros' life: champions' faces, all-in programs and pro prices.

### What Nobody Does

**No player combines:**
1. Calorie and macro targets that adapt to planned sessions (the proven fundamental), explained line by line and protected by an energy floor
2. A free start: a free tier and a trial without a subscription, with the price shown before setup
3. A price near the trackers' (about $60 a year), not the coaching apps' ($130-$140)
4. Planned sessions from the apps most athletes use (Runna, Garmin, intervals.icu, Apple Health), not only TrainingPeaks
5. Logging in seconds, in grams or ounces, with a food database for each launch market and targets that never rewrite a meal already eaten
6. Distribution through the communities where people train (clubs, gyms, coaches, creators with day jobs) instead of champions and paid reach

Honest reading: Fuelin covers 1, and 4 for TrainingPeaks users. Hexis covers 1 for endurance athletes. Mavr covers 1 and part of 3 for endurance and HYROX athletes, but requires a subscription and has 8 US ratings. MacroFactor adapts targets to body weight, with a trial but no free tier. MyFitnessPal and Cronometer have free tiers but fixed targets. Strava owns the community channel but not fueling, and it bought Runna. No single product combines all six, and every piece is copyable: the gap is a position and an execution, not a moat.

This is the strategic gap.

## PART 3: WHERE THE MARKET IS MOVING

### The Participation Wave: Goal-Driven Amateur Sport
- **HYROX reports growth from about 175,000 competitors (2022/23) to "over 1.5 million participants" (2025/26)** and targets "more than 2 million athletes" in 2026/27 across 107 race weekends (Infront; HYROX via endurance.biz, July 2026). Press counts for 2025/26 range from 1.3 to 1.5 million, all unaudited organizer figures that count doubles and relays; an independent results-based study counted 278,063 participants across HYROX's first five seasons, through 2023/24 (Fernández-Navarrete et al., 2026). About 70% of participants are first-timers (Infront).
- **London Marathon ballot applications rose from 578,304 (2024 race) to 1,338,544 (2027 race)**, and 35% of UK applicants were aged 18-29 (London Marathon Events, May 2026). London set a world record of 59,830 finishers in April 2026.
- **Strava passed 200 million users** (July 2026). 43% of its users wanted "to conquer a big race or event in 2025," and Gen Z is "75% more likely than Gen X to say their main motivation for exercise is a race or event" (Strava, 2025).
- **Clubs are the new front door.** New clubs on Strava "nearly quadrupled in 2025, reaching 1 million total clubs"; running clubs grew 3.5x and club-organized events 1.5x (Strava via SGB Media, December 2025), after a 59% rise in running-club participation in 2024 (Strava).
- **Caveat: the running base is slowing.** US same-race participation grew 5.0% in 2025, down from 10% and 8% in the two prior years, and marathons grew 1.5% (RunSignup, February 2026): "the post-COVID boom has passed."

### Strength and Hybrid Training
- **81 million Americans belonged to a gym in 2025 (+5.2%).** Gen Z (18-24) penetration was 35.5%, the highest of any age group, and free weights were the "fastest-growing equipment category since 2021" (Health & Fitness Association, April 2026).
- **Gen Z is 2x more likely than Gen X to call weight training their primary sport, and 54% of Strava users track multiple activities** (Strava, December 2025).
- **58% of lifters say conflicting advice makes it hard to know how best to train** (Les Mills Global Fitness Report, 2026).
- **HYROX is endurance-dominant and very hard.** In a simulated race, recreational athletes spent 79.5% of 86.5 minutes above 90% of maximum heart rate (Brandt et al., 2025, n=11), and running makes up about 50% of race time (Rappelt et al., 2026). We found no peer-reviewed HYROX fueling study (PubMed and Europe PMC search, 5 October 2026).
- **70% of Americans try to consume protein, and 23% follow a high-protein diet, the most common diet three years running** (IFIC, 2025).
- **Signs of saturation:** "Good source of protein" as a definition of healthy food fell from 38% to 33% (IFIC, 2026), and BellRing (Premier Protein) cut its FY2026 growth guidance to 1-3% (August 2026).
- **Carbohydrate has no equivalent wave.** Athletes' mean daily carbohydrate intakes range from 2.4 to 4.6 g/kg across 28 studies (Janiczak et al., 2022), below the 5-7 g/kg the guidelines set for about an hour of moderate training a day (Thomas et al., 2016).
- **Caveat:** Gen Z is "61% more" likely than Gen X to lift for aesthetics (Strava, 2025), and 64.6% of resistance-trained women track calories, mostly to restrict for aesthetic weight loss (SantaBarbara et al., 2024). Many lifters want body-composition change.

### The Weight-Loss Paradigm Is Re-Tooling Around GLP-1s
- **12% of US adults currently take a GLP-1** (KFF, November 2025). 11% take one for weight loss, up from 3% in 2024, and adult obesity fell to 36.8% from 39.9% in 2022 (Gallup, July 2026).
- **WeightWatchers filed for Chapter 11 on 6 May 2025** and emerged in June. By Q2 2026 its total subscribers had fallen 21.4% to 2.5 million while clinical (GLP-1) subscribers grew 55.7% (company filings). Noom cut coaching staff over "a revenue mix shift... towards our fast-growing GLP-1-related products" (NJBIZ, February 2025). MyFitnessPal and Lose It! added GLP-1 medication tracking.
- **Caveat: weight management is not fading as a goal.** "Weight loss/weight management" as a benefit sought from diet rose to 40% (+10 points since 2022), and calorie counting rose from 12% to 15% of US adults (IFIC, 2024 and 2025). The calorie category is not dying; it is re-tooling around medication and drifting further from people who train.

### Incumbents Are Converging on Performance and Photos
- **MyFitnessPal bought Cal AI and runs it "for performance-oriented members"** (March 2026), sponsors HYROX Tampa with fueling content (August 2026) and launched an AI Coach that covers pre-workout choices (August 2026).
- **Hexis raised $2.1M to go direct-to-consumer** (June 2026); **MacroFactor launched a workouts app** (January 2026); **Strava bought Runna** (April 2025), which publishes race-day nutrition checklists and is a HYROX online training partner.
- **The official HYROX slots are taken:** MyFitnessPal is HYROX Tampa's title partner and Myprotein HYROX's official global nutrition partner, so the open channels are gyms, clubs, coaches and creators.
- **AI photo logging became table stakes in under two years:** Hexis (November 2024), MacroFactor (March 2025), Fuelin (April 2025), Oura and ZOE (May 2025), Cronometer (September 2025), Garmin (January 2026), Google Health (May 2026). 28% of health and fitness apps now bid on AI keywords (Sensor Tower, February 2026), and Apple's iOS 27 gives away a photo health rating (September 2026).
- **Health and fitness app spending hit a record $4.5 billion in 2025 (+13%) while downloads grew only 0.8%** (Sensor Tower, February 2026): growth comes from monetizing engaged users, not from finding new ones.

## KEY DATA POINTS

| Data Point | Number | Source |
|-----------|--------|--------|
| MyFitnessPal members | 280M+ (cumulative) | MyFitnessPal press releases, 2026 |
| Cal AI downloads / annual revenue | 15M+ / over $30M | TechCrunch, March 2026 |
| Cal AI positioning after acquisition | "for performance-oriented members" | MyFitnessPal press release, March 2026 |
| Photo-app energy undercount per meal | 252-345 kcal (about 33%) | NIH/NIDDK, ASN Nutrition 2026 abstract (preliminary) |
| AI food identification | 87-97% (Foodvisor, MyFitnessPal) | Li et al., *Nutrients*, 2024 |
| AI mixed-dish energy error | -76% to +270% | Li et al., *Nutrients*, 2024 |
| General LLM protein error (MAPE) | about 61% | Fridolfsson et al., 2025 |
| US label calorie tolerance | Misbranded only above +20% | 21 CFR 101.9(g)(5), current eCFR |
| Athletes' self-reported intake vs. doubly labeled water | -19% (11 studies) | Capling et al., 2017 |
| Wrist-device energy expenditure | No device within 20% | Shcherbina et al., 2017 |
| Daily carbohydrate by training load | 3-5 / 5-7 / 6-10 / 8-12 g/kg | Thomas, Erdman and Burke, 2016 |
| Carbohydrate during exercise | 30-60 g/h (1-2.5 h); up to 90 g/h (over 2.5-3 h) | Thomas, Erdman and Burke, 2016 |
| Protein breakpoint for muscle gain | 1.62 g/kg/day (95% CI 1.03-2.20) | Morton et al., 2018 |
| Protein per dose | 0.25 g/kg or 20-40 g; 700-3,000 mg leucine | Jäger et al., ISSN, 2017 |
| Nutri-Score for sport nutrition products | "cannot be used" | Santé publique France Q&A, 2025 |
| Marathoners meeting 60-90 g/h in race | 5.3% (2 of 38) | *European Journal of Sport Science*, 2025 |
| Marathon in-race carbohydrate | 35 g/h (n=160) | Jiménez-Alfageme et al., 2025 |
| Science-based race carbohydrate strategy vs. free choice, non-elite marathon | 4.7% (10 min 55 s) faster | Hansen et al., 2014 |
| Marathoners who hit the wall | 28% of men, 17% of women (1.9M results) | Smyth, 2021 |
| Recreational athletes at risk of low energy availability | 43-47% (screening) | Henninger et al., 2024; Lane et al., 2019 |
| Non-elite athletes meeting daily carbohydrate guideline | 45.7% (vs. 87.1% reaching 1.2 g/kg protein) | Masson and Lamarche, 2016 |
| Americans who don't know their protein needs | 53% (plus 26% unsure) | IFIC protein spotlight, 2025 |
| Amateurs who know the glycogen-refuel carbohydrate dose | 1.8% | Csanaky et al., 2025 |
| Nutrition education vs. intake, young endurance athletes | Knowledge up (78 to 85-86); intake unchanged | Heikkilä et al., 2019 |
| Weight loss vs. adherence and diet type, four popular diets | r = 0.60 (adherence) vs. r = 0.07 (diet type) | Dansinger et al., 2005 |
| Swap offer vs. Nutri-Score label, basket nutrient score | B = -9.58 vs. -3.28 (n=550) | Jansen et al., 2021 |
| Swaps added to Nutri-Score | d = -0.48; low-knowledge shoppers benefited most (n=428) | Schruff-Lim et al., 2024 |
| Habit automaticity plateau | Median 66 days (range 18-254) | Lally et al., 2010 |
| Gamification effect on physical activity | g = 0.42 overall; g = 0.23 vs. non-gamified versions | Mazeas et al., 2022 |
| Gamified vs. non-gamified health apps | +489 steps/day; no difference in dietary outcomes | Nishi et al., 2024 |
| People with an eating disorder who said MyFitnessPal contributed | 73% | Levinson et al., 2017 |
| HYROX participants | About 175,000 (2022/23) to over 1.5M (2025/26) | Infront; HYROX, 2026 |
| HYROX 2026/27 target | 2M+ athletes, 107 race weekends | HYROX, July 2026 |
| HYROX time above 90% max heart rate | 79.5% of 86.5 min (n=11) | Brandt et al., 2025 |
| London Marathon ballot applications | 578,304 (2024 race) to 1,338,544 (2027 race) | London Marathon Events, 2026 |
| US gym members / Gen Z penetration | 81M (+5.2%) / 35.5% | Health & Fitness Association, 2026 |
| US adults currently taking a GLP-1 | 12% | KFF, November 2025 |
| WeightWatchers subscribers, Q2 2026 | 2.5M (-21.4%); clinical +55.7% | WeightWatchers, August 2026 |
| US adults following calorie counting | 12% (2024) to 15% (2025) | IFIC, 2024 and 2025 |
| Health and fitness app spending, 2025 | $4.5B (+13%); downloads +0.8% | Sensor Tower, February 2026 |
| MacroFactor users | 600K+ | MacroFactor annual report, 2026 |
| Hexis seed round | $2.1M (June 2026) | Silicon Republic, 2026 |
| Fuelin scale and price | 65K+ downloads; 4.5 stars on 1,267 US ratings; Autopilot $29/month or $139/year, Copilot $99/month or $399/year | Fuelin; US App Store, 5 October 2026 |
| Fuelin's free-trial policy | "We don't offer a free trial" | Fuelin FAQ, October 2026 |
| Fuelin 1:1 coaching | $1,500/month; consultation $500 for 60 minutes | fuelin.com/coaches, October 2026 |
| Fuelin low-rated reviews raising price, trial or billing | 61% of 142 (hand-coded) | App Store reviews from nine countries, January 2023 to October 2026 |
| Fuelin low-rated review complaints | Price 31%, logging 28%, no trial 28%, integrations 24%, targets 20% | Same |
| Logging complaints in low-rated reviews | Fuelin 28%, Hexis 54%, MacroFactor 40% | Same feeds, hand-coded |
| Fuelin's most praised theme | "Takes the guesswork out" (~70 of 144 four- and five-star reviews) | Same feeds |
| Tracker prices (yearly) | MacroFactor $71.99 (7-day trial, no free tier); MyFitnessPal $79.99; Cronometer $59.99; Lose It! $39.99; Cal AI $29.99 | US App Store, 5 October 2026 |
| Cal AI vs. SnapCalorie, monthly downloads | About 400K vs. 20K | Sensor Tower estimates, 5 October 2026 |
| Clubs on Strava | 1M (new clubs nearly 4x in 2025; running clubs 3.5x) | Strava via SGB Media, December 2025 |
| HYROX affiliate gyms | About 15,000 | SportsPro, June 2026 |
| HYROX ownership | Majority stake sold to an L Catterton-led consortium (September 2026) | Athletech News, September 2026 |
| HYROX participants, independent count | 278,063 across five seasons to 2023/24 | Fernández-Navarrete et al., 2026 |
| Digital self-monitoring and weight loss | Linked in 74% of occurrences (39 RCTs) | Patel et al., 2021 |
| Eating disorders, elite athletes vs. controls | 13.5% vs. 4.6% (clinical or subclinical) | Sundgot-Borgen and Torstveit, 2004 |
| Ketogenic diets and performance | "largely neutral or detrimental" | Leaf et al., ISSN, 2024 |
| Yuka users | About 89.5M | Yuka homepage counter, October 2026 |

## MARKET LANDSCAPE OBSERVATIONS

1. **The calorie belongs to weight management, and its owners are doubling down.** MyFitnessPal (listed as "Calorie Counter"), Cal AI, WeightWatchers and Noom are all re-tooling around weight loss and GLP-1 medication. The better they serve that job, the less they fit people who train.

2. **The leader has noticed the athlete and is answering with line extension.** Cal AI "for performance-oriented members," a HYROX Tampa sponsorship and an AI Coach bolt performance content onto a calorie counter. The incumbent has validated the demand without changing its unit.

3. **Adaptive fueling is proven and wanted; its users praise the science and complain about access.** Fuelin's most praised theme is taking "the guesswork out" (about 70 of 144 positive reviews), while 61% of its low-rated reviews raise price, the missing trial or billing, and the top product complaints are logging (28%) and integrations (24%). The fundamentals can be copied; the access can be rebuilt.

4. **The fueling apps were built for the committed few, and it shows in their reach.** No free trials, prices of $130-$140 a year, coaching ladders up to $1,500 a month and champions on the homepage. Fuelin reported about 3,000 monthly age-group athletes in 2025 and has 1,267 US ratings; Hexis has 29. And "fuel" is taken: Fuelin carries it in its name and Hexis built its science story on it.

5. **The audience is large, goal-driven and under-fueled.** HYROX reports more than 1.5 million participants (an independent results-based count found 278,063 across its first five seasons), London drew 1.34 million ballot applications, and Gen Z has the highest gym membership rate. Yet only 2 of 38 marathoners in one study hit the race carbohydrate target.

6. **Distribution decides consumer nutrition apps.** Cal AI drew about twenty times SnapCalorie's monthly downloads; MacroFactor's users credit creators and friends; Strava's clubs reached 1 million. The official HYROX nutrition slots belong to MyFitnessPal and Myprotein, which leaves gyms, clubs, coaches and creators as the open channels.

7. **The evidence supports simple rules and low-friction habits, within honest limits.** The best-supported rules are few: fuel hard and long sessions adequately and cover daily protein, while timing matters little for muscle once totals are met (Schoenfeld et al., 2013). Knowledge alone rarely changes intake (Heikkilä et al., 2019), adherence predicted results in a weight-loss trial (Dansinger et al., 2005), and swaps helped grocery shoppers (Jansen et al., 2021; Schruff-Lim et al., 2024). No trial has tested adaptive fueling apps or swaps in amateurs, and we found no HYROX fueling study.

8. **The opportunity is real, thin and time-limited.** No player combines all six capabilities in What Nobody Does, but every piece is copyable, and three sides are moving: Hexis's direct-to-consumer push, MacroFactor's workouts, and Strava's Runna, which already publishes race-day nutrition checklists. The winner will be the first brand in these athletes' minds, not the first to ship the feature.

## SOURCES

**Incumbent calorie trackers and AI photo logging**
- [TechCrunch: MyFitnessPal has acquired Cal AI (2 March 2026)](https://techcrunch.com/2026/03/02/myfitnesspal-has-acquired-cal-ai-the-viral-calorie-app-built-by-teens/)
- [MyFitnessPal: Acquires Cal AI (GlobeNewswire, 2 March 2026)](https://www.globenewswire.com/news-release/2026/03/02/3247439/0/en/MyFitnessPal-Acquires-Cal-AI-Expanding-on-its-Position-as-the-Leading-Player-in-Digital-Nutrition-Tracking.html)
- [MyFitnessPal: 2026 Summer Release (GlobeNewswire, 25 August 2026)](https://www.globenewswire.com/news-release/2026/08/25/3350516/0/en/myfitnesspal-announces-its-2026-summer-release.html)
- [MyFitnessPal: GLP-1 Support launch (GlobeNewswire, 28 April 2026)](https://www.globenewswire.com/news-release/2026/04/28/3282728/0/en/myfitnesspal-launches-comprehensive-glp-1-support-helping-users-stay-consistent-and-build-habits-alongside-medication-to-maximize-their-experience.html)
- [MyFitnessPal: Calorie Counter, US App Store listing and in-app purchases](https://apps.apple.com/us/app/id341232718)
- [MyFitnessPal Premium pricing](https://www.myfitnesspal.com/premium)
- [Reuters via WIMZ: MyFitnessPal explores sale (9 April 2026)](https://wimz.com/2026/04/09/fitness-and-health-app-myfitnesspal-explores-sale-sources-say/)
- [Athletech News: MyFitnessPal becomes HYROX Tampa title partner (11 August 2026)](https://athletechnews.com/myfitnesspal-hyrox-peloton-robin-arzon-performance-nutrition/)
- [TechCrunch: Cal AI built by two teenagers (16 March 2025)](https://techcrunch.com/2025/03/16/photo-calorie-app-cal-ai-downloaded-over-a-million-times-was-built-by-two-teenagers/)
- [Cal AI: Calorie Tracker, US App Store listing and reviews](https://apps.apple.com/us/app/id6480417616)
- [Cal AI website and FAQ](https://www.calai.app/)
- [Sensor Tower: Q3 2025 top US health and fitness apps by revenue](https://sensortower.com/blog/2025-q3-unified-top-5-health%20and%20fitness-revenue-us-600af518241bc16eb8dce802)
- [Sensor Tower: Health and fitness apps and AI (February 2026)](https://sensortower.com/blog/health-and-fitness-apps-ai)
- [Lose It!: US App Store listing (GLP-1 tracking)](https://apps.apple.com/us/app/id297368629)
- [Apple US App Store charts: top grossing, Health & Fitness (read 5 October 2026)](https://itunes.apple.com/us/rss/topgrossingapplications/limit=50/genre=6013/json)
- [Apple US App Store charts: top free, Health & Fitness (read 5 October 2026)](https://itunes.apple.com/us/rss/topfreeapplications/limit=50/genre=6013/json)
- [Cronometer: US App Store listing and in-app purchases](https://apps.apple.com/us/app/id1145935738)
- [Cronometer: Photo Logging launch (September 2025)](https://www.newswire.ca/news-releases/cronometer-launches-premium-photo-logging-fast-verified-nutrition-tracking-for-real-life-892631239.html)

**Accuracy of photo, AI and manual logging**
- [Healio: AI photo-based calorie tracking tools underestimate by 33% (4 August 2026)](https://www.healio.com/news/primary-care/20260804/ai-photobased-calorietracking-tools-underestimate-them-by-33)
- [EurekAlert: ASN NUTRITION 2026 release on photo apps (25 July 2026)](https://www.eurekalert.org/news-releases/1136415)
- [Li et al., *Nutrients* 2024: AI food recognition apps](https://pmc.ncbi.nlm.nih.gov/articles/PMC11314244/)
- [Fridolfsson et al., *Current Developments in Nutrition* 2025: LLM nutrient estimation](https://pmc.ncbi.nlm.nih.gov/articles/PMC12513282/)
- [Mu et al., ACM BCB 2025: portion as the bottleneck](https://pubmed.ncbi.nlm.nih.gov/42502812/)
- [Evenepoel et al., JMIR 2020: MyFitnessPal vs. reference database](https://pubmed.ncbi.nlm.nih.gov/33084583/)
- [Diktas et al., *J Nutr* 2025: MyFitnessPal vs. weighed intake](https://pubmed.ncbi.nlm.nih.gov/41022156/)
- [Chen et al., *Nutrition* 2019: real-world MyFitnessPal logging](https://pubmed.ncbi.nlm.nih.gov/30184514/)
- [Morello et al., *J Hum Nutr Diet* 2025: app validity in endurance athletes](https://pubmed.ncbi.nlm.nih.gov/41133373/)
- [21 CFR 101.9, nutrition labeling (eCFR)](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-101/subpart-A/section-101.9)
- [Urban et al., *J Am Diet Assoc* 2010: stated vs. measured calories](https://pubmed.ncbi.nlm.nih.gov/20102837/)
- [Novotny et al., *Am J Clin Nutr* 2012: almond energy](https://pubmed.ncbi.nlm.nih.gov/22760558/)
- [Capling et al., *Nutrients* 2017: athletes' self-report vs. doubly labeled water](https://pubmed.ncbi.nlm.nih.gov/29207495/)
- [Shcherbina et al., *J Pers Med* 2017: wearable energy expenditure](https://pubmed.ncbi.nlm.nih.gov/28538708/)

**Sports nutrition science**
- [Thomas, Erdman and Burke 2016: ACSM/AND/DC joint position (PubMed)](https://pubmed.ncbi.nlm.nih.gov/26891166/)
- [Thomas, Erdman and Burke 2016: full text (Dietitians of Canada)](https://www.dietitians.ca/DietitiansOfCanada/media/Documents/Resources/noap-position-paper.pdf)
- [Jäger et al. 2017: ISSN position stand, protein and exercise](https://pmc.ncbi.nlm.nih.gov/articles/PMC5477153/)
- [Jeukendrup 2017: training the gut for athletes](https://pubmed.ncbi.nlm.nih.gov/28332114/)
- [Morton et al. 2018: protein and resistance training meta-analysis](https://pubmed.ncbi.nlm.nih.gov/28698222/)
- [Schoenfeld and Aragon 2018: per-meal protein](https://pubmed.ncbi.nlm.nih.gov/29497353/)
- [Schoenfeld, Aragon and Krieger 2013: protein timing meta-analysis](https://pubmed.ncbi.nlm.nih.gov/24299050/)
- [Impey et al. 2018: fuel for the work required](https://pmc.ncbi.nlm.nih.gov/articles/PMC5889771/)
- [Mountjoy et al. 2023: IOC consensus on REDs](https://pubmed.ncbi.nlm.nih.gov/37752011/)
- [Forbes, Burke et al., *Sports Medicine Open* 2026: ultra-processed foods and athletes](https://pmc.ncbi.nlm.nih.gov/articles/PMC13582765/)
- [Forsyth and Mantzioris 2023: sports food use](https://pubmed.ncbi.nlm.nih.gov/36999372/)
- [Sarda et al. 2024: Nutri-Score and NOVA](https://pmc.ncbi.nlm.nih.gov/articles/PMC10897572/)
- [Santé publique France: Nutri-Score Q&A, 17 March 2025](https://www.santepubliquefrance.fr/sites/default/files/rdd/document/FAQ-updatedAlgo-V11.pdf)
- [Jansen et al. 2021: swaps vs. Nutri-Score labels](https://pubmed.ncbi.nlm.nih.gov/34863208/)
- [Heikkilä et al. 2019: nutrition education and an app in young endurance athletes](https://pubmed.ncbi.nlm.nih.gov/31540535/)
- [Leaf et al. 2024: ISSN position stand on ketogenic diets](https://pubmed.ncbi.nlm.nih.gov/38934469/)

**Behavior change, habits and gamification**
- [Schruff-Lim et al. 2024: swaps on top of Nutri-Score](https://pubmed.ncbi.nlm.nih.gov/38113984/)
- [Forwood et al. 2015: swaps offered in online shopping](https://pubmed.ncbi.nlm.nih.gov/26109390/)
- [Hartmann-Boyce et al. 2018: grocery store interventions, systematic review](https://pubmed.ncbi.nlm.nih.gov/29868912/)
- [Dansinger et al. 2005: adherence vs. diet type in four popular diets](https://pubmed.ncbi.nlm.nih.gov/15632335/)
- [Lally et al. 2010: how habits are formed in the real world](https://doi.org/10.1002/ejsp.674)
- [Gardner, Lally and Wardle 2012: making health habitual](https://pubmed.ncbi.nlm.nih.gov/23211256/)
- [Atoms (from Atomic Habits): US App Store listing, 10,717 ratings (read 6 October 2026)](https://apps.apple.com/us/app/id6474421906)
- [PeakByPros: US App Store listing, no ratings (read 6 October 2026)](https://apps.apple.com/us/app/id6745181932)
- [Mazeas et al. 2022: gamification and physical activity, meta-analysis of RCTs](https://pubmed.ncbi.nlm.nih.gov/34982715/)
- [Nishi et al. 2024: health apps with and without gamification, meta-analysis](https://pubmed.ncbi.nlm.nih.gov/39764571/)
- [Suleiman-Martos et al. 2021: gamification for diet in children and adolescents](https://pubmed.ncbi.nlm.nih.gov/34371989/)
- [Patel et al. 2021: digital self-monitoring and weight loss, 39 RCTs](https://pubmed.ncbi.nlm.nih.gov/33624440/)

**Under-fueling and athlete behavior**
- [*European Journal of Sport Science* 2025: race-day carbohydrate in endurance athletes](https://pmc.ncbi.nlm.nih.gov/articles/PMC12501108/)
- [Jiménez-Alfageme et al. 2025: Seville Marathon nutrition](https://pubmed.ncbi.nlm.nih.gov/40089940/)
- [Masson and Lamarche 2016: non-elite multisport athletes' intake](https://pubmed.ncbi.nlm.nih.gov/27176786/)
- [Janiczak et al. 2022: athletes' intake and knowledge](https://pubmed.ncbi.nlm.nih.gov/34706784/)
- [Hansen et al. 2014: planned gel intake in non-elite marathoners](https://pubmed.ncbi.nlm.nih.gov/24901444/)
- [Smyth 2021: hitting the wall in 1.9 million marathon results](https://pubmed.ncbi.nlm.nih.gov/34010308/)
- [Slater et al. 2016: LEA risk in recreational exercisers](https://pubmed.ncbi.nlm.nih.gov/26841435/)
- [Henninger et al. 2024: trail runners' LEA and disordered-eating risk](https://pubmed.ncbi.nlm.nih.gov/38288400/)
- [Lane et al. 2019: non-elite male endurance athletes' energy availability](https://pubmed.ncbi.nlm.nih.gov/31581498/)
- [McHaffie et al. 2025: self-report vs. doubly labeled water in LEA](https://pubmed.ncbi.nlm.nih.gov/39145767/)
- [Csanaky et al. 2025: amateur endurance athletes' nutrition knowledge](https://pubmed.ncbi.nlm.nih.gov/41305679/)
- [IFIC Spotlight: Perceptions of Protein (July 2025)](https://ific.org/wp-content/uploads/2025/07/IFIC-Spotlight-Survey-Protein-Perceptions.pdf)
- [SantaBarbara et al. 2024: calorie tracking in resistance-trained women](https://pubmed.ncbi.nlm.nih.gov/39579199/)

**Tracking and eating-disorder risk**
- [Levinson et al. 2017: MyFitnessPal and eating disorders](https://pubmed.ncbi.nlm.nih.gov/28843591/)
- [Hahn et al. 2024: weight-related self-monitoring apps, longitudinal](https://pubmed.ncbi.nlm.nih.gov/39113131/)
- [Jospe et al. 2018: 12-month RCT of self-monitoring](https://pubmed.ncbi.nlm.nih.gov/29951219/)
- [Sundgot-Borgen and Torstveit 2004: eating disorders in elite athletes](https://pubmed.ncbi.nlm.nih.gov/14712163/)
- [Anderberg et al. 2025: systematic review of diet and fitness apps](https://pubmed.ncbi.nlm.nih.gov/39671845/)

**Performance-nutrition, lifter and food-score competitors**
- [MacroFactor annual report 2026](https://macrofactor.com/annual-report-2026/)
- [MacroFactor: US App Store listing](https://apps.apple.com/us/app/macrofactor-macro-tracker/id1553503471)
- [MacroFactor: AI food logging announcement](https://macrofactor.com/ai-food-logging/)
- [Hexis homepage](https://www.hexis.live/)
- [Hexis athlete app page](https://hexis.live/athlete-app)
- [Hexis: about and founders](https://www.hexis.live/about)
- [endurance.biz: Hexis launches AI camera and voice logging (November 2024)](https://endurance.biz/2024/industry-news/advanced-nutrition-tracking-tools-from-hexis/)
- [Silicon Republic: Hexis seed round (22 June 2026)](https://www.siliconrepublic.com/start-ups/irish-sports-tech-platform-hexis-raises-seed-funding-round-wearables)
- [Enterprise Ireland: Hexis closes €1.85M seed round](https://www.enterprise-ireland.com/en/news/hexis-closes-1-85m-seed-round)
- [Hexis Live: US App Store listing](https://apps.apple.com/us/app/hexis-live/id1610334327)
- [Roadman Cycling: Hexis review (July 2026)](https://roadmancycling.com/blog/hexis-review)
- [Fuelin homepage](https://fuelin.com/)
- [Fuelin: US App Store listing](https://apps.apple.com/us/app/fuelin-performance-nutrition/id1579806995)
- [endurance.biz: Fuelin Smart Meals (November 2025)](https://endurance.biz/2025/industry-news/fuelin-launches-ai-powered-smart-meals-for-endurance-athlete-nutrition/)
- [Endurance Sportswire: Fuelin App 2.0 (April 2025)](https://www.endurancesportswire.com/fuelin-unveils-fuelin-app-2-0-a-revolution-in-personalized-nutrition-for-athletes/)
- [iTunes Search API: "food swap" apps in the US store (queried 5 October 2026)](https://itunes.apple.com/search?term=food+swap&entity=software&country=us)
- [Fuelin coaches and coaching prices](https://fuelin.com/coaches)
- [Fuelin podcasts ("Fuelin Sessions")](https://fuelin.com/podcasts)
- [App Store customer reviews feed: Fuelin (US; other countries use the same pattern)](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1579806995/sortby=mostrecent/json)
- [App Store customer reviews feed: Hexis Live (US)](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1610334327/sortby=mostrecent/json)
- [App Store customer reviews feed: MacroFactor (US)](https://itunes.apple.com/us/rss/customerreviews/page=1/id=1553503471/sortby=mostrecent/json)
- [MenuFit: US App Store listing](https://apps.apple.com/us/app/menufit-healthy-eating-out/id6746144481)
- [Sensor Tower: MenuFit overview (US)](https://app.sensortower.com/overview/6746144481?country=US)
- [Sensor Tower: Cal AI overview (US)](https://app.sensortower.com/overview/6480417616?country=US)
- [Hacker News discussion of Cal AI's marketing (April 2025)](https://news.ycombinator.com/item?id=43563580)
- [Runna: race-day nutrition checklist](https://support.runna.com/en/articles/12894662-runna-s-race-day-nutrition-checklist)
- [HYROX: online training partners](https://hyroxus.com/hyrox-online-training-partners/)
- [THG: Myprotein and HYROX official nutrition partnership](https://www.thg.com/news/myprotein-and-hyrox-partner-to-launch-exclusive-product-range)
- [FoodCoach: US App Store listing](https://apps.apple.com/us/app/foodcoach-nutrition-tracker/id6443778029)
- [Saturday: Pro Fuel & Hydration, US App Store listing](https://apps.apple.com/us/app/saturday-pro-fuel-hydration/id6444738746)
- [Mavr: US App Store listing](https://apps.apple.com/us/app/mavr-running-race-fuel/id6740541806)
- [DC Rainmaker: Supersapiens shutting down (29 February 2024)](https://www.dcrainmaker.com/2024/02/supersapiens-announces-shutting.html)
- [Yuka: how food products are scored](https://help.yuka.io/l/en/article/ijzgfvi1jq-how-are-food-products-scored)
- [Yuka homepage (user counter)](https://yuka.io/en/)
- [Yuka: social impact and user survey](https://yuka.io/en/social-impact/)
- [Yuka: US App Store listing](https://apps.apple.com/us/app/id1092799236)
- [Glossy: Yuka criticism (12 August 2024)](https://www.glossy.co/beauty/yuka-beauty-wellness-product-scanning-app/)
- [Athletech News: ZOE free food-risk app (13 May 2025)](https://athletechnews.com/new-app-from-zoe-labels-food-risk-in-seconds/)
- [ZOE 2.0 explained](https://zoe.com/learn/zoe-2-0-science-made-simple)
- [ZOE membership page (gut tests)](https://zoe.com/en-us/buymembership)
- [Country & Townhouse: ZOE app review and pricing](https://www.countryandtownhouse.com/food-and-drink/zoe-app-review/)
- [MacRumors: iOS 27 Health and Visual Intelligence](https://www.macrumors.com/guide/ios-27-health-app/)
- [Garmin: nutrition tracking in Garmin Connect (January 2026)](https://www.garmin.com/en-US/newsroom/press-release/sports-fitness/stay-on-top-of-nutrition-goals-in-garmin-connect/)
- [Garmin: Connect+ launch and pricing (March 2025)](https://www.garmin.com/en-US/newsroom/press-release/wearables-health/elevate-your-health-and-fitness-goals-with-garmin-connect/)
- [TechCrunch: Google Health AI coach launch (7 May 2026)](https://techcrunch.com/2026/05/07/googles-9-99-per-month-ai-health-coach-launches-may-19/)
- [Google Health Help: nutrition targets](https://support.google.com/googlehealth/answer/14237210?hl=en)
- [Oura: Meals and Glucose launch (6 May 2025)](https://ouraring.com/blog/introducing-metabolic-health/)

**Open Food Facts product pages (read 5 October 2026)**
- [Maurten Gel 100](https://world.openfoodfacts.org/product/73160717/gel-100-maurten)
- [Maurten Gel 100 Caf 100](https://world.openfoodfacts.org/product/73160731)
- [SiS GO Isotonic gel (French listing)](https://world.openfoodfacts.org/product/5025324002054)
- [Gatorade Orange 20 oz (US)](https://world.openfoodfacts.org/product/0052000328677)
- [Thomas' Plain Bagels (US)](https://world.openfoodfacts.org/product/0048121277079)
- [Quaker Lightly Salted Rice Cakes (US)](https://world.openfoodfacts.org/product/0030000169018)
- [Maribel honey](https://world.openfoodfacts.org/product/4056489361855)
- [Golden Sun Bio basmati rice](https://world.openfoodfacts.org/product/4056489095736)

**Market and participation trends**
- [Infront: HYROX from disruptive race to mass participation](https://www.infront.sport/blog/participation-sports/hyrox-from-a-disruptive-fitness-race-to-a-global-mass-participation-powerhouse)
- [endurance.biz: HYROX targets 2 million athletes in 2026/27 (20 July 2026)](https://endurance.biz/2026/industry-news/targeting-2-million-athletes-hyrox-expands-global-calendar-for-2026-27-season/)
- [Health Club Management: L Catterton-led consortium buys HYROX stake (8 September 2026)](https://www.healthclubmanagement.co.uk/health-club-management-news/L-Catterton-led-consortium-buys-Hyrox-stake-as-founders-regain-control/363576)
- [SportsPro: HYROX business model (17 June 2026)](https://www.sportspro.com/features/finance-investment/hyrox-business-model-mass-participation-private-equity-investment/)
- [The Star: The rise of HYROX (4 July 2026)](https://www.thestar.com.my/business/business-news/2026/07/04/the-rise-of-hyrox)
- [Brandt et al. 2025: first scientific study on HYROX](https://pubmed.ncbi.nlm.nih.gov/40230601/)
- [Rappelt et al. 2026: HYROX race-time analysis](https://pubmed.ncbi.nlm.nih.gov/42524284/)
- [London Marathon Events: record 1.33 million apply for 2027](https://www.londonmarathonevents.co.uk/london-marathon/article/record-133-million-people-apply-2027-tcs-london-marathon)
- [Endurance Sportswire: London Marathon finisher world record (April 2026)](https://www.endurancesportswire.com/tcs-london-marathon-breaks-finisher-world-record-with-59830-participants/)
- [RunSignup: 2025 Race Trends report (February 2026)](https://info.runsignup.com/wp-content/uploads/sites/3/2026/02/25-Race-Trends-FOR-ONLINE-compressed-1.pdf)
- [Strava: Year in Sport 2025](https://press.strava.com/articles/strava-releases-12th-annual-year-in-sport-trend-report-2025)
- [SGB Media: Strava Year in Sport 2025, clubs](https://sgbonline.com/stravas-year-in-sport-trend-report-highlights-gen-zs-passion-for-run/)
- [Strava: Year in Sport 2024, running clubs](https://press.strava.com/articles/strava-releases-annual-year-in-sport-trend)
- [Athletech News: L Catterton-led group acquires HYROX stake (8 September 2026)](https://athletechnews.com/hyrox-acquisition-l-catterton-led-group-co-founders-wndr-infront/)
- [Fernández-Navarrete et al. 2026: HYROX participation, five seasons](https://pubmed.ncbi.nlm.nih.gov/41380137/)
- [Strava: Samsung partnership, 200M+ users (July 2026)](https://press.strava.com/articles/strava-samsung-partner-for-pre-installs-on-new-galaxy-watches-routes-integration-into-samsung-health)
- [Strava to acquire Runna (PR Newswire, 17 April 2025)](https://www.prnewswire.com/news-releases/strava-to-acquire-runna-a-leading-running-training-app-302430939.html)
- [Health & Fitness Association: 81 million US members in 2025](https://www.healthandfitness.org/81-million-americans-were-members-of-a-fitness-facility-in-2025-new-hfa-report-finds/)
- [Les Mills: 2026 Global Fitness Report](https://www.lesmills.com/uk/articles/2026-global-fitness-report-strength-and-wellness-to-drive-next-wave-of-member-growth)
- [KFF Health Tracking Poll: GLP-1 use (November 2025)](https://www.kff.org/public-opinion/kff-health-tracking-poll-prescription-drug-costs-views-on-trump-administration-actions-and-glp-1-use/)
- [Gallup: GLP-1 usage reaches new high (July 2026)](https://news.gallup.com/poll/712157/glp-usage-reaches-new-high.aspx)
- [WeightWatchers: Q2 2026 results](https://www.globenewswire.com/news-release/2026/08/05/3339651/0/en/Weight-Watchers-Announces-Second-Quarter-2026-Results.html)
- [WeightWatchers: FY2025 Form 10-K (Chapter 11 dates)](https://www.sec.gov/Archives/edgar/data/105319/000119312526107176/ww-20251231.htm)
- [NJBIZ: Noom confirms layoffs (5 February 2025)](https://njbiz.com/noom-confirms-layoffs-at-the-digital-health-platform/)
- [IFIC 2024 Food & Health Survey](https://ific.org/wp-content/uploads/2025/07/2024-IFIC-Food-Health-Survey.pdf)
- [IFIC 2025 Food & Health Survey](https://ific.org/wp-content/uploads/IFIC-FH-Survey-Food-Nutrition-October-2025.pdf)
- [IFIC 2026 Food & Health Survey](https://ific.org/wp-content/uploads/2026-IFIC-Food-Health-Survey-Dietary-Guidance-and-Processed-Food.pdf)
- [BellRing Brands: Q3 FY2026 results (SEC exhibit)](https://www.sec.gov/Archives/edgar/data/0001772016/000162828026052137/brbrexh991-q32026earningsr.htm)

**Brand precedents cited in the strategy (read 6 October 2026)**
- [Nike: About Nike ("If you have a body, you are an athlete")](https://about.nike.com/en)
- [Dove Campaign for Real Beauty, launched in 2004 (Wikipedia)](https://en.wikipedia.org/wiki/Dove_Campaign_for_Real_Beauty)
- [Retail Brew: Dove's Real Beauty campaign turns 20 (9 April 2024)](https://www.retailbrew.com/stories/2024/04/09/the-dove-real-beauty-campaign-celebrates-20-years-with-a-commitment-to-forgo-ai-in-advertising)
