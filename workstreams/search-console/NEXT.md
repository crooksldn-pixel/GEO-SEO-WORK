# Next

## When George's answers arrive ("answered")

Read the `Answer:` lines in `QUESTIONS.md`, or the answers in the chat message. Then:
- **Q1:** put the Tesco tee redirect target in FINDINGS 5 and 8 and in `artifacts/opportunities.csv` row 3.
- **Q2:** if another property exists, export UK Queries, Pages and Dates for 23 Jul – 14 Oct into `artifacts/gsc-exports/` and rebuild the baseline in FINDINGS 1 around the weeks before 16 Oct.
- **Q3:** add the drop, launch and password dates to the measurement plan below, and leave those days out of like-for-like comparisons.
- **Q4:** if A, create the three scheduled checks (20 Oct, 24 Oct, 14 Nov); if B, wait for the main chat.

Update STATUS.md and commit.

## Do next

1. **From 20 Oct:** open Indexing > Pages. If processing has finished, record every "why pages aren't indexed" reason with page counts and example URLs in FINDINGS. Check that /password, /collections/frontpage, /collections/all and the archived 404s appear where FINDINGS 6–8 expect.
2. **Around 24 Oct (first 7-day post-deploy window, 16–22 Oct):** export UK Queries, Pages and Dates. Compare against the 15 Oct anchor and the Jan–Jul reference (`artifacts/gsc-exports/`). Report:
   - "crooks" position (reference 7.0; 6.1 on 15–16 Oct)
   - which URL Google shows for the joggers, jeans, jorts, tee and tesco clusters (query filter → Pages tab)
   - brand sitelinks (is /collections/frontpage still one?)
   - URL Inspection on /collections/outerwear and /blogs/news/convict-vs-cellblock-fit
   - reactive and other non-branded queries, especially "water reactive windbreaker"
3. Record any change another workstream deployed only against those measurements. Per the README evidence rule, a deploy alone is not evidence.
4. **Around 14 Nov:** 28-day read (16 Oct – 12 Nov), same breakdowns, and a fresh Core Web Vitals check.

Use the same method each time: country filter United Kingdom, search type Web, and the URL Inspection search bar on the Overview page. Never click "Request indexing" or anything on the Sitemaps page; run "Test live URL" only when a check needs it.

## Do not do yet

- Don't compare 16–22 Oct with Jan–Jul as if it were before/after. Jan–Jul is pre-relaunch, on different URLs. Use it only for query demand.
- Don't judge the joggers/jeans/jorts/tees internal-link work until it has been live for at least 7 days; the first read before then shows only crawl timing.
- Don't recommend new landing pages for shorts or other unmapped intents. Volumes are too small (151 impressions in six months) and the programme rule is one URL per intent, no new landing pages.

## Decisions still required

- George: is the Crooks Express tee the "Tesco tee" design? (Redirect target for /products/white-tesco-tshirt and /products/black-tesco-tshirt.)
- Collections workstream, with George's OK: task F (redirects plus `seo.hidden` on /collections/frontpage). Search Console evidence is in FINDINGS 6 and 8, including five more 404 URLs to add to its list.

## Data still required

- Indexing > Pages report (processing).
- Search Console data from 17 Oct onward.
- Fresh CrUX data.

## Recommended follow-up date

- 20 Oct 2026: Indexing > Pages.
- 24 Oct 2026: first 7-day post-deploy read.
- 14 Nov 2026: 28-day read.
