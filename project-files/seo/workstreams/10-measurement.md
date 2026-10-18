<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 10 · GEO/SEO measurement and monitoring

Owner: workstream 10 thread. Read-only on the store. Last updated 16 Oct 2026.

## Current state

- **No query-level evidence exists yet.** There is no Search Console connection, no rank tracker, and the GEO query table in `seo/geo-query-set.md` is empty.
- **The GEO 43 → 50 → 54 and SEO health 70 → 74 scores have no recorded method.** Treat them as non-comparable audit scores, not as evidence of visibility change. Do not cite them as improvement.
- **What can be measured from the cloud (tested 16 Oct):** Shopify analytics (sessions, orders, sales by referrer and landing page) works. Google, Bing, DuckDuckGo, ChatGPT, Perplexity, OpenAI and SerpAPI are all unreachable from the cloud container (connection refused by the network policy). The built-in web search returns US results. Only `*.googleapis.com` is reachable, so a Search Console API or BigQuery route is technically possible once authorised.
- **The user's Mac (UK) is linked to the project**, so UK-located checks can be run there, either manually or by Claude driving the browser with the user's permission.

## Baseline · 16 Oct 2026 (source: Shopify analytics, ShopifyQL, last 90 days unless stated)

### Traffic by referrer (sessions, 90d)
| Source | Sessions | Conv. rate |
|---|---|---|
| Direct | 12,280 | 1.6% |
| Google organic | 3,799 | 2.1% |
| Instagram | 2,617 | 1.5% |
| Base44 (referrer) | 320 | 1.9% |
| Facebook | 222 | 0% |
| TikTok | 119 | 0% |
| Bing | 99 | 4.0% |
| ChatGPT | 2 | 0% |
| Total | 19,627 | |

### Orders by referrer (90d)
| Source | Orders | Net sales |
|---|---|---|
| No referrer recorded | [n] | £[redacted] |
| Google organic | [n] | £[redacted] |
| crooksldn (self) | [n] | £[redacted] |
| Base44 | [n] | £[redacted] |
| Instagram (both rows) | [n] | £[redacted] |
| Bing | [n] | £[redacted] |
| DuckDuckGo | [n] | £[redacted] |

### Organic search: where it lands (90d, 3,910 search sessions)
- Homepage `/`: 3,631 sessions (92.9%). This is overwhelmingly branded traffic (people searching "crooks ldn" and clicking the homepage). Inferred, not query-verified: Search Console is needed to confirm.
- `/password`: 36. Everything else: **243 sessions (6.2%)**, the best available proxy for non-branded / product-intent discovery.
- Top deep landings: /collections (74), /collections/tracksuits (22), /products/hydrocuff-windbreaker (13), /collections/frontpage (13), /products/black-joggers (13), /collections/all (12), /pages/contact (11), /products/cb2-wash-jorts (10), /collections/tees (9), /products/blue-wash-yard-jeans (8), /products/v2-baggies (8), /collections/sweats (6), /collections/new (6), /collections/denim (3). /collections/outerwear: 0.

### Organic search over time
Weekly search sessions (w/c): 20 Jul 80 · 27 Jul 239 · 3 Aug 175 · 10 Aug 190 · 17 Aug 197 · 24 Aug 198 · 31 Aug 522 · 7 Sep 440 · 14 Sep 459 · 21 Sep 319 · 28 Sep 388 · 5 Oct 362 · 12 Oct 179 (partial week).

Monthly organic-search orders / net sales: [redacted for the public repo; the Project copy has them].

Organic volume tracks drops and Instagram activity (spikes 31 Aug onwards), which is consistent with branded demand driving search, not rankings. Apr–Jun "deep" landings were mostly /password (840 sessions, store locked pre-drop), so there was no lost-rankings event; don't misread that period.

### AI assistant referrals (365d)
ChatGPT 2 sessions (/ and /collections), Perplexity 1 (/password). Effectively zero. Note that many AI-assistant clicks arrive with no referrer and land in "direct", so this undercounts, but it is the only hard number available.

### GEO query panel
Not yet measured. No UK-located result has been captured for any of the 21 queries. Status: **no baseline**.

## Measurement method

| # | Signal | Source | Who runs it | Cadence | Status |
|---|---|---|---|---|---|
| M1 | Organic + AI-referrer sessions, orders, sales; deep-landing share; per-collection organic sessions | Shopify analytics | Claude, automated | Weekly (Mondays) | Baseline recorded; routine set up |
| M2 | Query-level impressions, clicks, position, CTR (branded vs non-branded split), pages ranking for each target query | Google Search Console | Needs user access (see below) | Monthly full pull; weekly for pages changed in the change log | **Blocked: no access** |
| M3 | Google UK SERP for the 21-query panel: Crooks present?, position, URL, competitors, AI Overview citation | UK device, logged out / incognito, google.co.uk | User or Claude on the user's Mac | Monthly full panel | Not started |
| M4 | ChatGPT, Gemini, Perplexity answers for the panel: mentioned?, position in list, sources cited, sentiment, product | UK device, fresh chat, memory off, logged out where possible | User or Claude on the user's Mac | Monthly full panel; 8-query core fortnightly | Not started |
| M5 | Shopping / free listings visibility | Merchant Center performance report | Workstream 3 | Monthly | Owned by workstream 3 |

### M3/M4 protocol (so results are comparable month to month)
1. UK location, private/incognito window, signed out of Google. For ChatGPT/Gemini use a fresh chat with memory/personalisation off; Perplexity signed out.
2. Type the query exactly as listed in `geo-query-set.md`. No follow-up prompts.
3. Google: record organic position of the first crooksldn.com URL (top 20), whether an AI Overview appears and whether it cites Crooks, and the first five brands/domains shown.
4. Assistants: record whether Crooks is named, its position in any list, the brands named, the sources/links cited, tone, and any product named.
5. Screenshot each result into `seo/measurements/YYYY-MM-DD/` and add one row per query per surface to the table in `geo-query-set.md`.
6. AI answers vary between runs. Run each assistant query **3 times** and record mentions as x/3. A change only counts if it holds across two consecutive monthly panels.

8-query core (fortnightly): Crooks LDN · 550gsm hoodie UK · heavyweight hoodie UK · baggy jeans UK · best UK streetwear brands · brands like Corteiz · water reactive jacket · heat reactive puffer.

## Proposed tasks (ranked)

| Rank | Priority | Action | Impact | Evidence | Effort | Confidence | Recommended action |
|---|---|---|---|---|---|---|---|
| 1 | P1 | Get Search Console data into the project | Without it no SEO change in the queue can be validated, and branded vs non-branded cannot be separated | GSC is the only source of query/position data; none exists in Drive or the project | Low for user (export or grant), medium for API/BigQuery | High | User exports GSC Performance (Queries and Pages tabs, last 16 months, country = UK) to the project now; longer term enable GSC bulk export to BigQuery so Claude can pull it on a schedule |
| 2 | P1 | Run the first M3/M4 GEO panel | Establishes the only real GEO baseline; every GEO claim depends on it | Panel table empty; cloud can't reach Google UK or assistants | ~90 min manual, or Claude on the Mac with permission | High | Run before any GEO-targeted change ships, so the change log has a true "before" |
| 3 | P2 | Weekly Shopify snapshot (M1) | Catches organic revenue and deep-landing movement after each deploy | Working today | Done | High | Routine created 16 Oct, appends to `seo/measurements/shopify-weekly.md` |
| 4 | P2 | Tag change-log entries with their M1/M2 metric and a review date | Stops "deployed = improved" claims | Change log C-001 already names its metric | Low | High | Each entry gets a 4-week and 8-week review row |
| 5 | P3 | Server-side AI-crawler and AI-referrer logging | Would show whether GPTBot/PerplexityBot fetch the site | Shopify does not expose raw logs | High | Low | Not worth it now; revisit only if a CDN/log route appears |
| 6 | P4 | Re-running the unnamed GEO/SEO "score" audits | None; method unknown | Scores not reproducible | Low | n/a | Stop using them as KPIs |

## Primary KPIs (what should move, in order of commercial weight)
1. Organic-search net sales and orders per month (M1).
2. Non-homepage organic landing sessions (M1 proxy now; M2 non-branded clicks once available). Baseline: 243 sessions / 90d, 6.2% of organic.
3. Organic sessions to /collections/sweats, /denim, /tees, /outerwear (M1). Baseline 90d: 6 / 3 / 9 / 0.
4. GSC non-branded impressions and average position for the product/category queries (M2). Baseline: none.
5. GEO panel mention rate by group (M4), and Google UK presence (M3). Baseline: none.
6. AI-assistant referral sessions (M1). Baseline: 3 in 365 days.

## Dependencies
- M2 needs the user (GSC owner) to export or grant access.
- M3/M4 need a UK device; the user's Mac is linked to the project.
- Workstream 4 (Search Console analysis) consumes M2 data; workstream 3 owns M5.

## Status
- Baseline M1: recorded 16 Oct 2026.
- Weekly M1 routine: scheduled Mondays 08:52 London (first run 19 Oct 2026), writes seo/measurements/shopify-weekly.md.
- M2: waiting on the user's Search Console export.
- M3/M4: user chose (16 Oct) a dedicated Claude session on their Mac to run the panel repeatably. Runbook, query list and results format: seo/measurements/geo-panel/RUNBOOK.md and queries.csv. Session requested 16 Oct, waiting on the user to allow it.
