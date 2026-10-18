<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 5: Commercial-intent query research and query map

Status: **Research complete, read-only** (16 Oct 2026, 14:30–15:00 UTC; facts updated 18:40 UTC). No pages written, no store or theme changes.
Score = commercial impact × likelihood of success × speed, each 1–5 (max 125). Class P0–P4 per the brief.

## Sources and limits

- Shopify Admin API (read): 25 active products, 9 collections, 7 pages, 1 blog article (16 Oct 2026).
- Live pages via WebFetch: /collections/sweats, /denim, /tracksuits, /pages/faq, /products/convict-hoodie-1, sitemaps.
- Search-landing proxy from [04-search-console.md](04-search-console.md) (Shopify search sessions by landing page, 90 days). **No Search Console query data exists yet**, so no volumes or positions below are measured; demand is inferred from SERP shape.
- SERP research used the only web search available here, which is **US-located**. Every SERP note says what a UK Google result is likely to differ on. A UK-located check (logged out, UK IP) should confirm each before money is spent on it.

## What changed since the roadmap was written (evidence beats roadmap)

1. **A fit guide already exists.** /blogs/news/convict-vs-cellblock-fit ("Convict 550gsm vs Cellblock 450gsm: how they fit") was published 16 Oct 2026 13:10 UTC, outside this project. It explains gsm, compares 550 vs 450gsm, and gives full size tables. The roadmap's separate "550gsm" and "sizing guide" pages would cannibalise it. It is the only blog article.
2. **/collections/tracksuits duplicates /collections/sweats.** Tracksuits lists the 6 individual Convict hoodies and sweats, which are also 6 of the 8 products on Sweats. The actual set products (Black/Grey/Pink Set £110, Cellblock Set £85) live only in /collections/sets, which is not in the sitemap and has no SEO fields. So the "matching set" intent lands on a page that doesn't sell the set. Tracksuits is also the collection with the most search landings (22 in 90 days vs Sweats 6, Denim 3).
3. **The FAQ is already good.** /pages/faq has rendered content on delivery, sizing, returns and payment (Admin body is empty; the theme renders it). No new FAQ page is needed. One inconsistency: FAQ says "over £80 gets free tracked Royal Mail 24", PDP says "Free UK Tracked 24 included". Passed to workstreams 2 and 6.
4. **Only one denim product is baggy jeans.** OG Jeans is baggy/stacked; Yard Jeans are explicitly "Structured, not baggy". Yard Jorts are baggy. Any "baggy jeans" page would be one product deep.
5. ~~No /collections/outerwear exists~~ Created and live on 16 Oct (programme thread).
6. **Branded search is ambiguous.** US results for "Crooks LDN streetwear" return only Crooks & Castles. UK results may differ, but entity disambiguation is a real risk. Passed to workstream 6.
7. **/products/cb2-wash-jorts** got 10 search landings in 90 days but is not an active product. Check it redirects to the Yard Jorts (workstream 1/9).

## Intent clusters and URL decisions

One primary URL per cluster. "Owner" is the workstream that should implement, so nobody edits the same file twice.

### C1. Heavyweight / 550gsm hoodies and joggers
- **Queries:** 550gsm hoodie UK, heavyweight hoodie UK, heavyweight joggers UK, baggy hoodie UK, 550gsm joggers, heavyweight baggy joggers.
- **Intent:** transactional with some commercial investigation.
- **SERP (US):** mixed. Retailer PDPs (ASOS "premium heavyweight 500gsm"), marketplaces (Lyst), and listicles ("best heavyweight hoodies", mensflair.com, apetogentleman.com). For "550gsm hoodie UK" the US index returned UK university merch and workwear, which means **no brand owns "550gsm" as a term**. That's an opening. UK SERP likely adds ASOS, Represent and Decathlon category pages.
- **Crooks assets:** 3 Convict hoodies + 3 Convict sweats at £60, all 550gsm; product titles already say "550gsm". Black joggers convert at 15.4% from search (13 sessions, small sample).
- **Decision:** **existing collection improvement** at /collections/sweats (primary). Product pages are already well targeted; no change. **No new landing page**, which would duplicate Sweats.
- **Recommended implementation:** title and H1 add "Heavyweight" (as P1 audit item 5); one copy line linking to the fit guide ("how 550gsm and 450gsm compare") and to /collections/tracksuits for sets. Wait for GSC if the user prefers evidence first, since the meta was rewritten today.
- **Owner:** workstream 1.

### C2. What gsm means / 550 vs 450gsm / is 550gsm heavy (informational)
- **Queries:** what does gsm mean in hoodies, is 550gsm heavyweight, 450gsm vs 550gsm, heavyweight hoodie gsm.
- **SERP (US):** supplier and print-shop explainers (Alibaba seller blog, Thygesen Apparel, teeone.co.uk). Weak, non-brand content, so a brand with real garments can compete. UK likely similar (teeone is UK).
- **Decision:** **no new page.** The existing article covers it. Optional small edit later: a two-sentence "is 550gsm heavy?" answer near the top (garment facts only, no industry claims we can't source). Strong GEO value: AI answers to "what is a good gsm for a heavyweight hoodie" cite pages that state a number plainly.
- **Owner:** workstream 5 (content). Needs links in from Sweats and the Convict PDPs (workstream 1), since the article currently has zero internal links pointing to it.

### C3. Heavyweight tracksuits / matching sets
- **Queries:** heavyweight tracksuit UK, fleece tracksuit men UK, matching hoodie and joggers set, baggy tracksuit, tracksuit set UK.
- **SERP (US):** large retailer category pages (Decathlon, ASOS, eBay) plus ASOS set PDPs ("4505 heavyweight 440gsm tracksuit set"). Category-page SERP, so a collection is the right page type. UK SERP will be the same retailers, plus JD Sports and Represent.
- **Crooks assets:** three £110 sets (550gsm) and the £85 Cellblock Set (450gsm, crewneck and shorts).
- **Decision:** **existing collection improvement** at /collections/tracksuits, made distinct from Sweats: show the three Convict Set products (the actual purchase unit and higher AOV), with the hoodies and sweats as secondary. Keep /collections/sets unindexed or redirect it to /collections/tracksuits so the set intent has one URL. **User decision (16 Oct):** the Cellblock Set (crewneck and shorts) is a matching set or co-ord, not a tracksuit. Tracksuits keeps hoodie + joggers only (the three Convict Sets). The Cellblock Set targets "matching set" / "co-ord" wording on its own product page and on Sweats (see C11).
- **Owner:** workstream 1 (collection rules and redirect). Highest-ranked item in this file.

### C4. Baggy jeans / stacked jeans / heavyweight denim
- **Queries:** baggy jeans UK, baggy jeans men UK, stacked jeans UK, heavyweight baggy jeans, 14oz jeans UK, straight leg jeans streetwear.
- **SERP (US):** price-comparison (PriceSpy UK), Depop, and brand blogs ("10 best streetwear jeans" on Represent's UK site). "Baggy jeans UK" is a head term dominated by big retailers and Levi's. Low likelihood for a 1-product range.
- **Decision:** **existing collection improvement** at /collections/denim for "jeans and jorts"; **product page improvement** at /products/og-jeans as the target for "heavyweight baggy stacked jeans" (long tail, realistic). **No baggy-jeans landing page**: one product would make it a thin doorway page. Revisit if more baggy fits drop.
- **Owner:** workstream 1 (denim collection) / workstream 2 (OG Jeans product data: missing fabric weight. Yard is 14oz; OG says only "heavyweight". The user should supply the oz).

### C5. Jorts / baggy denim shorts
- **Queries:** jorts UK, baggy jorts men, heavyweight jorts, below-the-knee jorts.
- **SERP (US):** Levi's GB, Lyst, Butter Goods at Flatspot (UK), ASOS jorts category, newspaper "best jorts" roundups. Seasonal; October is the trough.
- **Decision:** **existing collection improvement** (Denim already names jorts in the title). **No new page.** Revisit March–April. P3 now.
- **Owner:** workstream 1.

### C6. Reactive outerwear (Crooks' clearest differentiator)
- **Queries:** water reactive jacket, water reactive clothing, heat reactive puffer, heat reactive jacket, colour changing jacket, colour changing puffer, reactive streetwear.
- **SERP (US):** "water reactive jacket" returns brand PDPs (Lyle & Scott "Water Reactive Shell Jacket", On) mixed with "water-resistant" noise. "Heat reactive puffer" returns editorial (Yanko Design, snkrdunk) and a Louis Vuitton PDP. Small, specific SERPs where a direct PDP or collection can rank. UK SERP: Lyle & Scott is a UK brand, so it will likely be there too; "colour changing" (UK spelling) is a separate variant to check. Kids' "magic print" rainwear dominates generic colour-change queries, so target "jacket/puffer" and "streetwear" modifiers, not bare "colour changing clothing".
- **Crooks assets:** HydroCuff Windbreaker £85 (7.7% search conversion on 13 sessions), Double-Agent Puffa £140 (blank product type, no tags).
- **Decision:** (a) **product page improvements** first: both PDPs are the primary URLs for their exact queries; (b) **new collection** /collections/outerwear as the hub for "reactive jackets", already in workstream 1's plan; (c) **guide deferred**: a "how our reactive garments work" guide has strong GEO potential (AI assistants answer "streetwear brand with water-reactive jacket" from explanatory pages), but it **needs brand facts we don't have**: what the reactive effect is (print/ink type), what triggers it (wet only? what temperature?), how long it lasts, washing care. Don't write it until the user supplies those.
- **Owner:** workstream 1 (collection), workstream 2 (Puffa product type, tags, product data), workstream 5 (guide, once facts arrive).

### C7. Category discovery: best / British / London / independent / emerging UK streetwear brands
- **Queries:** best UK streetwear brands, British streetwear brands, London streetwear brands, independent British streetwear, emerging UK streetwear brands.
- **SERP (US):** editorial listicles only: Highsnobiety ("London city guide: 12 brands we love", "best English brands"), Complex UK ("British streetwear brands you need to get familiar with"), ldnfashion.com, Opumo, Grazia, Spocket, plus low-quality SEO farms (iconpolls, techbullion). UK SERP will be similar, with Complex UK/ldnfashion likely higher.
- **Decision:** **no new page.** A brand's own "best UK streetwear brands" listicle has no credibility with Google or AI assistants and breaks the duplicate-intent/doorway guardrail. The URL that should win the brand part of this intent is the **About/entity page** (workstream 6), plus the homepage (already titled "Crooks London Streetwear"). The rest is **external editorial inclusion** (workstream 7): ldnfashion.com, Complex UK, Highsnobiety and Opumo already run these lists. Ignore the farm sites.
- **Caveat (added after workstream 6's entity audit):** the registered office is [town redacted], [town redacted], not London (Companies House 16606021). Until the user confirms the brand's London connection, treat "London streetwear brands" as unconfirmed and favour "British"/"UK" queries. See [06-entity.md](06-entity.md).
- **Owner:** workstreams 6 and 7.

### C8. Competitor-alternative queries
- **Queries:** brands like Corteiz, Corteiz alternatives, brands like Carsicko, brands like Broken Planet, brands like Trapstar.
- **SERP (US):** Complex explainers about Corteiz, plus a lot of counterfeit/fake-store spam (it.com domains, hijacked .gov.sa and .edu pages). Real "alternatives" lists are thin, which means a genuine editorial mention would stand out.
- **Decision:** **no new page.** "Alternatives to X" pages on a brand's own site are low-trust, invite trademark issues, and rarely get cited. Route to workstream 7: target writers who cover Corteiz/Trapstar/Broken Planet (Complex UK, ldnfashion, Highsnobiety, GUAP).
- **Owner:** workstream 7.

### C9. Sizing and fit
- **Queries:** Convict hoodie size guide, how do Crooks hoodies fit, baggy hoodie sizing, should I size up oversized hoodie.
- **SERP (US):** brand-specific size pages and spammy "size chart" pages on hijacked domains. Non-branded demand goes mostly to listicles; branded demand matters for conversion more than traffic.
- **Decision:** **no new page.** PDPs already show full measurement tables as text (checked on /products/convict-hoodie-1), the FAQ covers sizing, and the fit article covers both fleeces. Add one link from the PDP size area to the fit article (workstream 1/2 theme work). A separate size-guide hub would split the same intent three ways.
- **Owner:** workstream 2 (PDP template).

### C10. Graphic tees
- **Queries:** graphic tees UK, streetwear t-shirts UK, heavyweight tee UK.
- **Decision:** **existing collection, revisit at the drop.** 3 live tees; 15 drafts (200gsm) tagged t-shirt-week; /pages/t-shirt-week exists with an empty body (not in sitemap). Don't target "heavyweight tee" with 200gsm product, as that would over-claim. P4 now.
- **Owner:** workstream 1 at drop time.

### C11. Cellblock / fleece shorts / made in Portugal
- **Queries:** matching set, co-ord set men, fleece shorts set, crewneck and shorts set.
- **Decision:** **product page** (Cellblock Set and pieces) plus the Sweats collection; **not** Tracksuits (user decision 16 Oct). Drop "made in Portugal" and "450gsm" as targets until origin and fabric weight are verified (see evidence gates below). **No new page.** Low volume; seasonal. P4.

### C12. Socks / caps
- MotionTec socks and the cream cap: branded-only demand. **No action** beyond workstream 2's product-type fix for the cap. P4.

## Ranked queue (this workstream)

| Rank | Class | Cluster | Action | Primary URL | Commercial ROI | SEO impact | GEO impact | Effort | Confidence | Score (I×L×S) | Dependencies | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | P1 | C3 tracksuits | Make Tracksuits sell the 3 Convict Set products (not Cellblock), distinct from Sweats; consolidate /collections/sets into it | /collections/tracksuits | High: £110 AOV; top search-landing collection | High: removes 6-product overlap with Sweats | Medium | 30–45 min | Med-high | 5×4×4=80 | User OK for collection changes | WS1 | Proposed |
| 2 | P1 | C6 reactive | Fix Puffa product data (type, tags), then Outerwear collection as hub | /products/double-agent-puffa, /products/hydrocuff-windbreaker, /collections/outerwear | High: £85/£140, best-converting search PDP | Med-high: small specific SERPs | **High**: the most distinctive, citable fact about the brand | 30 min | Med-high | 4×4×5=80 | User OK; WS1/WS2 already plan it | WS1, WS2 | Proposed |
| 3 | P1 | C1 heavyweight | Sweats title/H1 "Heavyweight", link to fit article and Tracksuits | /collections/sweats | High: £60 core range, 15% search conversion on joggers | Medium: "550gsm" SERP unowned | Medium | 15 min | Medium | 4×3×5=60 | Ideally GSC data (WS4) | WS1 | Proposed |
| 4 | P2 | C7/C8 discovery | Pitch list for editorial inclusion (ldnfashion, Complex UK, Highsnobiety, Opumo, GUAP) | external | Med-high long term | Medium | **High**: AI lists are built from these sources | Ongoing | Medium | 4×2×2=16 (slow, but high ceiling) | User approval for any contact | WS7 | Handed over |
| 5 | P2 | C2 gsm | Internal links into the fit article from Sweats, Tracksuits and Convict PDPs (the "is 550gsm heavy?" edit is blocked on spec evidence) | /blogs/news/convict-vs-cellblock-fit | Low-med | Medium: weak competing SERP | Med-high | 20 min | Medium | 2×4×5=40 | WS1 owns the collection copy edits | WS1, WS5 | Proposed |
| 6 | P2 | C4 denim | OG Jeans as "heavyweight baggy stacked jeans" target, stating 14oz (confirmed) | /products/og-jeans, /collections/denim | Medium | Low-med (head term out of reach) | Low | 10 min | Medium | 3×3×4=36 | None (14oz confirmed) | WS2 | Ready |
| 7 | P3 | C6 guide | Reactive garments guide (drafted, see 05-reactive-drafts.md) | /blogs/news/reactive-outerwear | Medium | Medium | High | 2 h | Medium | 3×3×2=18 | George's approval of the two ⚑ wording calls (Outerwear is live) | WS5 | Drafted, awaiting approval |
| 8 | P3 | C9 sizing | Link PDP size-guide area to the fit article | PDP template | Low-med (conversion) | Low | Low | 30 min theme | Medium | 2×4×3=24 | Theme owner (WS1/WS2) | WS2 | Proposed |
| 9 | P3 | C5 jorts | Revisit in spring | /collections/denim | Low now (season) | Low | Low | — | — | — | Season | WS1 | Deferred |
| 10 | P4 | C10 tees | Revisit at T-shirt Week drop; don't claim "heavyweight" at 200gsm | /collections/tees | Low now | Low | Low | — | — | — | Drop date | WS1 | Deferred |
| 11 | P4 | C11/C12 | No action | — | Low | Low | Low | — | — | — | — | — | Closed |
| 12 | P4 | C7/C8 | Own-site "best brands" / "Corteiz alternatives" pages | — | Low | Negative risk | Negative | — | High | — | — | — | **Rejected** (guardrail) |

## Roadmap P4 topics: verdict

| Roadmap topic | Verdict | Where it goes instead |
|---|---|---|
| 550gsm page | No new page | /collections/sweats + existing fit article |
| Heavyweight hoodies UK page | No new page | /collections/sweats |
| Baggy jeans UK page | No new page (1 product = thin) | /collections/denim + /products/og-jeans |
| Reactive clothing page | Collection now, guide later | /collections/outerwear, then a guide once facts are supplied |
| Sizing guides | No new page | PDP tables + FAQ + fit article (already live) |

Net result: **zero new pages are justified right now.** Every commercial intent maps to an existing or already-planned URL. The only new content candidate is the reactive guide, blocked on facts.

## Evidence gates (updated 16 Oct 2026, 18:26 UTC: owner-confirmed facts override earlier gates)

- **GSM/oz: LIFTED.** Hoodies and joggers are 550gsm, crewnecks and shorts 450gsm, jeans and jorts 14oz. Hoodies and joggers are 100% cotton; don't extend composition to other categories. C1 can use 550gsm wording on Sweats/Tracksuits, the C2 "is 550gsm heavy?" fit-guide edit can go ahead, and C4 can state 14oz on OG Jeans. Tees have no confirmed weight, so make no "heavyweight tee" claim.
- **Reactive: PARTLY LIFTED.** HydroCuff: reacts to rain/water, back to normal once dry, wash cold, do not iron, "reasonably durable" (careful wording). Puffa: heat-reactive, avoid washing where possible. Still gated: reaction time, cycles/lifetime, wash temperatures, mechanism, Puffa trigger temperature and reversibility. Drafts written: [05-reactive-drafts.md](05-reactive-drafts.md) (PDP copy, Outerwear intro, guide). Not live.
- **Origin: RESOLVED.** All current products are made in China. "Made in Portugal" is wrong and must be removed wherever it appears, including the Sweats and Denim collection copy and the Cellblock PDPs (workstreams 1 and 2). Don't use origin as a search target or a marketing line.
- **Tees:** all print on demand, so selling at zero stock is correct. C10 copy must not imply the tees are stocked (dispatch wording belongs to workstream 2).

## Facts needed from the user (escalation)

1. ~~Reactive facts~~ partly answered 18:26. Still open: Puffa trigger and whether it changes back; HydroCuff reaction time; the two ⚑ wording calls in 05-reactive-drafts.md.
2. ~~OG Jeans fabric weight~~ answered: 14oz.
3. ~~Whether the Cellblock Set should sit under "Tracksuits".~~ Answered 16 Oct: no, it is a matching set / co-ord.

## Affected URLs/files

/collections/tracksuits, /collections/sets, /collections/sweats, /collections/denim, /collections/outerwear (planned), /collections/tees, /products/double-agent-puffa, /products/hydrocuff-windbreaker, /products/og-jeans, /blogs/news/convict-vs-cellblock-fit, /pages/faq, /products/cb2-wash-jorts (legacy). No files or store objects changed.

## Monitoring (for workstream 10)

Add these to the GEO query set as product-intent checks: "heavyweight tracksuit UK" (exists), "water reactive jacket" (exists), "heat reactive puffer" (exists), plus new: "colour changing jacket UK", "550gsm joggers", "stacked jeans UK", "what gsm is a heavyweight hoodie". Metric per cluster once GSC lands: impressions and clicks for the cluster's query group on its primary URL, and whether a second Crooks URL is taking impressions for it (cannibalisation).

## SERP sources consulted (US-located search, 16 Oct 2026)

- ASOS 500gsm hoodie: https://www.asos.com/asos-design/asos-design-premium-heavyweight-500gsm-zip-through-hoodie-in-black/prd/208996474
- https://mensflair.com/best-heavyweight-hoodies/ · https://www.apetogentleman.com/the-best-heavyweight-hoodie-brands-for-men/
- https://www.decathlon.co.uk/men/tracksuits · https://www.asos.com/us/4505/4505-icon-rest-day-heavyweight-440gsm-cotton-tracksuit-set-in-light-heather-gray/grp/210145543
- https://pricespy.co.uk/s/baggy-jeans-men/ · https://uk.representclo.com/blogs/articles/10-best-streetwear-jeans
- https://www.levi.com/GB/en_GB/clothing/women/shorts-skirts/super-baggy-jorts/p/005DT0005 · https://www.flatspot.com/products/butter-goods-weathergear-heavyweight-denim-shorts-washed-indigo
- https://www.lyleandscott.com/fr/products/water-reactive-shell-jacket-water-reactive-black
- https://www.yankodesign.com/2024/11/24/this-puffer-jacket-color-shifts-when-exposed-to-heat-or-water/amp/ · https://br-int.louisvuitton.com/eng-e1/products/lv-2054-heat-reactive-puffer-nvprod3210058v/1A9KGY
- https://www.mountainwarehouse.com/community/expert-advice/outdoor/buying-guides-outdoor/the-magic-behind-water-activated-colour-changing-technology/
- https://www.highsnobiety.com/p/london-city-guide-12-brands-we-love/ · https://www.complex.com/style/a/james-harris/british-streetwear-brands-you-need-to-get-familiar-with · https://www.ldnfashion.com/features/streetwear-brands/ · https://www.opumo.com/magazine/best-streetwear-brands
- https://www.complex.com/style/a/lei-takanashi/corteiz-streetwear-everything-to-know
- https://thygesenapparel.com/blog/what-is-gsm-in-fabric · https://teeone.co.uk/blogs/news/tagged/gsm-in-clothing
- "Crooks LDN streetwear" → Crooks & Castles results only (e.g. https://mr-mag.com/streetwear-brand-crooks-castles-makes-its-comeback/)

## Owner-confirmed facts, 16 Oct 2026 18:26 UTC (override earlier conclusions in this file)
George confirmed these in the project chat. Where this file says otherwise, this section wins.
1. **Origin:** all current products are made in China. Remove all 7 "Made in Portugal" values. Use China only where origin is required (Shopify customs country, any required feed or legal field). Don't add consumer-facing origin copy otherwise.
2. **Fabric weights:** hoodies 550gsm, joggers 550gsm, crewnecks 450gsm, shorts 450gsm, jeans 14oz, jorts 14oz. OG Jeans is read as 14oz under "jeans"; correct this if George says otherwise. Existing claims matching these weights are supported and stay. Tees have no confirmed weight.
3. **Composition:** current hoodies and joggers are 100% cotton. Don't extend this to other categories.
4. **HydroCuff:** reacts to rain and water, returns to normal when dry, wash cold, do not iron, reaction "reasonably durable" (careful wording, no cycle or lifetime claims). Reaction time is still unconfirmed.
5. **Double-Agent Puffa:** heat-reactive; care guidance is to avoid washing where possible. No wash temperatures, durability or lifetime claims until there's supplier care info.
6. **Barcodes:** swing tags don't carry them, but the item bags do. **Do NOT clear the Shopify barcode values.** First establish whether the bag codes match the Shopify variant barcodes, whether any current or planned pick/pack workflow scans them, and whether moving them to SKU would break matching. The fix for the feed's invalid GTINs moves to the Merchant Center side (feed rule or supplemental feed to stop sending them as GTIN, identifier_exists=no), leaving Shopify untouched.
7. **Tees:** ALL tees are print on demand. Zero or negative inventory on tees is NOT overselling, and continue-selling is correct. The task is now an honesty audit: Shopify supports continued selling, Merchant Center availability and handling time are accurate, customers see a true production and dispatch expectation, and nothing describes tees as physically in stock.

## Owner decisions, 16 Oct 2026 18:30 UTC (override earlier recommendations in this file)
- Theme copy "Claude P1 fixes" (schema and popup): **HOLD**, do not publish.
- Product-data batch 2: **APPROVED**, except that barcodes must not be removed or remapped (item bags use them).
- Google Shopping gender: **MIXED.** Crooks sells men's and women's products, so assign gender per product, never one catalogue-wide value.
- Tracksuits: **YES**, list the three Convict Sets.
- Judge.me reviews on product pages: **NO** for now.
- Mida: **KEEP** (in use). Crooks Partner Hub: **KEEP.** Orderify: no live campaigns, so turn the embed off and prepare removal once no other dependency is found.
- About page: **not approved yet**; keep it drafted. "Designed in-house" = true; "free size swaps" = true.
- Official profiles for sameAs: https://crooksldn.com, Instagram @crooksldn, TikTok @crooksldn **only**. Not crooksldn.uk, X, YouTube, Pinterest or Depop.
- Tier-1 creator samples: **declined for now**.
