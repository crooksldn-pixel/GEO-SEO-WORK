# Next

## Scheduled runs (set 18 Oct, approved in QUESTIONS.md Q4)

Each run is read-only and arrives in this session as a message, which carries its own instructions.

| When | What | Task ID |
|---|---|---|
| Tue 20 Oct 2026, 10:00 BST | Lock status; Indexing > Pages; URL Inspection on outerwear, the fit article, /collections/frontpage, a Tesco tee URL | trig_01M227b4MqkZodFUcy5FsfLk |
| Sat 24 Oct 2026, 10:00 BST | First read from 15 Oct onward, with lock and T-shirt Week days labelled | trig_01SKWya36CezmkwRzEUV7cPV |
| Sat 14 Nov 2026, 10:00 GMT | 28-day read, plus 4-week figures for each live change in the change log | trig_016HxR8hzBPAb4XgQhLtg2HK |

If this session no longer exists when a run is due, the next agent runs the same check by hand from this table.

## Measurement calendar (label these days in every read)

| Dates | What | How to treat it |
|---|---|---|
| 21 Jan – 22 Jul 2026 | Pre-relaunch reference | Query demand only; different site and URLs |
| 23 Jul – 14 Oct 2026 | No Search Console data | Can't be filled (George parked the other-property question) |
| 15 Oct | Only full pre-deploy day | Anchor |
| 16 Oct | Deploy day (C-001, C-002, C-006, C-007) | Anchor, labelled |
| 18 Oct, from ~17:05 BST | Store password-locked (FINDINGS 13) | Leave out until reopening; record the reopen date |
| Mon 19 – Sun 25 Oct (presumed) | T-shirt Week (owner decision #24; the main chat says the tees went live 18 Oct) | Launch spike: report tee and brand queries separately, never as an SEO result |

The first clean 7-day window starts the day after the store reopens and T-shirt Week ends. If both end by 25 Oct, that's 26 Oct – 1 Nov, readable around 3 Nov.

## Do next

1. **20 Oct (scheduled):** as in the table. If Indexing > Pages has finished processing, record every "why pages aren't indexed" reason with page counts and example URLs, and check /password, /collections/frontpage, /collections/all and the archived 404s.
2. **24 Oct (scheduled):** export UK Queries, Pages and Dates from 15 Oct. Report:
   - "crooks" position (reference 7.0; 6.1 on 15–16 Oct)
   - which URL wins the joggers, jeans, jorts, tee and tesco clusters (query filter → Pages tab)
   - brand sitelinks (is /collections/frontpage gone?)
   - non-branded queries, especially "water reactive windbreaker"
   - URL Inspection on /collections/outerwear and the fit article
3. **Once the store reopens and collections has made its changes:** check every approved redirect on the live site (both Tesco tee URLs → /products/crooks-express-t-shirt; the archived and other 404s per FINDINGS 8) and that /collections/frontpage is noindexed. Then run URL Inspection on each.
4. **14 Nov (scheduled):** 28-day read with the same breakdowns, Indexing > Pages, fresh Core Web Vitals, and 4-week figures for each live change in `project-files/seo/change-log.md` (branch `cowork/project-files-import`), each labelled with the window it comes from.
5. Record any change another workstream deployed only against these measurements; per the README evidence rule, a deploy alone is not evidence.

Method each time: country United Kingdom, search type Web, and the URL Inspection bar on the Overview page, filled with form_input (typed text doesn't land; once a click focused the Sitemaps form instead). Never click "Request indexing" without George's go in chat, and nothing on the Sitemaps page. Run "Test live URL" only when a check needs it.

## Do not do yet

- No URL Inspection live tests or redirect checks while the store is locked: everything returns the password page.
- No "Request indexing", even after reopening, until George says go in chat (STATUS, Waiting on George #2). The original brief ruled it out, and the 18 Oct owner decisions don't cover it.
- Don't compare any October window with Jan–Jul as a before/after. Jan–Jul is pre-relaunch, on different URLs; use it for query demand only.
- Don't judge the internal-link work until it has been live for at least 7 open days.
- Don't recommend new landing pages for shorts or other unmapped intents (151 impressions in six months; the programme rule is one URL per intent).

## Decisions still required

- George: is the password lock intentional, and when does the store reopen?
- George: after reopening, may this workstream request indexing for /collections/outerwear and /blogs/news/convict-vs-cellblock-fit?

## Data still required

- The store's reopening date and time.
- Indexing > Pages report (processing).
- Search Console data from 17 Oct onward.
- Fresh CrUX data.

## Recommended follow-up date

20 Oct 2026, 10:00 BST (scheduled). Then 24 Oct and 14 Nov (scheduled), and the first clean 7-day window once the store reopens and T-shirt Week ends.
