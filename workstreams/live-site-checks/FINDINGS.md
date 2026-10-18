# Findings

Live theme throughout: **CROOKSLDN — SEO round 2 (from live 16 Oct)**, `gid://shopify/OnlineStoreTheme/207329132887` (MAIN, last edited 16 Oct 13:33 UTC). Measured 16 Oct 2026 20:28–21:05 BST, re-checked 18 Oct 16:35 BST. Full report with every number: [`artifacts/live-site-checks-report-2026-10-16.md`](artifacts/live-site-checks-report-2026-10-16.md).

## Finding 1 — Print-on-demand tees say "IN STOCK" and "leaves tomorrow", and show false "1 LEFT"

**Finding:**
All three live tees are print on demand, but the PDP treats them as stocked goods:
- CRX GARMS T-SHIRT has zero stock in every variant and shows **IN STOCK** and **"> Ordered now — leaves tomorrow"**.
- CROOKS EXPRESS TEE White / XS (stock −4) shows the same.
- CROOKS EXPRESS TEE White / XL (stock 1) shows **"1 LEFT IN SIZE White / XL"**, which is false scarcity on a made-to-order item.
- Product schema marks all 30 tee variants `InStock` with `handlingTime` 0–2 days. They are not `PreOrder`: tees have no selling plans, and PreOrder only fires for the CROOKS Operations pre-order plan.
- The 14 draft T-shirt week tees are set up identically and will publish with the same lines.

**Evidence:**
- Admin API, 18 Oct, on `crooks-express-t-shirt`, `crx-garms-t-shirt` and `crxst-rz-t-shirt`:
  - `tracksInventory: true` and `inventoryPolicy: CONTINUE` on every variant.
  - Quantities 0 or negative except the EXPRESS variants.
  - Tags `black, cotton, tee, white`. None tagged `made-to-order`.
- Draft tees: 14 products tagged `t-shirt-week`, same setup.
- Code:
  - Live `sections/crooks-exhibit-record.liquid`: the stock line prints `label_low` whenever `inventory_quantity` is 1–3, regardless of `inventory_policy`. The made-to-order line is gated on the product tag set in `templates/product.json` (`made_to_order_tag: "made-to-order"`).
  - `snippets/crooks-schema-offer-state.liquid` and `crooks-schema-shipping.liquid` produce the InStock / 0–2 day schema.
- Screenshots: `artifacts/screenshots/10-…`, `11-…`, `12-…`.

**Why it matters:**
Commercial: a shopper told "leaves tomorrow" on a printed-to-order tee gets a late parcel. That means complaints and refunds, plus exposure under UK consumer-protection rules on misleading delivery and scarcity claims. It's about to repeat across 14 launches.
SEO/Shopping: merchant-listing handling time is wrong for every tee.

**Confidence:** High.

**Recommended action:**
1. Product data: tag all 17 tees `made-to-order`, and turn off "Track quantity" on POD variants. That removes the 1 LEFT line and the negative stock.
2. Theme editor: set the made-to-order line to the real POD lead time. The current 9–16 days is a theme default, not a CROOKSLDN figure.
3. Theme code: don't print the low-stock line when `inventory_policy == 'continue'`. Set tee `handlingTime` from the POD lead time.

Needs the POD lead time from George.

## Finding 2 — Checkout pre-ticks email marketing consent

**Finding:**
At checkout, "Keep me updated." (`marketing_opt_in`) is ticked by default. "Text me with discounts and latest drops." is unticked.

**Evidence:**
- Live checkout read 16 Oct and again 18 Oct 16:35 BST: `marketing_opt_in` checked, `sms_marketing_opt_in` unchecked.
- Screenshot `artifacts/screenshots/41-checkout-top-preticked-marketing.jpg`.

**Why it matters:**
Pre-ticked boxes aren't valid consent under UK GDPR/PECR. Every email subscriber collected at checkout this way is a compliance risk, and the list feeds Omnisend campaigns.

**Confidence:** High.

**Recommended action:**
Shopify admin → Settings → Checkout → Marketing options: turn off preselecting the email sign-up. George's action; about two minutes.

## Finding 3 — Every page promises UK delivery in 1–2 days; checkout's free service says 2–3

**Finding:**
These all say UK delivery is 1–2 working days:
- shipping, refund and contact policies
- FAQ and its FAQPage schema
- Terms
- PDP custody accordion
- Product schema (`transitTime` 1–2)

Checkout's free default for £30–£79.99 orders is **Tracked 48 — "2 to 3 business days"**, and that's the service the product schema prices at £0. Prices themselves are consistent: Tracked 48 £3, free from £30; Tracked 24 £4.99, free from £80.

Smaller drift:
- "over £30" everywhere, while Shopify's rule is ≥ £30.
- Policy says "standard £3"; FAQ and Terms say "calculated at checkout".
- Same-day dispatch is "where possible" in FAQ/Terms but a flat promise elsewhere.

**Evidence:**
- Admin API `deliveryProfiles` (General profile, UK zone): 4 method definitions, unchanged 18 Oct.
- `shopPolicies` bodies, all updated 16 Oct 14:04–14:06.
- Live checkout at £51 to the shipping-method step: screenshot `42-checkout-shipping-methods-51gbp.jpg`.
- The full 14-place inventory with exact wording is in the report, section 3.

**Why it matters:**
Commercial: most orders land in the gap. GEO/SEO: answer engines and merchant listings quote the 1–2 day figure, and Merchant Center shipping settings should match what the site and checkout say.

**Confidence:** High.

**Recommended action:**
One wording everywhere: Tracked 48 = 2–3 working days, Tracked 24 = 1–2. Change the schema `transitTime` to match. Proposed copy and an owner for each place are in the report, section 3.

## Finding 4 — Homepage fails Core Web Vitals on mobile (INP), and Mida is the heaviest script on every page

**Finding:**
Real-user data (CrUX, 28 days) for the homepage on mobile: **INP 228 ms → Failed**. LCP 1.3 s and CLS 0 pass. The origin passes on mobile (INP 155 ms) and desktop. Other URLs have too little traffic for URL-level data.

In the lab, the top main-thread script on all five pages is Mida's session recorder, `recorder.msr.js` (Shopify app extension, rrweb), at 350–590 ms on mobile. Shopify Forms' `index.js` is 261.7 KiB on every page, with 244 KiB unused on the homepage. Omnisend loads its own forms stack alongside it. Judge.me and Orderify are negligible.

**Evidence:**
- PageSpeed reports (persist):
  - home https://pagespeed.web.dev/analysis/https-crooksldn-com/dinaybwpm0
  - PDP https://pagespeed.web.dev/analysis/https-crooksldn-com-products-convict-hoodie-1/b0ijxs3xgz
  - sweats https://pagespeed.web.dev/analysis/https-crooksldn-com-collections-sweats/gczfywqfx6
  - tracksuits https://pagespeed.web.dev/analysis/https-crooksldn-com-collections-tracksuits/xyt4yv49i0
  - outerwear https://pagespeed.web.dev/analysis/https-crooksldn-com-collections-outerwear/6vgae8q0ee
- Screenshots `01-…` to `04-…`.
- In-browser resource timing on the PDP: Mida pings `ping.mida-app.io/sessions/*` from 0.6 s onwards.

**Why it matters:**
INP is a ranking signal and the homepage carries most branded traffic. It's the only failing field metric on the site.

**Confidence:**
High on the measurements. Medium that Mida is the main INP cause: lab TBT is low (40 ms), and INP comes from real interactions, which the lab doesn't exercise.

**Recommended action:**
1. Sample Mida recording or exclude the homepage.
2. Scope the Shopify Forms app embed to pages that use it, or remove it if Omnisend owns signup.
3. Re-check homepage INP in CrUX 28 days after the change.

This is the **baseline ("before") measurement** for any performance workstream.

## Finding 5 — Mobile popup covers the whole screen 3.7 s after load; the fix is already staged but not live

**Finding:**
At 390 × 844 on the live homepage:
- The Getaway popup opens at 3.72 s (3 s timer after DOMContentLoaded at 0.72 s).
- It covers 100% of the screen (390 × 844) and locks scroll.
- Closing with × spends nothing, so it returns on every homepage load.

The held, unpublished theme **"CROOKSLDN — Claude P1 fixes (copy of live 16 Oct)"** (`gid://shopify/OnlineStoreTheme/207340142935`) already contains a rebuilt `snippets/crack-the-cuffs.liquid`:
- never sooner than 10 s, then opens on half-page scroll, a return visit, or exit intent
- phones get a non-modal bottom sheet capped at 40vh
- × quiets it for the session
- `ctc_*` customer events for measurement

Its comment cites "owner decision 16 Oct 2026; spec in seo/workstreams/09-performance.md, section B".

**Evidence:**
- Live measurement 16 Oct: screenshots `50-…`, `51-…`.
- Live code `snippets/crack-the-cuffs.liquid`: `DELAY = 3000`; on ≤ 749 px the sheet is full height.
- Checksum diff of all 499 files, held theme vs live, 18 Oct: only `snippets/crack-the-cuffs.liquid` and `snippets/crooks-schema-site.liquid` differ.

**Why it matters:**
Google treats a full-screen interstitial on a mobile landing page as a page-experience negative. It also sits in Lighthouse's final frame (homepage mobile Speed Index 9.5 s).

**Confidence:** High.

**Recommended action:**
None from this workstream. Ship the staged fix when George lifts the hold on "Claude P1 fixes". Use this workstream's 16 Oct numbers as the before-state.

## Finding 6 — The held theme also changes Organization schema (overlap note)

**Finding:**
The held theme's `snippets/crooks-schema-site.liquid` differs from live:
- adds `founder` (George Hinxman), `identifier` (Companies House 16606021) and `address.addressCountry` GB
- restricts `sameAs` to instagram.com/crooksldn and tiktok.com/@crooksldn
- adds "Crooks LDN" to `alternateName`
- changes the fallback description to "independent British streetwear brand…"

Live Organization is valid but uses the older description ("CROOKSLDN (Crooks London) is a streetwear label…").

**Evidence:** Admin API file read of both themes, 18 Oct. Rich Results Test on the homepage: Organization valid.

**Why it matters:**
Entity/GEO work is staged in the same held theme as the popup fix. None of this workstream's findings conflict with it.

**Confidence:** High.

**Recommended action:**
Whoever owns the entity/About workstream should know this is staged, not live.

## Finding 7 — Structured data baseline: valid on indexable pages; set pages invalid but noindexed

**Finding:**

| Page | Result |
|---|---|
| Homepage | Organization + Return policy valid |
| Convict hoodie PDP | Product snippets 1, Merchant listings 5, Breadcrumbs, Organization: all valid, non-critical only |
| Tee PDP | Product snippets 1, Merchant listings 10, Breadcrumbs, Organization: all valid |
| /collections/outerwear | CollectionPage (with an ItemList of 2), BreadcrumbList, WebSite, Organization: 0 errors |
| Set PDPs | Print `"size"` twice per variant: Google reports "Unparsable structured data — Duplicate unique property"; validator.schema.org drops the ProductGroup. All four sets carry `seo.hidden = 1` (noindex,nofollow) by design, so there's no search loss today. |

Across all of it: priceCurrency is GBP everywhere; shippingDetails is on every offer; no "Portugal" in visible text or schema (only inside the country-picker JSON); `countryOfOrigin` is absent everywhere.

**Evidence:**
- Rich Results Test:
  - home https://search.google.com/test/rich-results/result?id=Y2SFHIS5_l04zG2tgZyNaQ
  - hoodie …?id=mOhKHa_rE94oTkUULSLXXQ
  - tee …?id=GJGE3gvgywypQPcnYsBmyg
  - set …?id=62iPFBz18DwP_m_CF_BXKg
  - outerwear …?id=3OQYiWEe8pmlvLknHQ5arA
- Screenshots `30-…` to `35-…`.
- Code: `snippets/crooks-schema-product.liquid`, the per-option loop. Set options are "X (Size)" and "Y (Size)"; both contain "size", so `size` is printed twice.

**Why it matters:**
It confirms the schema programme is live and valid. The set bug only matters if sets are ever made indexable.

**Confidence:** High.

**Recommended action:**
- Theme code: print `size` once on products with two size options.
- Keep `countryOfOrigin` absent. It's driven by `crooks.origin`, which also renders in the PDP "Origin" row, and the brand rule is no manufacturing origin in consumer copy. If Merchant Center needs origin, set it in the feed (03-merchant-feed).

## Finding 8 — Pre-order notice links to a cancellation policy that doesn't exist

**Finding:**
With a pre-order in the bag, both cart and checkout show Shopify's deferred-purchase consent text: "…I agree to the cancellation policy and authorize you to charge my payment method…". No cancellation or subscription policy is set. `/policies/subscription-policy` returns 404, and the cart's "cancellation policy" text links nowhere. It doesn't appear for tees, which have no selling plans.

**Evidence:**
- Cart and checkout with PINK CONVICT SWEATS XL (pre-order, "expected to dispatch by 31 October"): screenshots `40-…`, `41-…`.
- Admin API `shopPolicies` has no subscription/cancellation policy.

**Why it matters:**
Shoppers are asked to agree to a policy they can't read. That's a consumer-law and chargeback risk on every pre-order.

**Confidence:** High.

**Recommended action:**
Shopify settings → Policies: add a short cancellation policy for pre-orders (cancel any time before dispatch for a full refund). Needs George's approval of the wording.

## Finding 9 — Mobile lab LCP of 9.5–10.2 s on PDP/collections comes from render-blocking CSS and text-render delay

**Finding:**

| Page | Mobile lab score | Mobile lab LCP |
|---|---|---|
| PDP | 59 | 10.2 s |
| Tracksuits | 61 | 9.5 s |
| Outerwear | 60 | 9.8 s |
| Sweats | 82 | 4.2 s |
| Home | 75 | 4.2 s |

- Render-blocking CSS costs 560–740 ms: `compiled_assets/styles.css` 46.5 KiB, `base.css` 15.1, `crooks.css` 11.2, `crx-mono.css`, accelerated-checkout CSS, plus Partner Hub's `creator-gift.css`.
- The LCP element on tracksuits/outerwear/sweats is the collection intro `<p>`, with render delay 0.95–2.4 s. That points at web-font blocking.
- Homepage hero `IMG_2393.jpg` has an 810 ms load delay, and image delivery could save 263 KiB.

Field LCP is fine (origin 1.1 s), so this is a lab/low-end-device issue rather than a failing metric.

**Evidence:** The PageSpeed reports above. Report section 1.

**Why it matters:**
It's the headroom on slow phones, and the cheapest wins: critical CSS, `font-display: swap`, hero `fetchpriority`.

**Confidence:** Medium-High.

**Recommended action:** For the theme/performance workstream. Not urgent while field LCP passes.

## Finding 10 — The set-panel line "Free UK Tracked 24 included" reads as applying to the £60 item

**Finding:**
On hoodie and sweats PDPs, the "Cop the full fit" panel shows "Free UK Tracked 24 included" directly under the £60 price, before any set price is shown. It's true for every set total (£85–£110 is over £80), but not for the item on the page.

**Evidence:**
- Screenshot `20-pdp-hoodie-set-panel-free-tracked24-line.jpg`.
- `templates/product.json` → `set_shipping_text`.

**Why it matters:**
It's a misleading shipping claim on the highest-traffic product pages.

**Confidence:** High.

**Recommended action:**
Theme editor: change it to "The set ships free by Tracked 24 (orders £80+)", or show it only after the set price.
