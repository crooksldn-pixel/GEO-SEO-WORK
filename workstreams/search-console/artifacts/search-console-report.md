# 05 — Search Console (crooksldn.com)

Research only. First pass 16 Oct 2026; refreshed 18 Oct 2026 (17:05 BST, plus answers and lock note at 20:15 BST). Nothing was changed in Shopify, the theme, Merchant Center or Search Console. No "Request indexing", no sitemap submitted. URL Inspection was used read-only (indexed view plus one "Test live URL").

Raw exports: `/mnt/project-files/seo/measurements/gsc/` (mirrored on GitHub branch `cowork/search-console` under `workstreams/search-console/artifacts/gsc-exports/`).

"Suggested owner" names the programme workstream best placed to act. This workstream implements nothing.

## 1. What the data covers (read before using any number)

- Property `sc-domain:crooksldn.com`, the only property on team@crooksldn.com. Settings: "Property added to account 16 October 2026".
- **Performance data exists for 21 Jan – 22 Jul 2026, then 15 Oct onwards.** Nothing for 23 Jul – 14 Oct. As of 18 Oct 16:30, 15 and 16 Oct are in; 17 Oct is not yet.
- Indexing > Pages still says "Processing data, please check again in a day or so" (checked 16 and 18 Oct). Core Web Vitals, Shopping reports and Crawl stats stop at 23 Jul.
- Most likely explanation (not confirmed): an earlier verification of the domain lapsed around 22 Jul, and the 16 Oct re-verification restarted collection. Shopify reported organic search sessions and orders through the gap, so Google traffic continued; GSC just didn't record it.
- **Use Jan–Jul as a reference period, not the baseline.** It is pre-relaunch and pre-deploy, and page-level rows reflect the old site's URLs.
- **Store password-locked from the evening of 18 Oct** (after ~17:05 BST; seen at 20:09 and 20:11 BST): every URL 302s to /password, Googlebot included, and /sitemap.xml returns 404. Probably the T-shirt Week launch, but not confirmed. Lock days must be labelled and left out of like-for-like comparisons.
- **T-shirt Week** runs Monday to Sunday (owner decision #24). Presumed 19–25 Oct; the main chat says its 14 tees went live 18 Oct. Expect a branded and tee-query spike that isn't an SEO result.
- **Baseline anchors:** 15 Oct is the only full pre-deploy day on record; 16 Oct is deploy day. First usable post-deploy read: 7 days, 16–22 Oct (in GSC around 24 Oct). 28-day read: 16 Oct – 12 Nov (around 14 Nov).

## 2. Baseline totals

### Reference period: UK, web, 21 Jan – 22 Jul 2026 (183 days)

| Segment | Queries | Clicks | Impressions | CTR | Avg pos |
|---|---|---|---|---|---|
| **Property total** | — | **14,312** | **35,948** | 39.8% | 4.2 |
| Branded — programme definition (contains crooks / crooksldn / crooks ldn / crooks london / convict hoodie / cellblock) | 124 | 12,303 | 27,925 | 44.1% | 4.21 |
| Non-branded — everything else | 146 | 61 | 766 | 8.0% | 12.82 |
| Anonymised by Google (no query string) | — | 1,948 | 7,257 | — | — |

Same 270 queries, split more finely:

| Group | Queries | Clicks | Impressions | CTR | Avg pos |
|---|---|---|---|---|---|
| Branded (CROOKSLDN) | 93 | 12,303 | 27,785 | 44.3% | 4.02 |
| Brand misspellings (krooks, crooka, crroks, crook shop…) | 51 | 58 | 553 | 10.5% | 8.86 |
| Crooks & Castles (any "castle") | 35 | 0 | 147 | 0% | 42.45 |
| Conversational / AI-mode style | 17 | 2 | 19 | 10.5% | 1.89 |
| **Genuinely non-branded** | 74 | **1** | **187** | 0.5% | 24.34 |

**Non-branded search was effectively zero**: 187 impressions and 1 click in six months. No non-branded query reaches 50 impressions (largest: "ldn joggers", 22 @ 9.7). None of the URL-map intents (550gsm/heavyweight hoodie, tracksuit, baggy jeans, reactive jacket, fit/size) has Jan–Jul history.

Halves (UK):

| Period | Clicks | Clicks/day | Impressions | CTR | Avg pos |
|---|---|---|---|---|---|
| 21 Jan – 21 Apr (91 d) | 8,092 | 88.9 | 18,800 | 43.0% | 3.26 |
| 22 Apr – 22 Jul (92 d) | 6,220 | 67.6 | 17,148 | 36.3% | 5.31 |
| Last 30 days of data (23 Jun – 22 Jul) | 1,542 | 51.4 | 4,163 | 37.0% | 5.23 |

**Why clicks fell 23%:** the bare query "crooks" lost 1,076 clicks (1,573 → 497) as its position slid 5.4 → 8.7 on flat impressions (6,152 → 5,838). That one query is 60% of the 1,786-click drop in query-attributed clicks. The rest is spread across brand+category terms (crooks london −285, crooks clothing −135 with pos 2.0 → 3.8, crooks joggers −83, crooks streetwear −52 with pos 1.4 → 3.3). GSC doesn't show why "crooks" slid.

Drop days show as spikes: 14 Feb (615 clicks), 31 Mar (180), 2 May (591), 4 Jul (250). The store was password-gated around the May and July drops: /password collected impressions only on 2–6 May and 4–6 Jul.

### Post-gap anchor: UK, web, 15–16 Oct 2026

| Day | Clicks | Impressions | CTR | Avg pos |
|---|---|---|---|---|
| 15 Oct (pre-deploy) | 37 | 152 | 24.3% | 5.2 |
| 16 Oct (deploy day) | 49 | 143 | 34.3% | 4.1 |
| **Total** | **86** | **295** | 29.2% | 4.6 |

Top queries: crooks ldn 19 clicks / 30 impr @ 1.0; crooks london 14 / 17 @ 1.0; crooks 11 / 114 @ 6.1; crooks clothing 8 / 9 @ 1.0. Two days is too little to compare against anything; it's recorded as the anchor.

First non-branded commercial query on record: **"water reactive windbreaker" — 4 impressions, position 3.0, landing on /products/hydrocuff-windbreaker** (15–16 Oct, before /collections/outerwear was known to Google).

## 3. Ranked opportunity list

UK, 21 Jan – 22 Jul 2026 unless stated. "Best URL" follows the one-URL-per-intent map; unmapped intents name the nearest live, indexed URL. **Pattern behind most rows:** for brand+product searches Google showed the homepage, not a product or collection page (597 of 600 "joggers" clicks and all 136 "jeans" clicks went to `/`). The fix is making the mapped collection the obvious answer (internal links using the searched word as anchor text, and that word in the collection's H1/intro), not new pages.

| # | Query / cluster | Best URL | Impr | Pos | CTR | Recommended action | Pri | Conf | Suggested owner |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **crooks** | / | 11,990 | 7.0 (5.4 → 8.7) | 17.3% | A third of all impressions, 60% of the click loss. Entity markup is already live (16 Oct live test: Organization with alternateName "Crooks London" and "Crooks", sameAs Instagram + TikTok), so don't redo schema. Remaining levers: the homepage H1 is just "CROOKSLDN" — show "CROOKSLDN (Crooks LDN)" near the top (the brand's own disambiguation form, and the top query "crooks ldn"); make sure the Instagram and TikTok bios link to crooksldn.com. Measure from the 16 Oct anchor. | P1 | Medium (cause of slide unknown) | entity-about |
| 2 | crooks joggers, crooks ldn joggers, crooks london joggers, crooksldn joggers, ldn joggers | /collections/sweats | 1,561 | 1.2–1.8 (ldn joggers 9.7) | 35–46% | Largest product cluster, falling (crooks joggers 571 → 325 impr). Homepage got 1,560 of the impressions; /products/black-joggers 40. Link /collections/sweats from home and nav with "joggers" anchor; say "joggers" in its intro (title already does since 16 Oct). "ldn joggers" is the only non-branded query near page 1. | P1 | Medium | collections |
| 3 | crooks tesco shirt, crooks tesco tee, crooks tesco | /products/crooks-express-t-shirt (George confirmed 18 Oct: the Tesco tee is the Crooks Express tee) | 238 | 3.8–4.3 | 17–19% | **Rising** (52 → 186 impr). Homepage took 239 impressions, Crooks Express PDP 18. The two old URLs, /products/white-tesco-tshirt and black-tesco-tshirt, are **404**: 301 both to /products/crooks-express-t-shirt (approved, owner decision #21). Don't put "Tesco" in titles. | P1 | High | collections (redirects) |
| 4 | Brand sitelinks (15–16 Oct) | — | see §4 | ~1.0 | 0% | Brand searches now show sitelinks, and two of them are thin system listings: /collections/frontpage (title "PRODUCTS \| CROOKSLDN", 76 impr) and /collections/all (51). Noindex /collections/frontpage (or unpublish it and 301 to /collections/new) so a real collection can take its slot. /collections/tees-1, /search and /cart also appear but already redirect or are noindexed, so they will drop on recrawl. | P1 | Medium | collections |
| 5 | crooks t shirt, crooks tshirt, crooks shirt, crooks tee, crooks shirts | /collections/tees (indexed) | 169 | 5.9–9.9 | 0–14% | Pos 5–20 **and rising** (crooks t shirt 22 → 72 impr, pos 7.8 → 5.9; crooks tee new at 17). Homepage was the result. Link /collections/tees from home with "T-shirts" anchor. | P2 | Medium | collections |
| 6 | crooks jorts, crooks ldn jorts, crooks london jorts, ldn jorts, grey wash jorts | /collections/denim (indexed) | 278 | 2.0–2.4 | 25–30% | **Rising** (crooks ldn jorts 2 → 62, crooks jorts 83 → 124). Homepage 278 impr vs old jorts PDP 32 (that PDP got 31% CTR). Old /products/cb2-wash-jorts now 301s to /products/grey-wash-yard-jorts — keep. "Jorts" anchor link to /collections/denim. | P2 | Medium | collections |
| 7 | crooks jeans, crooks ldn jeans, crooks london jeans, miss crooks jeans, lnd jeans | /collections/denim + /products/og-jeans | 420 | 1.2–2.1 | 31–38% | **Falling** (crooks jeans 189 → 63 impr, pos 1.7 → 3.2). Crawl stats show /products/og-jeans returned **404 to Googlebot on 19–23 Jul** (200 now) — likely part of the slide. Homepage took 423 impr, OG Jeans 17. Same anchor-link fix. | P2 | Medium | collections |
| 8 | crooks clothing, crooks brand, crooks streetwear, crooks clothes, crooks london clothing, crook clothing, crooks clothing brand | / | 2,623 | 1.4–2.9 | 25–64% | Positions slipped (crooks clothing 2.0 → 3.8, crooks streetwear 1.4 → 3.3, crooks brand 2.0 → 2.8). Same entity work as #1. | P2 | Medium | entity-about |
| 9 | crooks shorts, crooks ldn shorts | Unmapped. Nearest: /collections/denim (Yard Jorts), /products/charcoal-cellblock-shorts | 151 | 5.5 / 1.4 | 15% / 45% | Rising (40 → 111 impr). "crooks shorts" sits at pos 5.5. Not worth a page; cross-link the shorts products from /collections/denim and /collections/sweats. | P3 | Low | collections |
| 10 | (page) /collections | /collections | 213 | 4.3 | 14.1% | All 30 clicks were Jan–Apr. Now a brand sitelink (90 impr, 15–16 Oct). Title "Collections \| CROOKSLDN", **no meta description** — give it one. | P3 | Medium | collections |
| 11 | crooks hoodie, crooks hoodies | /collections/sweats | 27 | 5.9–6.2 | 11.5% | The 550gsm hoodie intent at small volume; covered by #2's linking. | P3 | Medium | collections |
| 12 | crooks ldn logo, crooks logo, crooks london logo | / | 82 | 1.5–5.2 | 0–12% | Image intent, falling. No action. | P4 | High | — |
| 13 | krooks, crooka, crroks, crook shop, other misspellings | / | 553 | 6.9–13.6 | 0–11% | Rides on #1. No action. | P4 | Medium | — |
| 14 | Crooks & Castles variants | none | 147 | 13.5–63.9 | 0% | Negligible in UK (zero clicks). The real overlap is inside "crooks" (#1). Don't target. | P4 | High | — |

Machine-readable copy: `artifacts/opportunities.csv` on the GitHub branch.

### Queries at positions 5–20 with 50+ impressions (task 3)

| Query | Impr | Pos | CTR | Branded | Best URL |
|---|---|---|---|---|---|
| crooks | 11,990 | 7.0 | 17.3% | yes | / |
| krooks | 153 | 7.7 | 3.9% | misspelling | / |
| crooks t shirt | 94 | 6.4 | 13.8% | yes | /collections/tees (unmapped) |
| crooks. | 93 | 7.3 | 19.4% | yes | / |
| crooks shorts | 78 | 5.0 | 15.4% | yes | unmapped — /collections/denim |
| crooka | 54 | 7.6 | 0% | misspelling | / |

No non-branded query qualifies.

### High-impression, low-CTR and cannibalisation (task 4)

Low-CTR queries (50+ impr): crooks (11,990 @ 7.0, 17.3%), crooks jeans (252 @ 2.1, 31.7%), crooks jorts (207 @ 2.0, 30.4%), crooks ldn jorts (64 @ 2.0, 25%), crooks london jeans (50 @ 1.4, 32%), crooks ldn logo (55 @ 1.7, 3.6%).

Low-CTR pages: /products/crooks-express-t-shirt (381 @ 3.1, 1.3%), /password (307 @ 1.5, 0.7%), /products/cb2-wash-jorts?variant=… (264 @ 1.7, 4.5%), /collections (213 @ 4.3, 14.1%), /products/v1-hoodie (172 @ 1.7, 2.9%). These are **not** real snippet problems: the per-page breakdowns show they were second results for navigational brand queries ("crooks ldn", "crooksldn") under the homepage (e.g. 238 of the Crooks Express tee's 381 impressions were "crooks ldn"). Ignore their CTR.

Cannibalisation: one real pattern — **homepage vs the mapped product/collection page for brand+product queries** (joggers, jeans, jorts, shirt/tee, shorts, tesco). Every cluster sent >90% of impressions to `/`. No case of two product or collection pages splitting a query. Variant (`?variant=`) and `?utm_source=shop_app` URLs picked up stray impressions; variant URLs canonicalise to the base product (checked), so no action.

### Emerging queries and pages losing clicks (task 5)

Emerging (Apr–Jul vs Jan–Apr, plus 15–16 Oct):
- **Reactive outerwear**: "water reactive windbreaker" (15–16 Oct, 4 impr @ 3.0 → HydroCuff PDP). First non-branded commercial query on record.
- **Tees**: crooks tesco tee (new, 69 impr), crooks tesco shirt 51 → 117, crooks t shirt 22 → 72, crooks tee (new, 17).
- **Jorts/shorts**: crooks ldn jorts 2 → 62, crooks jorts 83 → 124, crooks ldn shorts 16 → 57, crooks shorts 24 → 54.
- **First generic tracksuit/jogger signals**: ldn tracksuit (new, 5 @ 19.0), dfnd london jogger (new, 5 @ 19.2).
- **Shown alongside other London labels**: protect ldn (18 @ 28.9), blake ldn (13 @ 34.4), project ldn (9 @ 20.6), zrk ldn, nocturn ldn, ultralight ldn. Topical association, no traffic.
- **Conversational drop-day queries** at pos 1–5: "when does it go live", "when is the drop", "i want the password", "next drop", "is it a good price", "how much do they weigh". Looks like AI-mode follow-ups around drops; tiny volume.

Pages losing clicks:

| Page | Clicks Jan–Apr → Apr–Jul | Impr | Pos |
|---|---|---|---|
| / | 7,064 → 5,274 (−1,790) | 15,076 → 13,606 | 3.3 → 5.6 |
| /collections | 30 → 0 | 192 → 21 | 4.3 → 4.7 |
| /products/v1-hoodie | 4 → 1 | 144 → 28 | 1.5 → 2.2 |

Every other page with impressions first appeared in Apr–Jul.

## 4. Index hygiene (task 6)

Indexing > Pages is still processing, so its "why pages aren't indexed" list can't be read yet. Each in-scope URL was checked with URL Inspection (Google's indexed view) and a live status check instead:

| URL | Google (URL Inspection) | Live | GSC impressions Jan–Jul (UK) | 15–16 Oct (UK) |
|---|---|---|---|---|
| /password | **Not indexed — Page with redirect**; last crawl 16 Oct 16:35 | 302 → / | 307 @ 1.5, 2 clicks — only on drop days 2–6 May, 4–6 Jul | — |
| /collections/frontpage | **Indexed** | 200, self-canonical, in sitemap, title "PRODUCTS \| CROOKSLDN" | none | **76 impr — brand sitelink** |
| /collections/all | **Indexed** | 200, self-canonical, in sitemap | 21 @ 7.1 | **51 impr — sitelink** |
| /collections/tees-1 | **Indexed** (last crawl 14 Oct, before its redirect) | 301 → /collections/tees | — | 21 impr — sitelink |
| /collections/sweats-1, /denim-1, /new-1 | not inspected | 301 → base collection | none | — |
| /search, /cart | not inspected | 200, `noindex` | — | 4 and 2 impr — sitelinks |
| /products/3-clives-tee | **Not indexed — Server error (5xx)** at last crawl 10 Sep | 404 | 31 (+17 on `?utm_source=shop_app`) | — |
| /products/evil-clive-tee | — | 404 | 20 (+2 `?variant=`, +1 `?utm_source=`) | — |
| /products/white-tesco-tshirt | — | 404 | 7, 1 click | — |
| /products/black-tesco-tshirt | — | 404 | 9 | — |
| /products/joggas-1 | Googlebot got 404 on 19 and 23 Jul (Crawl stats) | 404 | none | — |
| /collections/2005-drop/products/pink-crsdr-joggas, …/pink-crsdr-hoody | — | 404 (products now /products/pink-crsdr-joggers, -hoodie) | 7, 1 | — |

**The five archived products** (from the collections workstream's Shopify Admin read) are og-crook-tee, 3-clives-tee, broadcast-tee, evil-clive-tee and large-duffle-bag. **Two of the five had impressions**: 3-clives-tee and evil-clive-tee (table above). og-crook-tee, broadcast-tee and large-duffle-bag had none in Jan–Jul.

**Five more 404s** had impressions or Googlebot hits but aren't archived products, so they aren't on the collections redirect list yet: white-tesco-tshirt and black-tesco-tshirt (with live "tesco" query demand, see #3; approved target /products/crooks-express-t-shirt), joggas-1 (→ /collections/sweats), and the two 2005-drop pink CRSDR URLs (→ /products/pink-crsdr-joggers and -hoodie).

(A hint about CB1/CB2 washes was withdrawn on 18 Oct: George confirmed CB1/CB2 were placeholder names, so nothing should be derived from them.)

New 16 Oct pages:

| URL | 16 Oct | 18 Oct |
|---|---|---|
| /collections/outerwear | Not in sitemap; "URL is unknown to Google" | **In sitemap; "Discovered – currently not indexed"** (found via sitemap.xml) |
| /blogs/news/convict-vs-cellblock-fit | Not in sitemap; unknown to Google | **Still not in sitemap_blogs_1.xml; still unknown to Google.** It is published, has no robots meta and is linked from /blogs/news and the Atom feed, so Google will find it on its next crawl of /blogs/news, a page it rarely visits. Link it from /collections/sweats, /collections/tracksuits and the hoodie/crewneck size guides. |

Other findings:
- Map targets that are indexed: /collections/sweats, /collections/tracksuits, /collections/denim, /collections/tees, /products/hydrocuff-windbreaker (indexed "with issues" — old variant-image problem, see §7).
- **Markets currency URLs are being discovered**: Google lists `/products/convict-hoodie-1?variant=…&country=CZ&currency=CZK` as a referring page for the hoodie. That URL returns 200, canonicalises to the base product, and its Product JSON-LD says **priceCurrency CZK** (`Shopify.currency` active = CZK). See §7.
- Crawl stats (90 days to 23 Jul): 803 requests, avg response 181 ms; 95% 200, 2% 301, 2% 404, <1% 302, <1% unreachable. 404 samples: /products/og-jeans (19–23 Jul, now 200), /products/joggas-1, /products/hyrdocuff-windbreaker (typo handle, now 301 → hydrocuff-windbreaker), /favicon.ico (still 404), /b.
- http:// and www. both 301 to https://crooksldn.com/.

## 5. Sitemaps (task 9)

| Sitemap | Type | Submitted | Last read | Status | Discovered |
|---|---|---|---|---|---|
| https://crooksldn.com/sitemap.xml | Sitemap index | 16 Oct 2026 | 16 Oct 2026 | Success | 39 pages, 0 videos (38 on 16 Oct; /collections/outerwear added since) |

Children: products (21 products + homepage), pages 6, collections 9 (frontpage, tracksuits, tees, denim, sweats, accessories, new, all, outerwear), blogs 1 (/blogs/news only), agentic_discovery 1 (/agents.md). **/blogs/news/convict-vs-cellblock-fit is still missing** (see §4).

## 6. Core Web Vitals (task 7)

Source CrUX, last update 23 Jul 2026 (stale — same data gap).

| Device | Poor | Needs improvement | Good |
|---|---|---|---|
| Mobile | 0 | 0 | 8 URLs |
| Desktop | 0 | 0 | 8 URLs |

"No issues detected in the last 90 days." No URL groups to list: the good-URL drill-down shows only the count. HTTPS: 8 HTTPS, 0 non-HTTPS.

**This is out of date.** The live-site-checks workstream measured current field data through PageSpeed Insights on 16 Oct and found the homepage failing Core Web Vitals on mobile (INP). Use its figures, not this report, until Search Console shows CrUX data from after 16 Oct.

## 7. Currency and structured data (task 8)

**Answer: yes — GBP.** URL Inspection "Test live URL" on /products/convict-hoodie-1, 16 Oct 2026 21:15 (Googlebot smartphone, rendered): Offer `price 60.00`, `priceCurrency GBP` on all 5 size variants. Merchant listings: **5 valid items**, 2 non-critical issues each (variant `description` missing — optional; `hasMerchantReturnPolicy` missing inside `offers` — optional, it is set on the Organization). Product snippets 1 valid, Breadcrumbs 1 valid. Same GBP result from a raw fetch at a US IP for convict-hoodie-1, og-jeans and hydrocuff-windbreaker.

The indexed version is older: crawled 7 Oct, Merchant listings **5 invalid items — critical "Missing field 'image'" on every variant**. The live page now has a variant image, so this clears on recrawl.

Two structured-data issues worth fixing:

| Issue | Evidence | Action | Pri | Conf | Suggested owner |
|---|---|---|---|---|---|
| Currency-param URLs emit non-GBP prices | A `?country=CZ&currency=CZK` URL is known to Google, returns 200, canonical → base product, JSON-LD priceCurrency CZK. Theme builds it from `cart.currency`, so any `currency=` URL changes it. | Output JSON-LD price/currency in the store's base currency (GBP) regardless of `cart.currency`, or disallow `/*?*currency=` in robots.txt.liquid. | P2 | Medium | theme |
| shippingDetails overstates free shipping | Live test: Organization `shippingDetails` → `shippingRate 0.00 GBP`, no order threshold. Store policy is free UK shipping **over £30**. | Make shippingDetails reflect the real rate below £30, or drop it and rely on Merchant Center shipping settings. | P2 | Medium-high | theme (tell merchant-center) |

Shopping reports (to 23 Jul): Product snippets 6 valid / 0 invalid; Merchant listings 40 valid / 0 invalid. "Improve item appearance" lists missing hasMerchantReturnPolicy, missing shippingDetails, invalid GTIN, missing description — each at 0 items at last update.
