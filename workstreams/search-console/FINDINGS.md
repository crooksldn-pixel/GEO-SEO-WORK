# Findings

All figures are Google Search Console, property `sc-domain:crooksldn.com`, web search, United Kingdom, unless stated. Exports: `artifacts/gsc-exports/`. Full report: `artifacts/search-console-report.md`. Ranked actions: `artifacts/opportunities.csv`.

## Finding 1 — Search Console has no data for 23 Jul – 14 Oct 2026

**Finding:**
Performance data covers 21 Jan – 22 Jul 2026, then resumes on 15 Oct 2026. Nothing in between. Core Web Vitals, Shopping and Crawl stats also stop at 23 Jul. Indexing > Pages still says "Processing data" (checked 16 and 18 Oct).

**Evidence:**
Performance report, Days tab (`gsc_uk_16m_dates.csv`, `gsc_uk_28d_dates.csv`). Settings > About: "Property added to account 16 October 2026". The 3-month view lists only 17–22 Jul and 15–16 Oct.

**Why it matters:**
There's no pre-deploy baseline from the weeks before the 16 Oct changes. Jan–Jul is pre-relaunch reference data, and its page rows use the old site's URLs. Any before/after claim has to be anchored on 15 Oct (the only full pre-deploy day) and 16 Oct (deploy day).

**Confidence:** High.

**Recommended action:**
Treat 15–16 Oct as the anchor (UK: 86 clicks, 295 impressions, CTR 29.2%, avg position 4.6). First 7-day read 16–22 Oct, around 24 Oct. First 28-day read 16 Oct – 12 Nov, around 14 Nov.

## Finding 2 — Non-branded search is effectively zero

**Finding:**
In Jan–Jul, 74 genuinely non-branded queries produced 187 impressions and 1 click. Of 14,312 clicks, branded queries produced 12,303, anonymised queries 1,948, and everything else 61 (mostly brand misspellings). No non-branded query reached 50 impressions; the largest was "ldn joggers" (22 impressions, position 9.7). The first non-branded commercial query since the gap is "water reactive windbreaker": 4 impressions at position 3.0 on 15–16 Oct, landing on /products/hydrocuff-windbreaker.

**Evidence:**
`gsc_uk_16m_queries.csv`, `gsc_uk_28d_queries.csv`. Branded uses the programme definition (contains crooks, crooksldn, crooks ldn, crooks london, convict hoodie or cellblock); the finer split is in the report, section 2.

**Why it matters:**
None of the URL-map intents (550gsm/heavyweight hoodie, tracksuit, baggy jeans, reactive jacket, fit/size) has any Search Console history. Non-branded progress has to be measured from zero. The reactive jacket is the first commercial term to break through.

**Confidence:** High.

**Recommended action:**
Report non-branded and branded separately in every future read. Track "water reactive windbreaker" and other reactive terms from 16 Oct (shared with the geo-measurement panel).

## Finding 3 — One query, "crooks", caused most of the click decline

**Finding:**
Clicks fell 23% between 21 Jan – 21 Apr and 22 Apr – 22 Jul (8,092 → 6,220). The bare query "crooks" lost 1,076 clicks (1,573 → 497) while its position slid 5.4 → 8.7 on flat impressions (6,152 → 5,838). That's 60% of the 1,786-click drop in query-attributed clicks. "crooks" carries a third of all impressions (11,990). Brand+category terms also slipped: crooks clothing position 2.0 → 3.8, crooks streetwear 1.4 → 3.3.

**Evidence:**
`gsc_uk_compare_H1_vs_H2_queries.csv`. On 15–16 Oct, "crooks" was at position 6.1 (11 clicks, 114 impressions).

**Why it matters:**
"crooks" is ambiguous (Crooks & Castles and other "crooks" results compete). Recovering a few positions there is worth more clicks than any other single change in this data.

**Confidence:** High for the size of the drop. Low for its cause: Search Console doesn't show why.

**Recommended action:**
Entity work rather than schema, which is already live (Organization alternateName "Crooks London" and "Crooks", sameAs Instagram and TikTok — confirmed in the 16 Oct live test). Show "CROOKSLDN (Crooks LDN)" near the top of the homepage (H1 is only "CROOKSLDN"), and make sure the Instagram and TikTok bios link to crooksldn.com. Suggested owner: entity-about. Track "crooks" position weekly from 16 Oct.

## Finding 4 — Brand+product searches land on the homepage, not the mapped collection

**Finding:**
For every product cluster, Google showed the homepage, not the mapped collection or product page:

| Cluster | Impressions to `/` | Impressions to the product/collection page | Mapped URL |
|---|---|---|---|
| joggers | 1,560 | 40 (black-joggers PDP) | /collections/sweats |
| jeans | 423 | 17 (OG Jeans) | /collections/denim |
| jorts | 278 | 32 (old jorts PDP) | /collections/denim |
| shirt | 321 | 11 (Crooks Express) | /collections/tees |
| tesco | 239 | 18 (Crooks Express) | see Finding 5 |
| shorts | 158 | 8 | unmapped |

The PDPs that ranked had low CTR (1–5%) because they appeared under the homepage for navigational searches ("crooks ldn", "crooksldn"), not because their snippets are weak.

**Evidence:**
`gsc_uk_16m_query_page_breakdowns.csv` (query filter → pages, and page filter → queries).

**Why it matters:**
This is the only cannibalisation pattern in the data. A searcher who types "crooks joggers" lands on the homepage and has to find joggers. Collection landing pages convert better, and they are what the one-URL-per-intent map targets.

**Confidence:** Medium (pre-relaunch URLs; the mapped collections have no history yet).

**Recommended action:**
Internal links using the searched word as anchor text ("joggers", "jeans", "jorts", "T-shirts") from the homepage and nav to the mapped collection, plus the word in each collection's H1 or intro. No new pages. Suggested owner: collections. Ranked list in `artifacts/opportunities.csv`, rows 2 and 5–9.

## Finding 5 — "Tesco tee" demand is rising and both old Tesco tee URLs are 404

**Finding:**
crooks tesco shirt / tee / tesco: 238 impressions at position 3.8–4.3, rising from 52 to 186 impressions half on half. /products/white-tesco-tshirt and /products/black-tesco-tshirt both return 404.

**Evidence:**
`gsc_uk_compare_H1_vs_H2_queries.csv`; `curl` status checks on 16 and 18 Oct.

**Why it matters:**
Real, growing demand for a product people still remember, with no live page to receive it.

**Confidence:** High. George confirmed on 18 Oct that the "Tesco tee" is the Crooks Express tee (owner decision #21).

**Recommended action:**
301 both URLs to /products/crooks-express-t-shirt (approved, owner decision #21). Don't use "Tesco" in titles. Owner: collections (redirects). This workstream checks the redirects and the "tesco" queries' landing page once the store is unlocked (Finding 13).

## Finding 6 — Thin system listings now show as brand sitelinks

**Finding:**
Since 15 Oct, brand searches show sitelinks under the homepage: /collections (90 impressions), /collections/frontpage (76, title "PRODUCTS | CROOKSLDN"), /collections/tracksuits (75), /pages/contact (62), /collections/all (51), /collections/tees-1 (21), /collections/tees (17), /search (4), /cart (2). /collections/frontpage and /collections/all are indexed and self-canonical. /collections/tees-1 is indexed from a 14 Oct crawl but now 301s to /collections/tees. /search and /cart are `noindex`.

**Evidence:**
`gsc_uk_28d_pages.csv`, `query=crooksldn` page breakdown on 18 Oct, URL Inspection (frontpage, all, tees-1), live fetch of /search and /cart.

**Why it matters:**
Sitelinks are what every brand searcher sees. A "PRODUCTS" link to a duplicate listing takes a slot a real collection could fill.

**Confidence:** Medium (two days of data).

**Update 24 Oct:** /collections/frontpage is still indexed (URL Inspection) and still a brand sitelink, on 30–127 impressions a day (Finding 15). It has no robots meta and is still in the sitemap, so the approved `seo.hidden` hasn't been applied yet.

**Recommended action:**
Noindex /collections/frontpage, or unpublish it and 301 it to /collections/new. Leave /collections/all. tees-1, /search and /cart will drop out on recrawl. Give /collections a meta description; it has none. Suggested owner: collections.

## Finding 7 — The fit article is invisible to Google

**Finding:**
/blogs/news/convict-vs-cellblock-fit returns 200 and is self-canonical, but on 18 Oct it is still missing from sitemap_blogs_1.xml, which lists only /blogs/news, and URL Inspection says "URL is unknown to Google". /collections/outerwear, by contrast, has been added to the sitemap and is now "Discovered – currently not indexed".

**Evidence:**
Live sitemap fetch (16 and 18 Oct), Sitemaps report (39 discovered pages, up from 38), URL Inspection on 16 and 18 Oct.

The article is published (collections audit: 16 Oct 13:10 UTC), has no robots meta, and is linked from /blogs/news and the blog's Atom feed. So Google will find it when it next crawls /blogs/news. It just isn't in the sitemap yet.

**Update 24 Oct:** the article now sits in a new `sitemap_articles_1.xml`, and Google read the sitemap index on 23 Oct (54 pages discovered, up from 39). URL Inspection on 24 Oct still says "URL is unknown to Google", which should change at the next crawl. /collections/outerwear is still "Discovered – currently not indexed".

**Why it matters:**
The article is the mapped URL for fit and size intent, and today the only way in is a page Google rarely visits (/blogs/news had 2 impressions in six months).

**Confidence:** High.

**Recommended action:**
Link it from pages Google already crawls: /collections/sweats, /collections/tracksuits and the hoodie and crewneck size guides. Collections tasks A and C already plan the Sweats and Tracksuits links, so this adds urgency rather than new work. Suggested owner: collections.

## Finding 8 — Which 404s had search impressions (evidence for collections task F)

**Finding:**
The five archived products are those in the `cowork/collections` Admin API audit: og-crook-tee, 3-clives-tee, broadcast-tee, evil-clive-tee and large-duffle-bag. **Two of the five had UK impressions in Jan–Jul:** /products/3-clives-tee (31, plus 17 on `?utm_source=shop_app`; Google's last crawl on 10 Sep got a 5xx) and /products/evil-clive-tee (20, plus 3 on parameter URLs). og-crook-tee, broadcast-tee and large-duffle-bag had none.

Five more 404s had impressions or Googlebot hits but **aren't on the collections redirect list**:

| URL | Live | Search Console evidence | Suggested target |
|---|---|---|---|
| /products/white-tesco-tshirt | 404 | 7 impressions, 1 click; 238 impressions of "tesco" queries (Finding 5) | /products/crooks-express-t-shirt (approved) |
| /products/black-tesco-tshirt | 404 | 9 impressions | /products/crooks-express-t-shirt (approved) |
| /products/joggas-1 | 404 | Googlebot got 404 on 19 and 23 Jul | /collections/sweats |
| /collections/2005-drop/products/pink-crsdr-joggas | 404 | 7 impressions | /products/pink-crsdr-joggers (200) |
| /collections/2005-drop/products/pink-crsdr-hoody | 404 | 1 impression | /products/pink-crsdr-hoodie (200) |

(An earlier version of this finding offered a hint about which wash CB2 was. It's withdrawn: George decided on 18 Oct that CB1/CB2 were placeholder names, so nothing should be derived from them; owner decision #27.)

**Evidence:**
`gsc_uk_16m_pages.csv`, `gsc_uk_16m_query_page_breakdowns.csv`, Crawl stats 404 drill-down, URL Inspection, `curl` on 16 and 18 Oct. Archived list: `cowork/collections` → `workstreams/collections/artifacts/index-hygiene-audit.md`.

**Why it matters:**
It gives collections task F its go-ahead evidence. The Tesco pair carries real, growing demand; the rest are small but are lost visits and crawl noise.

**Update 24 Oct:** T-shirt Week republished four of the five archived tees on 18 Oct at 18:27: /products/3-clives-tee, evil-clive-tee, og-crook-tee and broadcast-tee now return 200. They need no redirect, and old impressions can come back to them. Still 404 on 24 Oct: large-duffle-bag, both Tesco tee URLs (approved redirect not made yet), joggas-1 and the two 2005-drop pink CRSDR URLs. The Index report (Finding 14) adds low-value 404s last crawled in August: double-agent-balaclava, untitled-nov28_15-42, poster-v2, clive-s-cash-sticker-pack and /collections/all/products/joggas-1. These are optional redirects.

**Confidence:** High.

**Recommended action:**
Go ahead with collections F: redirect the five archived URLs, and add the five URLs above to the list (approved as "other legacy redirects as proposed", owner decision #21). Owner: collections (redirects).

## Finding 9 — Structured data: GBP confirmed, but currency URLs leak other currencies and shipping is overstated

**Finding:**
URL Inspection "Test live URL" on /products/convict-hoodie-1 (16 Oct, 21:15) rendered Offer `priceCurrency GBP`, price 60.00, on all 5 variants; Merchant listings 5 valid. But:
- Google has discovered `/products/convict-hoodie-1?variant=…&country=CZ&currency=CZK`. That URL returns 200, canonicalises to the base product, and its JSON-LD says `priceCurrency CZK`.
- Organization `shippingDetails` gives `shippingRate 0.00 GBP` with no order threshold, while store policy is free UK shipping over £30.

The indexed copy (crawled 7 Oct) still shows 5 invalid merchant items ("Missing field 'image'"); the live page passes, so that clears on recrawl.

**Evidence:**
URL Inspection (indexed and live test), raw fetch of the CZK URL (`Shopify.currency` active CZK).

**Why it matters:**
Wrong-currency prices and an overstated free-shipping claim can cause merchant listing mismatches with Merchant Center, and a misleading price snippet.

**Confidence:** High for what renders. Medium for how much it hurts.

**Recommended action:**
Output JSON-LD prices in the base currency (GBP) whatever `cart.currency` is, or disallow `/*?*currency=` in robots.txt.liquid. Make `shippingDetails` match the real rate below £30, or remove it. Suggested owner: theme; tell merchant-center.

## Finding 10 — /products/og-jeans returned 404 to Googlebot on 19–23 Jul

**Finding:**
Crawl stats list /products/og-jeans and its variant URL as 404 on 19, 20, 21, 22 and 23 Jul. It returns 200 now. Over the same period jeans queries fell (crooks jeans impressions 189 → 63, position 1.7 → 3.2 half on half).

**Evidence:**
Settings > Crawl stats > Not found (404) drill-down.

**Why it matters:**
It probably explains part of the jeans decline, and jeans is a mapped intent (baggy jeans → /collections/denim and /products/og-jeans).

**Confidence:** Medium.

**Recommended action:**
None now. Recheck og-jeans indexing in the first post-deploy read.

## Finding 11 — Search Console's Core Web Vitals report is stale; use live-site-checks instead

**Finding:**
Search Console shows mobile and desktop at 8 good URLs, 0 needing improvement, 0 poor, with "No issues detected in the last 90 days". But its CrUX data stops at 23 Jul, before the relaunch. The `cowork/live-site-checks` workstream measured current field data through PageSpeed Insights on 16 Oct and found the homepage failing Core Web Vitals on mobile (INP), with the Mida script as the heaviest load on every page (its Finding 4). HTTPS: 8 URLs, all HTTPS.

**Evidence:**
Search Console Core Web Vitals and HTTPS reports (last update 23 Jul). `cowork/live-site-checks` → `workstreams/live-site-checks/FINDINGS.md`, Finding 4.

**Why it matters:**
Search Console's "all good" is out of date and shouldn't be quoted as current.

**Confidence:** High that the Search Console report is stale.

**Recommended action:**
Use live-site-checks for current Core Web Vitals. Recheck Search Console once it shows CrUX data after 16 Oct.

## Finding 12 — Overlaps with other workstreams

**Finding:**
As of 18 Oct 16:50 BST:
- **collections** lists this workstream's report as its Blocker 3 (it couldn't reach `/mnt/project-files/seo/cowork-results/05-search-console.md`). The same report is now on this branch at `artifacts/search-console-report.md`. Findings 5, 6, 7 and 8 are the evidence its task F needs. It already plans `seo.hidden` on /collections/frontpage, which matches Finding 6.
- **live-site-checks** Finding 6: the held "Claude P1 fixes" theme changes `snippets/crooks-schema-site.liquid` (Organization). The homepage entity work in Finding 3 and the `shippingDetails` / currency fix in Finding 9 touch the same structured data, so they should go through whichever theme route that workstream settles on, not as a separate edit. Its Finding 3 (delivery days 1–2 vs 2–3) is a separate problem from Finding 9 here (free shipping shown with no £30 threshold); both are in the same `shippingDetails` block.
- **product-data** owns product records. Finding 10 here (OG Jeans 404 to Googlebot in July) sits alongside its Finding 2 (OG Jeans missing 14oz). No conflict.
- **geo-measurement** runs the UK GEO panel. "water reactive windbreaker" (Finding 2) is Search Console's first view of a query family that panel already tracks.

**Evidence:**
STATUS and FINDINGS files on `cowork/collections`, `cowork/live-site-checks`, `cowork/product-data` and `cowork/geo-measurement`, read 18 Oct.

**Why it matters:**
It avoids two sessions editing the same theme snippet, and it unblocks collections F.

**Confidence:** High.

**Recommended action:**
The orchestrator routes Findings 3 and 9 to the theme route in live-site-checks' NEXT.md, and Findings 5–8 to collections.

## Finding 13 — The store was password-locked for about 23 hours, 18–19 Oct

**Finding:**
Shopify password protection locked the whole store from about 18:15 BST on Sun 18 Oct to about 17:00 BST on Mon 19 Oct. While locked, every URL returned 302 → /password, Googlebot included, and `/sitemap.xml` returned 404. On 24 Oct at 10:01 BST the store was open: pages return 200 and the sitemap is back.

How the window was fixed:
- Search Console Crawl stats: Googlebot's last normal page fetch before the lock was 18 Oct 18:12; its 302s cluster from 18 Oct 18:00–18:59 through 19 Oct 16:00–16:59; it fetched /password itself on 19 Oct at 03:35 and 04:20; its first normal page fetch after was 19 Oct 18:12 (/products/pink-set).
- `curl`: open at 16:30–17:05 BST on 18 Oct, locked at 20:09 and 20:11 BST, open on 24 Oct 10:01 BST.
- `cowork/theme-editor` FINDINGS 9: Admin API `passwordProtection.enabled = true` at 20:14 BST on 18 Oct.
- Crawl stats times are taken as UK time; they fit the curl and Admin API readings.

The lock overlapped the T-shirt Week launch: 14 tees were published at 18:27 BST on 18 Oct. 19 Oct had the most clicks of the week (155), most of them while the store was locked.

**Evidence:**
Crawl stats (OK 200 and Moved temporarily 302 drill-downs, read 24 Oct), `curl` on 18 and 24 Oct, the theme-editor branch, `artifacts/gsc-exports/gsc_uk_2026-10-15_to_22_dates.csv`.

**Why it matters:**
Search Console credits a click to the URL shown in results, not to where the shopper landed, so the lock doesn't show in Performance data: 19 Oct looks like a good day even though most clicks hit a password page. Treat 18 Oct (evening) and 19 Oct (until ~17:00) as lock days in every comparison. A lock of under a day is unlikely to have cost indexing.

**Confidence:** High for the window, to within about an hour at each end. Not known whether the lock was deliberate; nobody recorded it.

**Recommended action:**
Label 18–19 Oct as lock days in every review (already done in the exports), and have programme-records log the reopen time. If future drops use a lock, record it in the change log beforehand, with times, so measurement can leave it out.

## Finding 14 — Index baseline (Indexing > Pages, report dated 16 Oct): 43 pages indexed, 800 not indexed

**Finding:**
The report finished processing between 18 and 24 Oct. Its snapshot is dated 16 Oct, so it predates the lock and T-shirt Week.

| Reason | Pages | What they are |
|---|---|---|
| Excluded by 'noindex' tag | 328 | 314 set-product variant URLs with `?variant&country&currency` (set pages are noindexed by design), customer login URLs, /collections/sets |
| Alternative page with proper canonical tag | 322 | 286 product URLs with `?country&currency&variant`, 22 `?variant`, 14 search-tracking `?_pos&_sid&_ss` |
| Blocked by robots.txt | 78 | Shop login (`/services/login_with_shop/authorize`), customer account pages on friendsof.crooksldn.com, cart endpoints |
| Page with redirect | 24 | http:// and www. hosts, /password, old cb1/cb2 handles, the hyrdocuff typo handle |
| Not found (404) | 22 | large-duffle-bag, evil-clive-tee and 3-clives-tee (both live again since 18 Oct), joggas-1, double-agent-balaclava, untitled-nov28_15-42, poster-v2, clive-s-cash-sticker-pack, some old variant URLs |
| Server error (5xx) | 1 | /products/3-clives-tee (crawled 10 Sep; live again since 18 Oct) |
| Crawled – currently not indexed | 25 | Theme JS files, set variant URLs, collection .atom feeds, /agents.md |

Indexed (43): the homepage, 9 store pages and policies, /collections, /search and /cart, 10 collections (including frontpage, all, and the 301'd denim-1, sweats-1, tees-1), and 21 products (including black-set, which is now noindexed).

**Evidence:**
`artifacts/gsc-exports/gsc_index_reasons_2026-10-16_snapshot.csv`, `artifacts/gsc-exports/gsc_indexed_pages_2026-10-16_snapshot.csv`.

**Why it matters:**
- **639 of the 800** are parameter copies of product pages; 600 of those are Shopify Markets `?country&currency&variant` URLs. They aren't indexed, so they do no ranking harm, but they take crawl. They're also the same kind of URL that outputs a non-GBP price (Finding 9).
- Nothing important is blocked or erroring. The real gaps are /collections/outerwear and the fit article (not indexed yet, Finding 7) and the stale entries (/cart, /search, the three -1 collections, black-set), which will drop on recrawl.
- /collections/frontpage and /collections/all are indexed (Finding 6).

**Confidence:** High.

**Recommended action:**
No action on noindex, canonical or robots: they're working as designed. The currency-URL fix in Finding 9 (theme) also reduces this crawl. Re-read the report on 14 Nov.

## Finding 15 — First week after the gap (15–22 Oct): no clean SEO read yet

**Finding:**
UK, web, 15–22 Oct: 650 clicks, 1,520 impressions, CTR 42.8%, average position 3.6. Day labels:

| Day | Clicks | Impr | Pos | Label |
|---|---|---|---|---|
| 15 Oct | 37 | 152 | 5.2 | anchor (only full pre-deploy day) |
| 16 Oct | 49 | 143 | 4.1 | deploy day |
| 17 Oct | 48 | 130 | 4.2 | open, post-deploy |
| 18 Oct | 52 | 176 | 4.6 | tees launched 18:27; locked from ~18:15 |
| 19 Oct | 155 | 275 | 3.1 | locked until ~17:00; T-shirt Week |
| 20–22 Oct | 94–111/day | 198–224 | 2.8–3.1 | T-shirt Week |

Only 16–17 Oct are clean post-deploy days: two days against a one-day anchor. That isn't evidence of anything.

What can be recorded:
- **"crooks"**: position 4.7–6.2 on open days (Jan–Jul average 7.0; Apr–Jul 8.7). It falls in launch week, so it isn't attributable.
- **Product clusters still land on the homepage.** For "joggers" queries, Google now shows a block of site links (tracksuits 45 impr, /collections 43, frontpage 26, black-joggers 22, sweats 19, v2-baggies 19, all at position 1.0), but all 25 clicks went to the homepage. Jeans, jorts and tees had too little volume to read.
- **"tesco" queries had zero impressions** this week (238 in Jan–Jul).
- **Non-branded:** "550gsm hoodie" got 1 click at position 3.0 on **/collections/sweats**, the first non-branded click on record to a mapped collection. "water reactive windbreaker" had 7 impressions at 4.9 on the HydroCuff page. Smaller: lfn jeans (3), prisoner grey tracksuit (2), prison sweatpants, dark blue washed jorts, grey jorts. Genuinely non-branded commercial total: 1 click, 17 impressions in 8 days, against 187 impressions in 183 days in Jan–Jul.
- **Brand sitelinks:** /collections/frontpage still shows on 30–127 impressions a day; it hasn't been hidden yet (Finding 6).
- Two Merchant Center free-listing URLs (`utm_content=sag_organic`) now appear in web results for black-joggers and v2-baggies.

**Evidence:**
`artifacts/gsc-exports/gsc_uk_2026-10-15_to_22_*.csv` (queries, pages, dates, query-crooks, page-frontpage, query_page_breakdowns).

**Why it matters:**
It sets the record for the first post-deploy week and shows why it can't be used as a before/after. The non-branded signals are tiny but point at the right URLs (sweats for 550gsm, HydroCuff for water-reactive).

**Confidence:** High for the figures. None of it is evidence of an SEO change.

**Recommended action:**
The first clean 7-day window is 26 Oct – 1 Nov (after T-shirt Week), readable around 3 Nov. The 14 Nov scheduled read covers 16 Oct – 12 Nov with lock and launch days labelled.
