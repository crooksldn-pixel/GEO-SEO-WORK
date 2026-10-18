<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# CROOKSLDN work register / change log

Owner: workstream 1 thread (the only session that writes to Shopify or the theme copy). Other workstreams propose changes via /mnt/project-files/seo/master-queue.md.

Baselines: 9 Oct 2026 GEO 43. 15 Oct GEO 50, SEO health 70. 16 Oct GEO 54, SEO health 74.
Never record a ranking or GEO improvement without a captured measurement.

## Entries

### C-001 · Outerwear collection · 16 Oct 2026
- **Baseline:** no Outerwear collection; /collections/outerwear unreadable; HydroCuff Windbreaker (£85, type Outerwear) and Double-Agent Puffa (£140, blank type, no tags) have no category page; Outerwear absent from menus.
- **Rationale:** the two highest-priced products have only product pages for their query family.
- **Target intent:** water reactive jacket/clothing, heat reactive puffer/clothing, streetwear jacket UK.
- **Affected:** product double-agent-puffa (type + tags); new collection /collections/outerwear; main-menu SHOP dropdown; footer column (theme, later).
- **Expected result:** collection indexed and in sitemap; GSC impressions for reactive-outerwear queries on /collections/outerwear within 4–8 weeks.
- **Approval:** user, 16 Oct 15:33 UTC ("Approve Outerwear and collection copy. Go live.")
- **Implementation (16 Oct ~15:40 UTC):** (1) double-agent-puffa productType "" → "Outerwear", tags [] → outerwear, heat-reactive, puffer. (2) Created smart collection "Outerwear" (gid 698784121175, handle outerwear, rule product type = Outerwear, sort best-selling), SEO title "Water-Reactive & Heat-Reactive Jackets", SEO description and body copy per workstreams/01 draft; published to Online Store. (3) main-menu SHOP dropdown: added OUTERWEAR (collection link) between TRACKSUITS and ACCESSORIES; all other items resent unchanged.
- **Validation:** Admin read-back: collection has 2 products (hydrocuff-windbreaker, double-agent-puffa). Live fetch of /collections/outerwear: title "Water-Reactive & Heat-Reactive Jackets | CROOKSLDN", meta as set, H1 "Outerwear", copy shown, "2 ITEMS"; OUTERWEAR shows in the SHOP dropdown.
- **Deployment status:** live. Footer link (theme, footer-group.json block c1 slot 6) not done: live theme writes are blocked for this connection; user to add in theme editor.
- **Metric to monitor:** GSC impressions/clicks for /collections/outerwear; GEO rows "water reactive jacket", "heat reactive puffer".

### C-002 · Tracksuits collection copy · 16 Oct 2026
- **Baseline:** SEO title "Convict Tracksuits: Matching Fleece Sets | CROOKSLDN"; description without internal links.
- **Rationale:** add "heavyweight" + "550gsm" to the title for the "heavyweight tracksuit UK" family; link to Sweats. Per user (16 Oct) "tracksuit" means hoodie/track jacket + joggers only; Cellblock Set is not described as a tracksuit.
- **Implementation:** SEO title → "Heavyweight Tracksuits, 550gsm Fleece Sets" (theme appends " | CROOKSLDN"), then at ~16:00 UTC → "Heavyweight Tracksuits: Matching Fleece Sets" because "550gsm" has no supplier evidence yet (user answer 22); SEO description unchanged (its pre-existing "550gsm" is flagged in the master queue with the other GSM claims); description + sentence linking /collections/sweats and pointing to per-size measurements.
- **Validation:** live fetch shows new title, unchanged meta, Sweats link present, 6 items.
- **Deployment status:** live, 16 Oct ~15:42 UTC.
- **Metric:** GSC impressions/position for "heavyweight tracksuit(s) uk", "550gsm tracksuit" on /collections/tracksuits.

### C-003 · Sweats and Denim collection copy · 16 Oct 2026
- **Status:** approved, NOT applied. The live /collections/sweats and /collections/denim are not visible to this Admin API connection (only stale sweats-1/denim-1, 0 products). Draft copy in workstreams/01; user or the other editor to paste in Shopify admin, or tell me how those collections are managed.

### C-004 · Organization/Brand/WebSite schema (theme copy) · 16 Oct 2026
- **Baseline:** alternateName ["Crooks London","Crooks"]; no founder, identifier or country; fallback description "streetwear label… accessories".
- **Rationale:** one unambiguous entity; facts approved by the user in answers 10, 12, 14.
- **Implementation:** `snippets/crooks-schema-site.liquid` on theme copy 207340142935: alternateName adds "Crooks LDN" (Organization, WebSite; Brand gets ["Crooks LDN","Crooks London"]); Organization adds founder Person "George Hinxman", identifier Companies House 16606021, address addressCountry GB; fallback description = user's brand line. No foundingDate/location/street address.
- **Validation:** upload accepted (Liquid compiles); checksum eb35bdce… matches local file. Rendered JSON-LD not checked (no raw HTML access); run Rich Results Test on the preview/live homepage after publish.
- **Deployment status:** on unpublished copy only. Needs publish of the copy (live theme unchanged since 13:33 UTC, so the copy = live + C-004 + C-005).
- **Metric:** Knowledge-panel/AI answers naming CROOKSLDN = Crooks LDN; GEO brand rows.

### C-005 · Homepage popup delayed and softened (theme copy) · 16 Oct 2026
- **Baseline:** "The Getaway" opened 3 s after load, full screen on phones with scroll lock and dim.
- **Rationale:** user answer 5; spec workstreams/09 section B.
- **Implementation:** `snippets/crack-the-cuffs.liquid` on the copy: opens no sooner than 10 s, on 50% scroll + 10 s, a same-site return to the homepage, or desktop exit intent; phones get a non-modal bottom sheet (≤40vh, no dim/blur/scroll lock, × inside, tap-outside/Escape closes); RUN IT expands to the existing full-screen game; bare close quiets for the session, NOT NOW 14 days, win permanent; customer events ctc_shown/run/not_now/close/win via Shopify.analytics.publish. Offer copy, game, postMessage contract and ?ctc=1 unchanged.
- **Validation:** JS passes `node --check`; upload accepted; checksum f3f802ac… matches. Not yet browser-tested: check on a 390px phone via the theme preview with ?ctc=1 before publishing.
- **Deployment status:** on unpublished copy only.
- **Metric:** popup signups per 1,000 homepage sessions, 14 days before vs after; mobile conversion rate; GSC page experience.

### C-000 · Theme workspace · 16 Oct 2026
- Unpublished theme "CROOKSLDN — Claude P1 fixes (copy of live 16 Oct)" (gid 207340142935) created from live theme 207329132887. No edits yet. Publishing it would overwrite edits being made on the live theme today, so theme changes must be ported, not published wholesale.

### F-001 · Owner-confirmed facts (no site change) · 16 Oct 2026 18:26 UTC
- **Source:** George, project chat 18:26 UTC. These override earlier audit conclusions.
- **Origin:** all products made in China. The 7 "Made in Portugal" values are confirmed wrong and are to be removed (Q3). Nothing has been changed yet.
- **Weights and composition:** hoodies and joggers 550gsm, 100% cotton; crewnecks and shorts 450gsm; jeans and jorts 14oz. The 550gsm removed from the Tracksuits title in C-002 is now supported and may be restored if ranked worthwhile (Q4).
- **Reactive:** HydroCuff reacts to water, reverts when dry, wash cold, do not iron, reasonably durable. Puffa is heat-reactive; avoid washing where possible (Q37).
- **Barcodes:** item bags carry them, so the planned clear-to-SKU (batch 2 item 1) is withdrawn. Matching and scanning audit first; the feed-side GTIN fix is in Merchant Center (Q8).
- **Tees:** print on demand. Continue-selling at ≤0 is correct, and the "oversold" P0 is withdrawn. The task is now a dispatch-honesty and feed-availability audit (Q1).

### F-002 · Owner decisions (no site change) · 16 Oct 2026 18:30 UTC
- Theme copy (C-004 schema, C-005 popup): HOLD, do not publish. Batch 2: approved minus barcodes. Gender: mixed, per product. Tracksuits: list the 3 Convict Sets. Judge.me reviews: not shown. Mida: keep. Orderify: no live campaigns, prepare removal. Partner Hub: keep. About: not approved yet. "Designed in-house" and "free size swaps": true. sameAs: crooksldn.com, IG @crooksldn, TikTok @crooksldn only. Tier-1 samples: declined for now.

### C-006 · Product-data batch 2 · 16 Oct 2026 ~19:00 UTC
- **Approval:** user 18:29 ("Product-data batch 2: APPROVE … do not remove/break those barcode mappings"). Barcodes untouched.
- **Baseline:** sets Uncategorized (Cellblock = Sweatpants), cap = Sports Collectibles with blank type; no colour on HydroCuff, Blue Yard Jeans, 4 sets, cap; Grey Wash Jorts = Black, both socks = Geometric; Grey/Black/Pink Set and Crooks Express descriptions empty; Pink/Black/Cellblock sets showed the top only; Puffa 2 images with empty alt, reacted photo not on the product; hoodies/joggers material Fleece only.
- **Implementation:** (1) categories: 4 sets → Apparel & Accessories > Clothing > Outfit Sets; cap → … > Hats > Baseball Caps, product type Accessories (joins the Accessories smart collection). (2) `shopify.color-pattern`: HydroCuff Black, Blue Wash Yard Jeans Blue, Grey Set Gray, Pink Set Pink, Black Set Black, Cellblock Set Gray (Shopify has no Charcoal; Gray is the Google value), cap Cream (new metaobject, taxonomy Beige), Grey Wash Jorts Black → Gray, Black/Blue socks → Black + Blue, White/Red socks → White + Red (new Red metaobject). Puffa colour not set. (3) descriptions on Grey/Black/Pink Set (550gsm, 100% cotton, set price vs separate, links to both pieces) and Crooks Express (says "printed to order", no dispatch promise). (4) set images: 2 sweats images each on Pink and Black Set, 2 shorts images on Cellblock Set (alt "matching co-ord", never "tracksuit"). (5) Puffa: alt on both images from description facts (pixels not viewable from here: CDN blocked), heat-reacted photo attached at position 2. (6) Q4 material: `crooks.fabric` → "100% cotton, 550gsm brushed fleece" and `shopify.fabric` Cotton + Fleece on the 6 Convict hoodies/joggers.
- **Not done:** cap off the Google & YouTube channel (MCP blocks unpublishing; user does it in admin); gender (no product data says which pieces are women's); tee customs origin left blank (print on demand).
- **Validation:** mutation read-backs clean; all new media READY; Puffa order = photo, reacted, second photo.
- **Metric:** GMC export item issues (missing colour/description/category, image warnings) on these 13 products.

### C-007 · Tracksuits lists the 3 Convict Sets · 16 Oct 2026 ~19:05 UTC
- **Approval:** user 18:29 ("Tracksuits: YES, it can list the three Convict Sets").
- **Implementation:** manual collection 687058518359 + grey-set, black-set, pink-set (9 products). Description now says 550gsm, 100% cotton and links the three sets at £110 vs pieces at £60. Cellblock Set not added. /collections/sets left as is (holds the Cellblock Set too; set pages keep `seo.hidden`).
- **Validation:** read-back 9 products; description saved.
- **Metric:** Tracksuits sessions → set add-to-carts; AOV on Tracksuits landings.

### C-008 · sameAs limited to IG + TikTok (theme copy, on HOLD) · 16 Oct 2026
- **Implementation:** `snippets/crooks-schema-site.liquid` on copy 207340142935: allowlist changed from 14 social hosts to `instagram.com/crooksldn,tiktok.com/@crooksldn`; crooksldn.com stays the Organization url/@id. Live output today is already those two (footer links only them), so this guards against future footer links. Checksum f5527c5d…
- **Status:** unpublished, owner HOLD.

### Observed 16 Oct (not this thread)
- Q3 (Portugal removed, customs CN) was done by the product-schema thread: see C-WS02-1 below.
- Orderify is in use: [n] orders carry `orderify` / `orderifyCancelled(ForEditing)` tags (31 Aug–26 Sep), i.e. customers cancelling or editing their own orders. That is an operational dependency, so the embed stays on and removal waits for the owner.

## Outside changes observed
- 16 Oct: someone outside this project edited /collections/denim (title, meta, copy, 5 products) and published theme "CROOKSLDN — SEO round 2 (from live 16 Oct)". Details unknown.

### C-WS02-1 · "Made in Portugal" removed, customs origin China · 16 Oct 2026 (product-schema thread)
- **Baseline:** metafield crooks.origin = "Made in Portugal" on 7 products (v2-baggies, grey-wash-yard-jeans, blue-wash-yard-jeans, blue-wash-yard-jorts, grey-wash-yard-jorts, charcoal-cellblock-crewneck, charcoal-cellblock-shorts); crewneck description and SEO description also said "Made in Portugal". Inventory-item countryCodeOfOrigin set on 6 products only, blank on the rest.
- **Rationale / approval:** owner fact F-001 (all products made in China; remove unsupported Portugal claims; use China where origin is required).
- **Implementation (~18:20–18:45 UTC):** metafieldsDelete crooks.origin on the 7 products; crewneck descriptionHtml and SEO description re-sent without the Portugal sentence (all other text unchanged); inventoryItemUpdate countryCodeOfOrigin = CN on every inventory item of every ACTIVE non-tee product (25 products incl. all 4 sets, cap, Puffa).
- **Not changed:** tee inventory items (print on demand; where the blank is made/printed is not on record, so origin left blank rather than guessed). Draft/archived products. Barcodes untouched.
- **Validation:** Admin read-back 18:45 UTC: every active non-tee variant reads CN; crooks.origin absent on the 7 products; no userErrors on any write.
- **Deployment status:** live (store data). Theme JSON-LD reads crooks.origin only where present, so countryOfOrigin simply drops out; no theme change needed.
- **Metric to monitor:** duties/import charges shown at checkout for non-UK markets; no "Portugal" text in a site crawl.

### F-003 · Owner decisions on the 33-question pack (no site change) · 18 Oct 2026 17:03 UTC
- Full list and routing: `owner-decisions-2026-10-18.md`. Supersedes earlier open questions; unresolved items are parked.

### C-009 · Live tees: stock tracking off · 18 Oct 2026 ~17:20 UTC
- **Approval:** owner decision #2, 18 Oct 17:03 UTC.
- **Baseline:** CROOKS EXPRESS T-SHIRT, CRX GARMS T-SHIRT and CRXST★RZ T-SHIRT: 90 variants tracked, continue selling at 0; "[n] LEFT" lines possible on tee pages.
- **Implementation:** productVariantsBulkUpdate inventoryItem.tracked = false on all 90 variants. Inventory policy, barcodes and prices untouched.
- **Validation:** mutation read-back tracked=false on all 90, no userErrors.
- **Not done:** the 14 draft T-shirt Week tees (420 variants): the next write was refused by this session's permission check; waiting on George's "go" in the decision-pack thread. The "IN STOCK" label and the same-day dispatch lines are theme output and still show until the theme fix (owner decision #1/#7).
- **Metric:** tee-related "where is my order" contacts; tee PDPs show no "[n] LEFT".
