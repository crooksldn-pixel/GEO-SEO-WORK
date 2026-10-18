# 07 — Live site checks (crooksldn.com)

Run: Fri 16 Oct 2026, 20:28–21:05 BST. Research only.
Re-checked Sun 18 Oct 2026 via Admin API and a live checkout read: live theme not edited since 16 Oct 13:33 UTC; tee inventory setup, UK rates, policies and the pre-ticked checkout box all unchanged. Findings below still hold.
Live theme confirmed via Admin API: **CROOKSLDN — SEO round 2 (from live 16 Oct)** (`role: MAIN`). "Claude P1 fixes" was not previewed or touched.

**Nothing in Shopify, the theme, apps or Merchant Center was changed.** Store reads were read-only Admin API queries.
Browser side effects, for the record:
- PageSpeed runs in your Chrome; Chrome then stopped responding, so the rest ran in the Claude built-in browser.
- Cart/checkout used the cart already in that browser (1 × PINK CONVICT SWEATS XL, pre-order, £51). Nothing added or removed. Checkout went to the shipping-method step only. I typed the brand's published returns address (Bourne End Business Park, Bourne End, SL8 5AS) to get rates, then cleared it; the postcode may still sit in that abandoned checkout.
- To see the popup as a first-time visitor I removed `crooksldn_ctc_seen` from that browser's localStorage, loaded the homepage, closed the popup with ×, and set the key back to `1`.

---

## Issue register

P0 = broken now · P1 = misleading or legal exposure, fix this week · P2 = real problem, fix this sprint · P3 = improvement · P4 = note

No P0 found.

| ID | P | Issue | Evidence | Owner |
|---|---|---|---|---|
| 1 | **P1** | Print-on-demand tees tell shoppers they are in stock and leave tomorrow, and show false "1 LEFT" scarcity. | All 3 live tees: `inventoryPolicy: CONTINUE`, tracked stock at 0 or negative (CRX GARMS all 0; CRXST★RZ Black/S −2; EXPRESS White/XS −4, White/M −4). PDP shows **IN STOCK** + **"> Ordered now — leaves tomorrow"** on CRX GARMS Black/M (0 stock) and EXPRESS White/XS (−4). EXPRESS White/XL (qty 1) shows **"1 LEFT IN SIZE White / XL"**. Tees aren't tagged `made-to-order`, so the in-stock/dispatch lines render. Schema says handling 0–2 days. Shots 10–12. | **Product data** (tag tees `made-to-order`; turn off "Track quantity" on POD variants). **Theme editor** (made-to-order line = your real POD lead time). **Theme code** (no low-stock line when a variant sells on `continue`; tee `handlingTime` from the same lead time). |
| 2 | **P1** | Checkout pre-ticks email marketing consent. | "Keep me updated." is ticked by default at checkout (SMS box is unticked). Pre-ticked boxes aren't valid consent under UK GDPR/PECR. Shot 41. | **Shopify settings** → Checkout → Marketing options: turn preselection off. |
| 3 | P2 | Delivery-time promise doesn't match checkout. | Policy, refund policy, contact policy, FAQ (+ FAQPage schema), Terms, PDP custody step and Product schema (`transitTime 1–2`) all say UK **1–2 working days**. Checkout labels the free service **Tracked 48 "2 to 3 business days"**. That's the default for every £30–£79.99 order and the rate the schema prices. Shot 42. | **Theme code** (schema transit), **theme editor** (FAQ, PDP custody block), **Shopify settings → Policies** (shipping, refund, contact). |
| 4 | P2 | Homepage fails Core Web Vitals on mobile (real users). | CrUX URL-level mobile: **INP 228 ms** (needs improvement; good ≤ 200). LCP 1.3 s and CLS 0 pass. Origin passes (INP 155 ms). Heaviest script on every page is **Mida's session recorder** (`recorder.msr.js`, 350–590 ms main thread in mobile lab). Homepage also flags forced reflow. | **Apps** (Mida: sample sessions / exclude homepage, then re-measure). **Theme dev** (forced reflow on homepage). |
| 5 | P2 | Mobile popup is a full-screen takeover 3 s after load, and × doesn't stop it coming back. | At 390 × 844: DOMContentLoaded 0.72 s → popup at **3.72 s**, overlay **390 × 844 (100% of screen)**, page scroll locked. Code: 3,000 ms timer after DOMContentLoaded; waits for the cookie banner first (max 30 s). Only NOT NOW (14-day snooze) or a win suppresses it. A bare × spends nothing, so it returns on every homepage visit. It's also in Lighthouse's final mobile frame (Speed Index 9.5 s). Shots 50, 51, 02. | **Fix already staged, not live:** the held "Claude P1 fixes" theme's `snippets/crack-the-cuffs.liquid` (from the 09-performance workstream, owner decision 16 Oct) has a 10 s minimum, a scroll/return-visit/exit-intent trigger, a ≤ 40% bottom sheet on phones, × quiets it for the session, and `ctc_*` customer events. Ships when that theme's hold is lifted. |
| 6 | P2 | Pre-order notice points to a cancellation policy that doesn't exist. | With a pre-order in the cart, cart and checkout show Shopify's "deferred, subscription, or recurring purchase… I agree to the **cancellation policy**" text. No cancellation/subscription policy is set (`/policies/subscription-policy` → 404); the cart's "cancellation policy" text has no link. Not shown on tees (no selling plans). Shots 40, 41. | **Shopify settings → Policies** (add a cancellation policy for pre-orders). |
| 7 | P2 | Shopify Forms ships 262 KiB of JS to every page. | `forms-2625/assets/index.js`: 261.7 KiB transfer, **244.1 KiB unused** on the homepage (mobile lab). Omnisend forms also load on every page (99 KiB), so two signup stacks run side by side. | **Apps** (limit the Forms app embed to pages that carry a Shopify form, or drop it if Omnisend owns signup). |
| 8 | P3 | Mobile lab LCP 9.5–10.2 s on PDP/tracksuits/outerwear (real-user LCP is fine). | Render-blocking CSS 560–740 ms: `compiled_assets/styles.css` 46.5 KiB, `base.css` 15.1, `crooks.css` 11.2, `crx-mono.css` 1.6, accelerated-checkout CSS 2.8, plus `creator-gift.css` from the Partner Hub app. LCP render delay 2.1–2.4 s (collection intro `<p>` on tracksuits/outerwear; hoodie image on PDP). Origin field LCP 1.1 s mobile. | **Theme dev** (critical CSS inline, rest deferred; `font-display: swap` on VT323/CRX Mono; Partner Hub CSS non-blocking). |
| 9 | P3 | Homepage hero image is discovered late and oversized. | LCP = `IMG_2393.jpg`, mobile resource load delay 810 ms. "Improve image delivery" 263 KiB on homepage mobile. | **Theme dev** (`fetchpriority="high"` + preload on the hero; tighter `sizes`/widths). |
| 10 | P3 | Set product schema is invalid (duplicate `size` key). | Each set variant prints `"size": "XS","size": "XS"`. Google: **Unparsable structured data — Duplicate unique property**. validator.schema.org: 1 error, ProductGroup dropped. Sets carry `seo.hidden = 1` (noindex by design), so no search loss today. Shots 32–34. | **Theme code** (`crooks-schema-product.liquid`: emit size once on two-size products). |
| 11 | P3 | "Free UK Tracked 24 included" reads as if the £60 item ships free by Tracked 24. | The line sits in the "Cop the full fit" set panel on hoodie/sweats PDPs, under the £60 price, before any set price shows. It is true for every set total (£85–£110 ≥ £80). Shot 20. | **Theme editor** (product template → set panel shipping line). |
| 12 | P3 | Small wording drift on threshold, price and dispatch. | "over £30" everywhere, but Shopify frees it **at** £30 (≥). FAQ "Below £30 it is calculated at checkout" and Terms "charged at checkout" vs policy "standard £3". Policy calls it "standard"; checkout calls it "Tracked 48". FAQ/Terms say same-day "where possible"; status bar, policy and PDP say it flat. | **Theme editor** (FAQ, status bar, PDP), **Shopify settings → Policies**. |
| 13 | P3 | EXPRESS tee: White selected, black tee shown. | Variant image not set for White. Shot 10. | **Product data**. |
| 14 | P4 | Homepage loads ~360 KiB of Shopify checkout-web chunks. | Mobile lab total-byte-weight: `c1/164ad2e3…js` 184.5 KiB, `c1/6a2fc6d6…js` 90.3, `c1/4b4bc88f…js` 85.0 (homepage total 2,905 KiB). | **Theme dev** (find what triggers checkout assets on the homepage, likely the dynamic-checkout/Shop Pay buttons in the cart drawer). |
| 15 | P4 | Optional schema fields Google lists as missing. | Return policy: `returnFees`, `customerRemorseReturnShippingFeesAmount`, `refundType`. Merchant listings: per-offer `hasMerchantReturnPolicy`, variant `description`. Product snippets: `review`, `aggregateRating`. All non-critical; every item is valid. | **Theme code**, low priority. Only add the return-fee amount if it's fixed (FAQ says "from £2.98"). |
| 16 | P4 | Reviews: Judge.me is installed but the schema comment says it isn't. | Only CROOKS EXPRESS TEE has a review: 1 review, 1.0★. Not emitted in schema today. Don't add `aggregateRating` until there's volume, and never hide genuine reviews. | Note only. |
| 17 | P4 | "Portugal" and `countryOfOrigin`. | "Portugal" appears only inside the country-picker list (localization JSON) on every page. Not in visible text or schema. `countryOfOrigin` appears nowhere: no product has a `crooks.origin` metafield. | Note only. **Leave `crooks.origin` empty.** It renders as the "Origin" row on the PDP, and the brand rule is no manufacturing origin in consumer copy. If Merchant Center wants origin, set it in the feed (03-merchant-feed), not the PDP. |
| 18 | P4 | Housekeeping. | Disabled announcement bar still holds "FREE UK SHIPPING \| 24 HOUR SHIPPING AVAILABLE", which is wrong if re-enabled. Store has 17 themes (Shopify cap 20). | Theme editor / Online Store. |

---

## 1. Core Web Vitals baseline

PageSpeed Insights, run 16 Oct 20:28 BST. Lab = Lighthouse 13.5.0, emulated Moto G Power, slow 4G. The reports stay openable at the links in the evidence index.

### Field data (CrUX, last 28 days)

| URL | Mobile | Desktop |
|---|---|---|
| Homepage (URL level) | **Failed**: LCP 1.3 s · **INP 228 ms** · CLS 0 · FCP 1.1 s · TTFB 0.4 s | Passed: LCP 1.1 s · INP 106 ms · CLS 0 · FCP 0.9 s · TTFB 0.3 s |
| /products/convict-hoodie-1 | Insufficient URL data → origin shown | Insufficient URL data → origin shown |
| /collections/sweats | Insufficient URL data → origin shown | Insufficient URL data → origin shown |
| /collections/tracksuits | Insufficient URL data → origin shown | Insufficient URL data → origin shown |
| /collections/outerwear | Insufficient URL data → origin shown | Insufficient URL data → origin shown |
| **Origin (crooksldn.com)** | Passed: LCP 1.1 s · INP 155 ms · CLS 0 · FCP 0.9 s · TTFB 0.3 s | Passed: LCP 1.0 s · INP 95 ms · CLS 0 · FCP 0.8 s · TTFB 0.3 s |

### Lab data

| URL | Mobile score | Mobile FCP / LCP / TBT / CLS / SI | Mobile LCP element | Desktop score | Desktop LCP / TBT | Desktop LCP element |
|---|---|---|---|---|---|---|
| Homepage | 75 | 2.3 s / 4.2 s / **40 ms** / 0 / 9.5 s | Hero `IMG_2393.jpg` (two people in white tees). Load delay 810 ms, render delay 260 ms | 93 | 0.9 s / 40 ms | Same hero image |
| Convict hoodie PDP | **59** | 4.5 s / **10.2 s** / **90 ms** / 0 / 7.0 s | Hoodie image `crooksldn-black-baggy-fleece-hoodie`. Render delay 2,100 ms | 98 | 1.1 s / 30 ms | Same image |
| /collections/sweats | 82 | 2.2 s / 4.2 s / **0 ms** / 0 / 3.8 s | Intro `<p>` "Heavyweight fleece from CROOKSLDN…". Render delay 950 ms | 98 | 1.1 s / 50 ms | Same `<p>` |
| /collections/tracksuits | 61 | 4.1 s / **9.5 s** / **30 ms** / 0 / 6.5 s | Intro `<p>` "A CROOKSLDN tracksuit is…". Render delay 2,430 ms | 99 | 1.0 s / 40 ms | Product image `IMG-1254.png` |
| /collections/outerwear | 60 | 4.2 s / **9.8 s** / **90 ms** / 0 / 6.7 s | Intro `<p>` "CROOKSLDN outerwear reacts to the weather…". Render delay 2,410 ms | 98 | 1.0 s / 60 ms | HydroCuff windbreaker image |

### Top 3 opportunities (mobile)

| URL | 1 | 2 | 3 |
|---|---|---|---|
| Homepage | Render-blocking requests, ~690 ms | Image delivery, ~263 KiB | Unused JavaScript, ~299 KiB |
| Convict hoodie PDP | Render-blocking requests, ~560 ms | Unused JavaScript, ~346 KiB | Cache lifetimes, ~166 KiB |
| /collections/sweats | Render-blocking requests, ~580 ms | Unused JavaScript, ~299 KiB | Cache lifetimes, ~87 KiB |
| /collections/tracksuits | Render-blocking requests, ~740 ms | Unused JavaScript, ~299 KiB | Cache lifetimes, ~87 KiB |
| /collections/outerwear | Render-blocking requests, ~580 ms | Unused JavaScript, ~299 KiB | Cache lifetimes, ~87 KiB |

Also flagged everywhere: legacy JavaScript (11–17 KiB), forced reflow, network dependency chain. Mobile main-thread work 2.2–2.4 s on homepage, PDP and outerwear.

### Third-party weight

| Script | How it loads | Bytes | Main-thread (mobile lab) | Verdict |
|---|---|---|---|---|
| **Mida** (`recorder.msr.js`, app extension on cdn.shopify.com; posts to `ping.mida-app.io/sessions`, rrweb recorder) | Every page, deferred | ~31 KiB + 3 KiB mida-app.io | **350–590 ms**, the top script on all 5 pages (home 456, PDP 532, sweats 350, tracksuits 426, outerwear 586) | Heaviest by CPU. Prime INP suspect. |
| **Shopify Forms** (`forms-2625/assets/index.js` + loader) | Every page, module | **261.7 KiB** (244.1 KiB unused on home) | 59–78 ms | Heaviest by bytes. |
| **Omnisend** (`omnisnippet1.com`: shopify.js, launcher-v2.js, forms/main.js, monitoring.js; "Soundest" is Omnisend) | Every page | 98–99 KiB (forms/main.js 45 KiB, 35 unused) | 57–101 ms; monitoring.js 115–133 ms total CPU | Moderate. Overlaps Shopify Forms. |
| **Judge.me** (`judgeme-786` loader.js, cart_drawer.js) | Every page | ~5 KiB | Not in top CPU list | Negligible. |
| **Orderify** (`customer-first-focus.b-cdn.net/cffOrderifyLoader_min.js`) | Every page, async | 3 KiB | ~1 ms | Negligible. |

Lighthouse lumps everything served from cdn.shopify.com under "Shopify hosting" (402–490 KiB, 235–324 ms on mobile). Mida and Forms are most of it. In a consented UK session, Meta Pixel (`fbevents.js` + config, ~206 KiB) and gtag also load; neither appeared in the PageSpeed runs.

### Recommendations, in order
1. **Mida:** cut recording to a sample, or exclude the homepage, then watch homepage INP in CrUX. That's the only failing field metric. (Apps.)
2. **Shopify Forms:** confine the app embed to pages with a Shopify form, or remove it if Omnisend owns signup. Saves ~262 KiB per page. (Apps.)
3. **Render-blocking CSS:** inline critical CSS, defer the rest, load Partner Hub's `creator-gift.css` non-blocking, `font-display: swap` on the display fonts. This is what holds mobile FCP at 4+ s on PDP/collections. (Theme dev.)
4. **Homepage hero:** `fetchpriority="high"` + preload; serve smaller widths. (Theme dev.)
5. **Popup:** see issue 5. It also inflates homepage Speed Index.

---

## 2. Rendered structured data

Google Rich Results Test (smartphone crawler) + validator.schema.org. The live HTML was also parsed in the browser.

| Page | Rich Results Test | validator.schema.org | Types present |
|---|---|---|---|
| Homepage | 2 valid: Organization 1, Return policies 1 (3 optional fields missing) | WebSite 0 errors / 0 warnings (Organization nested as publisher) | Organization, WebSite. No breadcrumb (correct for home). |
| /products/convict-hoodie-1 | 8 valid: Product snippets 1, Merchant listings 5, Breadcrumbs 1, Organization 1. Non-critical only. | ProductGroup, BreadcrumbList, WebSite: 0 / 0 | ProductGroup (5 variant Products), BreadcrumbList "Home > Sweats > BLACK CONVICT HOODIE", Organization, WebSite |
| /products/crooks-express-t-shirt (tee) | 13 valid: Product snippets 1, Merchant listings 10, Breadcrumbs 1, Organization 1. Non-critical only. | ProductGroup, BreadcrumbList, WebSite: 0 / 0 | ProductGroup (10 variants), BreadcrumbList "Home > Tees > CROOKS EXPRESS TEE", Organization, WebSite |
| /products/black-set | **URL not available to Google: `noindex` in robots meta** (by design, `seo.hidden = 1`). Breadcrumbs 1, Organization 1, **Unparsable structured data 1** (duplicate `size`). | **1 error**. BreadcrumbList, WebSite valid; **ProductGroup dropped** | ProductGroup (25 variants), BreadcrumbList "Home > Sets > BLACK SET", Organization, WebSite |
| /collections/outerwear | 2 valid: Breadcrumbs 1, Organization 1 | CollectionPage (with ItemList, WebSite, Organization nested), BreadcrumbList: 0 / 0. First fetch said "URL unreachable"; the retry succeeded. | CollectionPage (mainEntity ItemList: HydroCuff Windbreaker, Double-Agent Puffa), BreadcrumbList, Organization, WebSite |

### Field check

| Field | Result |
|---|---|
| Product / ProductGroup | ProductGroup with per-variant Product on all multi-variant PDPs. `variesBy` size (and colour on tees). |
| Offer price | Hoodie 60.00 · tee 25.00 · set 110.00 |
| priceCurrency | **GBP** on every offer |
| availability | Hoodie: 1 InStock, 4 OutOfStock (matches 8 units in one size). **Tees: InStock on every variant of all three tees** (30 of 30), including 0 and negative stock. **Not PreOrder**: tees have no selling plans, and PreOrder only fires for the CROOKS Operations pre-order plan. Set: 5 InStock, 20 OutOfStock. |
| shippingDetails | On every GBP offer: GB; rate £3.00 under £30, £0.00 from £30 (Tracked 48); handlingTime 0–2 days; transitTime 1–2 days. Tee offers carry £3.00 because each tee is £25. |
| Organization | Present on every page: legal name, logo, Brand, sameAs (Instagram, TikTok), contactPoint, MerchantReturnPolicy (14 days, by mail, change-of-mind fees, defects free). |
| WebSite | Present on every page, with SearchAction. |
| CollectionPage / ItemList | Present on /collections/outerwear (ItemList, 2 items). |
| BreadcrumbList | All PDPs and the collection. 3 levels on PDPs. |
| "Portugal" | Not in visible text or schema on any of the 5 pages; only in the country-picker list. |
| countryOfOrigin | Not present anywhere. |

---

## 3. Shipping-promise parity

Actual Shopify rates (Settings → Shipping, General profile, UK zone):
- Tracked 48: £3.00, or **free when order ≥ £30**.
- Tracked 24: £4.99, or **free when order ≥ £80**.

So the £30 and £80 tiers both exist in settings. Policy and FAQ match the **price** rules. The conflicts are delivery time, dispatch, and wording.

### Every place a promise appears

| # | Place | Exact wording (live) | Owner |
|---|---|---|---|
| 1 | Status bar, site-wide, rotating | "FREE UK SHIPPING OVER £30 // ORDER BY 18:00 FOR SAME-DAY DISPATCH" | Theme editor (header group → Crooks status bar) |
| 2 | Announcement bar (**disabled**, not live) | "FREE UK SHIPPING \| 24 HOUR SHIPPING AVAILABLE" | Theme editor |
| 3 | Carriage bar: PDP top, cart, homepage | "[amount] to free Tracked 48" / "[amount] to free Tracked 24" / "Free Tracked 24 — unlocked". Tiers "TRACKED 48 FREE" (£30), "TRACKED 24 FREE" (£80). Seen live at £51 cart: "£29.00 to free Tracked 24". | Theme editor (crooks-cart-progress settings) |
| 4 | PDP buy box | "IN STOCK" or "[n] LEFT IN SIZE [size]", then "> Ordered now — leaves today / tomorrow / Monday" (18:00 cutoff, Mon–Sat). Static line in markup: "Order before 18:00 and it ships today (Mon–Sat)". Made-to-order alternative exists but no product uses it. | Theme editor (product template) + product tags |
| 5 | PDP set panel | "Free UK Tracked 24 included" | Theme editor (product template, set panel) |
| 6 | PDP "Chain of custody" accordion | "Orders placed before 18:00 are dispatched the same day, Monday to Saturday. After 18:00, the next dispatch day." · "Shipped with Royal Mail Tracked. Free UK shipping over £30, and free Tracked 24 over £80." · "Tracking issued by email. UK 1–2 working days. International 7–14 working days." | Theme editor (custody blocks) |
| 7 | Cart page | "Duties and taxes included. Shipping is calculated at checkout." Pre-order lines: "Pre-order: expected to dispatch by 31 October" + Shopify's deferred-purchase/cancellation-policy notice | Theme locale / Shopify / CROOKS Operations app |
| 8 | Checkout (£51 cart, stopped before payment) | "Tracked 48 — 2 to 3 business days — Tracking number provided — FREE" · "Tracked 24 — 1 to 2 business days — Tracking number provided — £4.99" | Shopify settings (Shipping and delivery) |
| 8a | Checkout under £30 / from £80 (from settings, not run live) | Under £30: Tracked 48 £3.00, Tracked 24 £4.99. From £80: both free. | Shopify settings |
| 9 | Shipping policy | "Free UK shipping over £30, and free Tracked 24 over £80. Under that: standard £3, Tracked 24 £4.99." · "Order before 18:00 (Mon–Sat) and it goes out the same day — after that, the next dispatch day. Limited drops and pre-orders ship on the date shown on the product page." · "UK 1–2 working days, international 7–14." | Shopify settings → Policies |
| 10 | Refund policy | "Free UK shipping over £30 (free Tracked 24 over £80). UK delivery 1–2 working days, international 7–14." | Shopify settings → Policies |
| 11 | Contact policy | "Tracking is emailed once it ships (UK 1–2 working days, international 7–14)." | Shopify settings → Policies |
| 12 | FAQ (+ FAQPage schema, same text) | "Orders placed before 18:00 are dispatched the same day where possible, Monday to Saturday…" · "Once it has left us: 1–2 working days in the UK, 7–14 working days internationally." · "Free on UK orders over £30. Over £80 you get Royal Mail Tracked 24 free. Below £30 it is calculated at checkout before you pay." | Theme editor (page.faq template) |
| 13 | Terms page | "UK shipping is free on orders over £30, and free Royal Mail Tracked 24 over £80. Below £30 it is charged at checkout before you pay. Once dispatched, UK orders arrive in 1–2 working days." · "…dispatched the same day where possible, Monday to Saturday." | Theme editor (page.terms template) |
| 14 | Product schema `shippingDetails` | GB · £3.00 below £30, £0.00 from £30 · handlingTime 0–2 days · transitTime 1–2 days | Theme code (`crooks-schema-product.liquid` / `crooks-schema-shipping.liquid`) |

### Conflicts

| Conflict | Where it disagrees |
|---|---|
| **UK transit time** | 1–2 working days (9, 10, 11, 12, 13, 6, 14) vs checkout Tracked 48 **2–3 business days** (8). Tracked 48 is the free default for £30–£79.99 and the rate the schema prices. |
| **Dispatch for POD tees and pre-orders** | Status bar and PDP promise same-day/next-day for everything (1, 4). Tees are print on demand; pre-orders ship by a date. The policy (9) exempts pre-orders but nothing exempts tees. |
| **Same-day: hedged or absolute** | "where possible" (12, 13) vs flat promise (1, 4, 6, 9). |
| **Threshold wording** | "over £30" everywhere vs Shopify rule **≥ £30**. |
| **Under-£30 price** | "£3" (9) vs "calculated / charged at checkout" (12, 13). |
| **Service name** | "standard" (9) vs "Tracked 48" (3, 8). |
| **Set line** | "Free UK Tracked 24 included" (5) shown under a £60 price; true only for the set total. |

### Proposed single wording

The **POD lead time** below has to come from you. I don't have it, and the theme's default "Ships in 9–16 days" is a placeholder, not your number.

- **Long form** (policies, FAQ, Terms, PDP custody block):
  > UK delivery is free from £30 by Royal Mail Tracked 48 (2–3 working days). Free Tracked 24 (1–2 working days) from £80. Under £30: Tracked 48 £3, Tracked 24 £4.99. In-stock orders placed by 18:00 Mon–Sat leave the same day. T-shirts are printed to order and leave within [POD lead time]. Pre-orders leave on the date shown on the product.
- **Status bar:** "FREE UK DELIVERY FROM £30 // IN-STOCK ORDERS BY 18:00 SHIP SAME DAY"
- **Set panel:** "The set ships free by Tracked 24 (orders £80+)"
- **Schema:** Tracked 48 transit 2–3 days (or 1–3 to cover both services); tee offers' handlingTime = POD lead time.

### Who changes each place

| Place | Owner |
|---|---|
| Status bar, carriage bar labels, PDP buy box lines, set panel line, custody accordion, FAQ, Terms | Theme editor |
| Tee `made-to-order` tag; POD variants not tracked | Product data |
| Shipping, refund and contact policies; add a cancellation policy; checkout marketing preselect off | Shopify settings |
| Rates and service names (only if you rename "standard" ↔ "Tracked 48") | Shopify settings → Shipping |
| Schema transit/handling times; low-stock line on `continue` variants; duplicate `size` on sets | Theme code |

---

## 4. Tee pages — what a customer sees

Viewed Fri 16 Oct ~20:45 BST (after the 18:00 cutoff), live theme.

| Tee / variant | Real state (Admin API) | What the PDP shows | Shot |
|---|---|---|---|
| CROOKS EXPRESS TEE, White / XS | Tracked, qty **−4**, sells on `continue`, POD | "IN STOCK" · "> Ordered now — leaves tomorrow" · Add to bag. Black tee image while White is selected. | 10 |
| CROOKS EXPRESS TEE, White / XL | Tracked, qty 1, `continue`, POD | "**1 LEFT IN SIZE White / XL**" · "> Ordered now — leaves tomorrow" | 11 |
| CRX GARMS T-SHIRT, Black / M | Tracked, qty **0** (whole product 0), `continue`, POD | "IN STOCK" · "> Ordered now — leaves tomorrow" | 12 |
| CRXST★RZ T-SHIRT | Tracked; Black/S −2, rest 0; `continue` | Same template and logic. Schema: all 10 InStock. | — |

- **Pre-order notice on tees:** none. Tees have no selling plans, so the pre-order block stays hidden.
- **Recurring-purchase notice on tees:** none.
- That notice appears only in cart and checkout when a pre-order item is in the bag (shots 40, 41).
- 14 T-shirt week tees are in **draft** with the same setup: tracked at 0 on `continue`, tagged `t-shirt-week` but not `made-to-order`. They'll publish with the same IN STOCK / leaves-today lines unless that's changed first.

---

## 5. Mobile popup at 390 px (live theme)

| Measure | Result |
|---|---|
| Opens immediately? | No. 3.0 s after DOMContentLoaded. DCL 0.72 s, popup in DOM at **3.72 s** from navigation start. At 3.50 s the page was still visible (shot 50). |
| Covers the screen? | **Yes, all of it.** Overlay 390 × 844 with a 90% black backdrop; the sheet is full height on ≤ 749 px. Page scroll locked; rest of the page `aria-hidden`. Close × top-left, RUN IT / NOT NOW centred (shot 51). |
| Offer copy | "CROOKSLDN: THE GETAWAY — Crack the cuffs. 10% off your first order — code sent by text. Attempts unlimited." · "One code per player." |
| Where | Homepage only. |
| Cookie banner | Waits until the banner is answered (gives up after 30 s). A UK first visit gets banner first, then popup. |
| How often | × close doesn't suppress, so it returns on every homepage load. NOT NOW snoozes 14 days; a win stops it for good. |
| Lab impact | Appears in Lighthouse's final mobile frame; homepage mobile Speed Index 9.5 s. |
| Recommendation | Already built and staged: the held "Claude P1 fixes" theme replaces this with a 10 s minimum plus an engagement trigger, a ≤ 40% non-modal bottom sheet on phones, and × quieting it for the session (09-performance workstream). Publish it when the hold lifts. Compare `ctc_shown` / `ctc_run` / signups per 1,000 homepage sessions before and after. |

---

## Evidence index

### PageSpeed reports (mobile and desktop in each; add `?form_factor=desktop`)
- Home: https://pagespeed.web.dev/analysis/https-crooksldn-com/dinaybwpm0
- Convict hoodie: https://pagespeed.web.dev/analysis/https-crooksldn-com-products-convict-hoodie-1/b0ijxs3xgz
- Sweats: https://pagespeed.web.dev/analysis/https-crooksldn-com-collections-sweats/gczfywqfx6
- Tracksuits: https://pagespeed.web.dev/analysis/https-crooksldn-com-collections-tracksuits/xyt4yv49i0
- Outerwear: https://pagespeed.web.dev/analysis/https-crooksldn-com-collections-outerwear/6vgae8q0ee

### Rich Results Test
- Home: https://search.google.com/test/rich-results/result?id=Y2SFHIS5_l04zG2tgZyNaQ
- Convict hoodie: https://search.google.com/test/rich-results/result?id=mOhKHa_rE94oTkUULSLXXQ
- Tee: https://search.google.com/test/rich-results/result?id=GJGE3gvgywypQPcnYsBmyg
- Black set: https://search.google.com/test/rich-results/result?id=62iPFBz18DwP_m_CF_BXKg
- Outerwear: https://search.google.com/test/rich-results/result?id=3OQYiWEe8pmlvLknHQ5arA

### Screenshots (`screenshots/`)

| File | Shows |
|---|---|
| 01-psi-home-mobile-field.png | Homepage CrUX mobile, failed on INP 228 ms |
| 02-psi-home-mobile-lab.jpg | Homepage mobile lab 75; popup in final frame |
| 03-psi-home-desktop-field.jpg | Homepage CrUX desktop, passed |
| 04-psi-origin-mobile-field.png | Origin CrUX mobile, passed |
| 10-tee-express-white-xs-instock-leaves-tomorrow.jpg | Express tee White/XS |
| 11-tee-express-white-xl-1-left.png | "1 LEFT" on a POD variant |
| 12-tee-crx-garms-zero-stock-shows-in-stock.jpg | CRX Garms at 0 stock shows IN STOCK |
| 20-pdp-hoodie-set-panel-free-tracked24-line.jpg | Set panel line on the £60 hoodie |
| 30-rrt-convict-hoodie-summary.jpg | RRT hoodie |
| 31-rrt-tee-express-summary.jpg | RRT tee |
| 32-rrt-black-set-noindex.jpg | RRT set, noindex |
| 33-rrt-black-set-duplicate-size.jpg | RRT set, duplicate `size` |
| 34-schemaorg-black-set-productgroup-dropped.jpg | Validator, set |
| 35-schemaorg-home-website-org.jpg | Validator, home |
| 40-cart-progress-and-deferred-purchase-notice.jpg | Cart |
| 41-checkout-top-preticked-marketing.jpg | Checkout, pre-ticked marketing box |
| 42-checkout-shipping-methods-51gbp.jpg | Checkout shipping methods at £51 |
| 50-home-390px-at-3.5s-before-popup.jpg | Homepage at 390 px, before the popup |
| 51-home-390px-popup-fullscreen-at-3.7s.jpg | Popup full-screen at 390 px |

### Store reads (Admin API, read-only)
- Shop policies, delivery profile rates, active products (inventory policy and quantities, selling plans, `seo.hidden`), theme list.
- Live theme files: `crooks-schema-product`, `crooks-schema-shipping`, `crooks-schema-offer-state`, `crooks-schema-site`, `crooks-exhibit-record`, `crooks-status-bar`, `crack-the-cuffs`, `header-group.json`, `product.json`, `page.faq.json`.
