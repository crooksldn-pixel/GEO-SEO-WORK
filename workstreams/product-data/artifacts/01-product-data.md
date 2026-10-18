# Cowork results 01 — product data (CROOKSLDN Shopify)

This is the results file the 16 Oct brief asked for (`seo/cowork-results/01-product-data.md`). It's kept here for `cowork/programme-records` because the seo folder isn't reachable from this session.

For each item: baseline, exact change, George's approval and time, Admin read-back, and the metric to watch. Approval and read-back stay "pending" until a write actually happens.

- First baseline: 16 Oct 2026, 20:31 BST
- Re-check: 18 Oct 2026, 16:30 BST
- Source: Shopify Admin GraphQL (API 2026-01), read-only queries
- Store: 25 active products, of which 22 are non-tee and 3 are tees (30 tee variants). All non-tee variants carry country of origin CN; tee variants are blank on purpose.
- Writes by this session so far: none.

---

## A. Cream Cap off "Google & YouTube" (pre-approved, batch 2)

- Product: MAJOR LEAGUE CROOKS CAP (CREAM), `gid://shopify/Product/11236081402199`
- Baseline (unchanged on 18 Oct): ACTIVE, 0 media, empty description, no SEO title or description. Published on Online Store, Shop, Point of Sale, Click & Drop, Facebook & Instagram, TikTok and Google & YouTube (`gid://shopify/Publication/333206487383`).
- Change: `publishableUnpublish` from Google & YouTube only. Every other channel stays as it is.
- 16 Oct, 20:29 BST: the connector's permission check refused the write before it reached Shopify. The pre-approval is in the brief file rather than in chat.
- Approval: pending (QUESTIONS Q1)
- Admin read-back: pending
- Metric: the Cap leaves the Google & YouTube feed, and its Merchant Center image disapproval clears.
- Risk: Google's auto-add from the site crawl starts on 2 Nov and may re-add the cap, still without an image (`cowork/merchant-center` Finding 7).

## B. Store description

- Baseline (unchanged on 18 Oct): `shop.description` is empty.
- Change: set to exactly "CROOKSLDN is an independent British streetwear brand making heavyweight fleece, baggy denim, graphic tees and reactive outerwear, cut in oversized, street-led silhouettes and released in drops." (195 characters)
- Route: the Admin API has no mutation for this field, so it has to be set in Shopify admin in the browser.
- Approval: pending
- Admin read-back: pending
- Metric: the Organization schema description on the homepage (Rich Results Test).

## C. Weight and composition audit

Scope: title, description, SEO title, SEO description, every image alt, crooks.fabric and shopify.fabric on all 25 active products. The 18 Oct re-check found no change to any of these fields since 16 Oct.

Clean against the facts:
- All Convict hoodies, sweats and the Black, Grey and Pink Sets say 550gsm. "100% cotton" appears only on hoodies, joggers and those three sets, which contain only hoodies and joggers.
- The Cellblock crewneck, shorts and set say 450gsm.
- Both Yard jeans and both Yard jorts say 14oz.
- No GSM figure on any tee, no wrong oz figure, and no "100% cotton" on denim or outerwear.
- No Portugal and no "London-based" anywhere.

Conflicts with "the cotton claim applies to hoodies and joggers only":

| # | Product | Fields carrying the claim |
|---|---|---|
| C1 | CHARCOAL CELLBLOCK SHORTS | shopify.fabric (Cotton, Fleece) |
| C2 | CROOKS EXPRESS TEE | description, SEO title, SEO description, 2 alts, crooks.fabric |
| C3 | CRX GARMS T-SHIRT | description, SEO title, SEO description, 2 alts, crooks.fabric, shopify.fabric ("premium cotton") |
| C4 | CRXST★RZ T-SHIRT | SEO title, SEO description, crooks.fabric |
| C5 | BLACK/BLUE and WHITE/RED MOTIONTEC SOCKS | description, SEO description, crooks.fabric, shopify.fabric ("cotton blend") |

OG Jeans, 14oz added where it reads naturally: C6 crooks.fabric, C7 description, C8 SEO description.

Exact before/after strings for C1–C8 are in [c-fabric-claim-fixes.md](c-fabric-claim-fixes.md).

C9, added 18 Oct: remove the product tag `cotton` from the 3 live tees (tags today: black, cotton, tee, white). No collection rule uses it.

Titles, added 18 Oct from `cowork/merchant-center` task F (QUESTIONS Q6). The SEO title is also the Google Shopping title.

| Product | Before | After |
|---|---|---|
| CHARCOAL CELLBLOCK CREWNECK | no SEO title (Shopping shows "CHARCOAL CELLBLOCK CREWNECK") | Charcoal Cellblock Crewneck — 450gsm Fleece \| CROOKSLDN |
| DOUBLE-AGENT PUFFA | Double-Agent Puffa \| Heat-Reactive Puffer Jacket | Double-Agent Puffa — Heat-Reactive Puffer Jacket \| CROOKSLDN |

- Approval: pending (C1–C8 = QUESTIONS Q3, C9 = Q4, titles = Q6)
- Admin read-back: pending
- Metric: Google's material attribute on the tees, socks and Cellblock Shorts; the OG Jeans page and search snippet.

## D. Age group and tee inventory tracking

- D1 baseline: no age group on any product. The store has no `shopify.age-group` metafield definition, so the definition has to be enabled first, or the value set in the product admin or the Google channel.
- D1 change: age group "adult". The brief says 24 apparel products, but there are 25 active and all 25 sit under Apparel & Accessories, cap included. Recommend all 25.
- D2 baseline: all 30 tee variants are tracked = true, policy CONTINUE. Re-check on 18 Oct, same values:
  - CROOKS EXPRESS TEE: White XS −4, White M −4, White L 0, Black XL 0. The other six variants are positive.
  - CRX GARMS T-SHIRT: all ten variants at 0.
  - CRXST★RZ T-SHIRT: Black S −2, the other nine at 0.
- D2 change: `inventoryItem.tracked = false` on all 30. Barcodes untouched.
- D2 extended on 18 Oct at `cowork/live-site-checks`' request (QUESTIONS Q5):
  - also untrack the 420 variants on the 14 draft T-shirt week tees (tag `t-shirt-week`, 30 variants each, all tracked);
  - add the tag `made-to-order` to all 17 T-Shirts products. None has it today. The theme switches the product page from "IN STOCK / leaves tomorrow" to its made-to-order line only when that tag is present.
- Correction: tee product schema is already InStock, not PreOrder (`cowork/live-site-checks` Rich Results Test, 16 Oct).
- Approval: pending (D1 = QUESTIONS Q7, D2 = Q5)
- Admin read-back: pending
- Metric:
  - no negative tee stock in Admin;
  - live tee pages no longer show "IN STOCK", "Ordered now — leaves tomorrow" or "1 LEFT";
  - Merchant Center availability for tees.

## E. Target gender

- Baseline: no target gender on any product, and no `shopify.target-gender` definition. Nothing in titles, tags, categories or size charts marks an item as women's or men's, although the catalogue covers both (confirmed 16 Oct).
- Suggested list for George to correct. Not to be written until he has corrected it, and never default everything to male.

| Product | Sizing on record | Suggested | Reason |
|---|---|---|---|
| BLACK / GREY / PINK CONVICT HOODIE | XS–XL; chart covers heights ~5'4" and under to ~6'2" and up | Unisex | Height range spans both; baggy |
| BLACK / GREY / PINK CONVICT SWEATS | XS–XL; waist 76.2–96.5cm | Unisex | Baggy, elastic waist |
| BLACK / GREY / PINK SET | Component sizes | Same as components | Hoodie plus sweats |
| CHARCOAL CELLBLOCK CREWNECK | XS–XL; chest 109.2cm at XS | Unisex | Relaxed |
| CHARCOAL CELLBLOCK SHORTS | XS–XL; fits waist 71.1cm at XS | Unisex | Relaxed, drawstring |
| CELLBLOCK SET | Component sizes | Same as components | Co-ord |
| BLUE / GREY WASH YARD JEANS, OG JEANS | XS–XL; chart copied from sweats (Finding 3) | George to say | Waist run reads as men's, but the chart isn't reliable |
| BLUE / GREY WASH YARD JORTS | XS–XL; waist 76.2–96.5cm | George to say | Same waist run as the jeans |
| HYDROCUFF WINDBREAKER | XS–XL; chest 110–134cm | Unisex | No gendered cut |
| DOUBLE-AGENT PUFFA | XS–XL; no chart | Unisex | No gendered cut |
| CROOKS EXPRESS / CRX GARMS / CRXST★RZ | XS–XL; one shared tee chart | Unisex | Print-on-demand blank |
| BLACK/BLUE and WHITE/RED MOTIONTEC SOCKS | Pack sizes only | Unisex | No foot sizing |
| MAJOR LEAGUE CROOKS CAP (CREAM) | One size | Unisex | One size |

- Approval: pending George's corrections
- Metric: Merchant Center "missing gender" item issues.

## F. Double-Agent Puffa colour

- Baseline (unchanged on 18 Oct): no `shopify.color-pattern` on the Puffa. Its own image alt says "the black shell shows metallic silver" when heat is applied.
- Change: set `shopify.color-pattern` to George's one-word base colour. Black (`gid://shopify/Metaobject/450303197527`) already exists if that's his answer.
- Approval: pending George's colour
- Metric: Merchant Center "missing color" item issue for the Puffa.

## G. HydroCuff and Puffa descriptions

- Blocked: workstreams/05-reactive-drafts.md isn't reachable from this session, and George's two wording calls are still open.
- Live baseline, HydroCuff: "HydroCuff windbreaker, engineered to react on contact. Water-activated cuff pattern emerges in the rain."
- Live baseline, Puffa: "Heat-reactive puffer with signature Crooks handcuff embroidery to the chest and hood. Changes appearance with temperature, finished with a padded streetwear fit and concealed hand pockets." The stored HTML also contains a stray `<meta charset="utf-8">` inside the paragraph, which the rewrite should drop.

## H. Shipping weights

On 16 Oct, 13 products were at 0. Two were set from outside this session on 17 Oct: CHARCOAL CELLBLOCK CREWNECK went from 0 to 800g at 20:42 BST, and PINK CONVICT SWEATS from 0 to 700g at 20:43 BST. That leaves 11, which matches the brief.

| Product | Variants | Proposed | Basis |
|---|---|---|---|
| BLACK SET | 25 | 1,700g | Hoodie 900g plus sweats 800g |
| GREY SET | 25 | 1,700g | Hoodie 900g plus sweats 800g |
| PINK SET | 50 | 1,600g | Hoodie 900g plus sweats 700g (as set on 17 Oct) |
| CELLBLOCK SET | 25 | 1,450g | Crewneck 800g plus shorts 650g |
| CRX GARMS T-SHIRT | 10 | 250g | Same as CROOKS EXPRESS TEE |
| CRXST★RZ T-SHIRT | 10 | 250g | Same as CROOKS EXPRESS TEE |
| BLUE WASH YARD JORTS | 5 | needs George | No comparable product |
| GREY WASH YARD JORTS | 5 | needs George | No comparable product |
| DOUBLE-AGENT PUFFA | 5 | needs George | No comparable product |
| MAJOR LEAGUE CROOKS CAP (CREAM) | 1 | needs George | No comparable product |
| WHITE/RED MOTIONTEC SOCKS | 4 (1/3/6/12) | needs George, per pack | BLACK/BLUE socks show 20g on all four pack sizes, so they aren't a usable reference |

Also for George to check:
- PINK CONVICT SWEATS at 700g against 800g on the Black and Grey sweats.
- BLACK/BLUE socks at 20g on the 12-pack.

- Approval: pending (derived rows can be approved as a block)
- Metric: Click & Drop label weights; Merchant Center shipping-weight issues.

## I. ReStock "preorder" selling plan

- Baseline (unchanged on 18 Oct): ReStock group "preorder" is attached to CROOKS EXPRESS TEE, CRX GARMS T-SHIRT, CRXST★RZ T-SHIRT and PINK CONVICT SWEATS.
- PINK CONVICT SWEATS also carries the clive-preorders group "Pre-order: expected to dispatch by 31 October". Variants M, L and XL are on CONTINUE.
- `requiresSellingPlan` is false on all four.
- Proposed route: remove the plan inside the ReStock app, not by uninstalling.
- Approval: pending (tees only, or the Pink Sweats too)
- Metric: the checkout "recurring/deferred purchase" notice disappears on tee orders.

## J. Photos / K. Bag-label barcodes

Waiting on files. This session has read no barcode values and changed none.
