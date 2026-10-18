# GEO panel run log

This lists every panel run, plus every event that could move the readings. Read it before comparing two runs. Times are in UTC unless marked BST.

## Runs

| Date | Folder | Type | Coverage | Notes |
|---|---|---|---|---|
| 16 Oct 2026, 19:28–21:03 UTC | `runs/2026-10-16/` | Full baseline | Google UK 16/21, ChatGPT 63/63, Gemini 63/63, Perplexity 5/63 | Perplexity hit a sign-up wall. The Mac went offline before the last 5 Google queries. |
| 18 Oct 2026, 15:38–15:45 UTC | `runs/2026-10-18/` | Gap-fill, Google UK only | Google UK 5/5 | Completes the 16 Oct Google column. Ran before the T-shirt Week tees went live. |
| 18 Oct 2026, 19:23–19:29 UTC | `runs/2026-10-18-extra-query/` | Extra-query baseline | "water reactive windbreaker": Google UK 1, ChatGPT 3, Gemini 3 | Ran inside the T-shirt Week window, allowed because it is a non-brand query. Gemini run 2 cites the crooksldn.com HydroCuff page. |
| Fri 13 Nov 2026 (planned) | — | Core 8 plus the extra query | Google UK, ChatGPT, Gemini | Perplexity is parked (owner decision). The extra query is "water reactive windbreaker", labelled outside the 21. |

## Events that can move the readings

Taken from `project-files/seo/change-log.md` on `cowork/project-files-import` (read 18 Oct, about 19:15 UTC) and from the workstream ANSWERS files. Add new LIVE entries here before each run.

| When (UTC) | Event | Status | Panel queries it can affect | Relative to the runs |
|---|---|---|---|---|
| 16 Oct, about 15:40 | **C-001:** Outerwear collection created (`/collections/outerwear`, title "Water-Reactive & Heat-Reactive Jackets \| CROOKSLDN"). Double-Agent Puffa tagged heat-reactive. | LIVE | water reactive jacket, heat reactive puffer, water reactive clothing, heat reactive clothing, water reactive windbreaker | About 3h50 before the baseline |
| 16 Oct, about 15:42 | **C-002:** Tracksuits collection SEO title and copy | LIVE | heavyweight tracksuit UK | About 3h45 before |
| 16 Oct, 18:20–18:45 | **C-WS02-1:** "Made in Portugal" removed; customs origin set to China | LIVE | brand queries (answers about where the clothes are made) | About 45 min before |
| 16 Oct, about 19:00 | **C-006:** product-data batch 2: categories, colours, descriptions, Puffa images | LIVE | product queries, and Google Shopping packs | About 30 min before |
| 16 Oct, about 19:05 | **C-007:** Tracksuits lists the 3 Convict Sets; copy says 550gsm, 100% cotton | LIVE | heavyweight tracksuit UK, 550gsm hoodie UK, heavyweight hoodie UK | About 25 min before |
| 16 Oct, time unknown | Outside edit of `/collections/denim` (title, meta, copy, 5 products), and theme "SEO round 2" published | LIVE (seen by the project thread) | baggy jeans UK | Unknown whether before or after the baseline |
| 18 Oct, about 17:20 | **C-009:** stock tracking off on the 3 live tees | LIVE | none of the 21 directly | After both runs |
| 18 Oct, between about 17:20 and 18:50 | **T-shirt Week launch:** 14 new tees went ACTIVE. C-009 at about 17:20 still calls them drafts; product-data ANSWERS at 18:50 calls them live. | LIVE | Brand queries (Crooks LDN, Crooks London, Crooks LDN reviews). None of the 21 is a tee query. | After both runs |

## T-shirt Week window

- **What was decided:** owner decision #24 says T-shirt Week runs Monday to Sunday, but gives no exact dates.
- **Window used here:** **Sun 18 Oct (launch) to Sun 25 Oct 2026.** This is the launch day plus the Monday-to-Sunday week that follows. It is taken from the 18 Oct launch because no dates were given.
- **Before running inside the window:** if a run between 18 and 25 Oct includes the brand queries, confirm the dates with George first. A non-brand run inside the window is allowed, but its `meta.json` must say it ran during T-shirt Week.
- **When reading results:** treat brand-query results captured in that window as possibly affected by launch traffic and social activity.
- **Runs so far:**
  - The 16 Oct baseline was before the launch.
  - The 18 Oct gap-fill finished at 15:45 UTC, before the tees went live.
  - The 18 Oct extra-query baseline ran inside the window, but it is a non-brand reactive-outerwear query.
- **13 Nov:** the planned run is well outside the window.

## How to read the baseline against these events

- **All five changes went live before the baseline started.** C-001, C-002, C-WS02-1, C-006 and C-007 were live 25 minutes to 4 hours before the baseline began.
- **No crooksldn.com page appeared on any non-brand query in the baseline.** That includes the reactive queries C-001 targets and the tracksuit query C-002 and C-007 target. Treat the baseline as the before-reading for these changes. Whether Google or the AI engines had crawled them at capture is unknown.
- **The 13 Nov run is the first after-reading,** about 4 weeks after these changes. On the reactive, tracksuit and hoodie queries, change effects and natural drift can't be separated.
- **Use the untouched queries to measure drift.** In a core-8 run, the drift controls are "best UK streetwear brands" and "brands like Corteiz". These queries stop being controls once the Streetwear Directory or Disco listing goes live: log that date here. No logged change targets these:
  - brands like Corteiz
  - best UK streetwear brands
  - British streetwear brands
  - London streetwear brands
  - emerging UK streetwear brands
  - independent British streetwear
  - Corteiz alternatives
  - brands like Carsicko
  - brands like Broken Planet
