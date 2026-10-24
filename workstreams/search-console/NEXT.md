# Next

## Scheduled runs (set 18 Oct, approved in QUESTIONS.md Q4)

Each run is read-only and arrives in this session as a message, which carries its own instructions.

| When | What | Task ID |
|---|---|---|
| Tue 20 Oct 2026, 10:00 BST | Lock status; Indexing > Pages; URL Inspection on outerwear, the fit article, /collections/frontpage, a Tesco tee URL | trig_01M227b4MqkZodFUcy5FsfLk — **done** (arrived late; run 24 Oct) |
| Sat 24 Oct 2026, 10:00 BST | First read from 15 Oct onward, with lock and T-shirt Week days labelled | trig_01SKWya36CezmkwRzEUV7cPV — **done** 24 Oct (FINDINGS 13–15) |
| Sat 14 Nov 2026, 10:00 GMT | 28-day read, plus 4-week figures for each live change in the change log | trig_016HxR8hzBPAb4XgQhLtg2HK |

If this session no longer exists when a run is due, the next agent runs the same check by hand from this table.

## Measurement calendar (label these days in every read)

| Dates | What | How to treat it |
|---|---|---|
| 21 Jan – 22 Jul 2026 | Pre-relaunch reference | Query demand only; different site and URLs |
| 23 Jul – 14 Oct 2026 | No Search Console data | Can't be filled (George parked the other-property question) |
| 15 Oct | Only full pre-deploy day | Anchor |
| 16 Oct | Deploy day (C-001, C-002, C-006, C-007) | Anchor, labelled |
| 18 Oct ~18:15 BST – 19 Oct ~17:00 BST | Store password-locked (FINDINGS 13, timed from Crawl stats) | Lock days: leave 18 and 19 Oct out of like-for-like comparisons |
| 18 Oct 18:27 BST | 14 T-shirt Week tees published, 4 of them on previously archived URLs | Tee queries from here are launch demand |
| Mon 19 – Sun 25 Oct (presumed) | T-shirt Week (owner decision #24; the main chat says the tees went live 18 Oct) | Launch spike: report tee and brand queries separately, never as an SEO result |

The store reopened on 19 Oct, so the first clean 7-day window is **26 Oct – 1 Nov** (after T-shirt Week), readable around 3 Nov. That read isn't scheduled; it needs George's or the orchestrator's OK. Otherwise the 14 Nov read covers it.

## Do next

1. **14 Nov (scheduled):** export UK Queries, Pages and Dates for 16 Oct – 12 Nov, labelling 16 Oct (deploy), 18–19 Oct (lock) and 19–25 Oct (T-shirt Week). Compare the clean days from 26 Oct onward with the 15 Oct anchor and with 16–17 Oct. Report:
   - "crooks" position (Jan–Jul 7.0; 15–22 Oct 4.7–6.2 on open days)
   - which URL wins the joggers, jeans, jorts, tee and tesco clusters (query filter → Pages tab). On 15–22 Oct, "joggers" still clicked through to the homepage.
   - brand sitelinks (is /collections/frontpage gone?)
   - non-branded queries ("550gsm hoodie" → /collections/sweats, "water reactive windbreaker" → HydroCuff)
   - Indexing > Pages against the 16 Oct baseline (FINDINGS 14), and URL Inspection on /collections/outerwear and the fit article
   - 4-week Search Console figures for each live change in `project-files/seo/change-log.md` (branch `cowork/project-files-import`), each labelled with the window it comes from
2. **When collections reports its changes live:** check every approved redirect (both Tesco tee URLs → /products/crooks-express-t-shirt; large-duffle-bag, joggas-1 and the 2005-drop pink CRSDR URLs) and that /collections/frontpage is noindexed. Then run URL Inspection on each. Don't redirect 3-clives-tee, evil-clive-tee, og-crook-tee or broadcast-tee: they're live again.
3. **If George says yes** to requesting indexing: do it for /collections/outerwear and /blogs/news/convict-vs-cellblock-fit only, then log it in CHANGES.md.
4. Record any change another workstream deployed only against these measurements; per the README evidence rule, a deploy alone is not evidence.

Method each time: country United Kingdom, search type Web, and the URL Inspection bar on the Overview page, filled with form_input (typed text doesn't land; once a click focused the Sitemaps form instead). Never click "Request indexing" without George's go in chat, and nothing on the Sitemaps page. Run "Test live URL" only when a check needs it.

## Do not do yet

- If the store is password-locked again, run no URL Inspection live tests or redirect checks until it reopens, and label the lock days.
- No "Request indexing" until George says go in chat (STATUS, Waiting on George #1). The original brief ruled it out, and the 18 Oct owner decisions don't cover it.
- Don't compare any October window with Jan–Jul as a before/after. Jan–Jul is pre-relaunch, on different URLs; use it for query demand only.
- Don't judge the internal-link work until it has been live for at least 7 open days.
- Don't recommend new landing pages for shorts or other unmapped intents (151 impressions in six months; the programme rule is one URL per intent).

## Decisions still required

- George: may this workstream request indexing for /collections/outerwear and /blogs/news/convict-vs-cellblock-fit?

## Data still required

- Search Console data for a clean window (26 Oct onward).
- Fresh CrUX data.

## Recommended follow-up date

3 Nov 2026 for the clean 26 Oct – 1 Nov read (needs an OK to schedule). 14 Nov 2026, 10:00 GMT (scheduled).
