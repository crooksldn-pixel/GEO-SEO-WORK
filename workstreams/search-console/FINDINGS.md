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

**Recommended action:**
Noindex /collections/frontpage, or unpublish it and 301 it to /collections/new. Leave /collections/all. tees-1, /search and /cart will drop out on recrawl. Give /collections a meta description; it has none. Suggested owner: collections.

## Finding 7 — The fit article is invisible to Google

**Finding:**
/blogs/news/convict-vs-cellblock-fit returns 200 and is self-canonical, but on 18 Oct it is still missing from sitemap_blogs_1.xml, which lists only /blogs/news, and URL Inspection says "URL is unknown to Google". /collections/outerwear, by contrast, has been added to the sitemap and is now "Discovered – currently not indexed".

**Evidence:**
Live sitemap fetch (16 and 18 Oct), Sitemaps report (39 discovered pages, up from 38), URL Inspection on 16 and 18 Oct.

The article is published (collections audit: 16 Oct 13:10 UTC), has no robots meta, and is linked from /blogs/news and the blog's Atom feed. So Google will find it when it next crawls /blogs/news. It just isn't in the sitemap yet.

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

## Finding 13 — The whole store has been password-locked since the evening of 18 Oct

**Finding:**
At 20:09 and 20:11 BST on 18 Oct, every storefront URL tested returned 302 → /password, with or without a Googlebot user agent: /, /collections/tees, /collections/outerwear, /blogs/news/convict-vs-cellblock-fit, /products/crooks-express-t-shirt, every archived product URL and /collections/frontpage. `/sitemap.xml` returns 404. The password page has the title "CROOKSLDN" and no robots meta. The live theme is now named "CROOKSLDN — live 18 Oct + evening fixes". Between 16:30 and 17:05 BST the same day, the same URLs returned their normal pages, so the lock started after about 17:05 BST. Nothing in the programme records (change log, owner decisions, workstream branches) mentions it.

**Evidence:**
`curl` status checks on 18 Oct (16:30–17:05 BST open; 20:09 and 20:11 BST locked). Earlier pattern from `gsc_uk_16m_dates.csv` and the project's `10-measurement.md`: the store was locked before the May and July drops, and /password then collected brand-search impressions.

**Why it matters:**
- Brand searches now land on a password page, as on the May and July drop days.
- Google can't crawl anything: not the new /collections/outerwear, not the fit article, not the approved redirects or the hidden /collections/frontpage. The next sitemap fetch will fail.
- If the lock lasts more than a few days, already-indexed pages can start dropping out.
- It falls inside the first post-deploy measurement window (16–22 Oct), so that window can't be read as an SEO before/after.

**Confidence:** High for the lock and its timing window. Unknown whether it's intentional; probably the T-shirt Week launch, but not confirmed.

**Recommended action:**
George confirms it's intentional and when the store reopens. Leave lock days out of every like-for-like comparison and label them in each read. After reopening, re-run URL Inspection on the new and redirected URLs; don't request indexing while the store is locked. Checked again by the scheduled run on 20 Oct.
