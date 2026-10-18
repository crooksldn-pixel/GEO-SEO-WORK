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

**Confidence:** High for the demand and the 404s. Medium for the target: it depends on which current design people mean.

**Recommended action:**
301 both URLs to /products/crooks-express-t-shirt if that's the design people call the "Tesco tee", otherwise to /collections/tees. George to confirm. Don't use "Tesco" in titles. Suggested owner: collections (redirects).

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

**Why it matters:**
The article is the mapped URL for fit and size intent. Two days on, this isn't sitemap lag.

**Confidence:** High.

**Recommended action:**
Check the article is published and visible on the Online Store channel. Link it from /collections/sweats and the hoodie and crewneck size guides so Google can discover it. Suggested owner: collections/blog.

## Finding 8 — Archived product URLs that had impressions now 404

**Finding:**
The likely five archived 404s are /products/3-clives-tee, /products/evil-clive-tee, /products/white-tesco-tshirt, /products/black-tesco-tshirt and /products/joggas-1. Four of the five had impressions before July (31+17, 20+3, 7, 9). 3-clives-tee shows "Server error (5xx)" from its last crawl on 10 Sep. Old drop handles /collections/2005-drop/products/pink-crsdr-joggas and -hoody also 404; the products now live at /products/pink-crsdr-joggers and -hoodie.

**Evidence:**
`gsc_uk_16m_pages.csv`, Crawl stats 404 samples, URL Inspection, `curl`.

**Why it matters:**
Small, but each is lost demand and crawl noise. The Tesco pair matters most (Finding 5).

**Confidence:** High for the status codes. Medium for which five George meant.

**Recommended action:**
301 each to its nearest live equivalent (the pink CRSDR pair to their new handles; the Clive tees to /collections/tees). Suggested owner: collections (redirects).

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

## Finding 11 — No Core Web Vitals or HTTPS problems on record

**Finding:**
Mobile and desktop: 8 good URLs, 0 needing improvement, 0 poor. "No issues detected in the last 90 days". HTTPS: 8 URLs, all HTTPS. Data source is CrUX, last updated 23 Jul.

**Evidence:**
Core Web Vitals and HTTPS reports.

**Why it matters:**
Nothing here for the core-web-vitals workstream to fix, but the data predates the Horizon rebuild.

**Confidence:** Medium (stale).

**Recommended action:**
Recheck once fresh CrUX data appears.
