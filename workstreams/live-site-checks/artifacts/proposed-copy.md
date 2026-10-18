# Shipping promise and pre-order cancellation policy — approved copy and where each piece stands

**Approved** by owner decisions #1, #3 and #4, 18 Oct 2026, 17:03 UTC. This branch's `ANSWERS.md` records Q6 and Q7 as YES, with the Q1/Q2 answers and the "estimated, not guaranteed" line added.

Facts used:
- **Tees:** printed to order and dispatched within **2–3 working days**. Never same-day or next-day.
- **UK delivery after dispatch:** Tracked 24 typically 1–2 working days, Tracked 48 typically 2–3. These are **estimated delivery aims, not guaranteed dates**, and delivery can occasionally take longer.
- **Prices**, from Shopify delivery settings: Tracked 48 £3, free from £30; Tracked 24 £4.99, free from £80.
- **No manufacturing origin and no "London-based"** anywhere.

**Live status** checked 18 Oct 2026, 20:15 BST, against the new live theme "CROOKSLDN — live 18 Oct + evening fixes" (`207475147095`, published ~18:58 UTC) and Shopify policies.

| # | Place | Owner | Status 18 Oct 20:15 |
|---|---|---|---|
| A1 | Status bar | theme-editor | **Changed live, differently.** "FREE UK DELIVERY OVER £30" everywhere. "ORDER BY 6PM — DISPATCHED TODAY" on product pages only, suppressed on products tagged `tee`. "FREE SIZE SWAPS WITHIN 14 DAYS" on browse pages. Meets the tee rule. "over £30" vs Shopify's "from £30" is cosmetic and left alone. |
| A3 | PDP made-to-order line | theme-editor | **LIVE.** `made_to_order_tag` = `tee`, text "Printed to order. Dispatched within 2–3 working days." The same-day dispatch line no longer renders on tees. |
| A3b | PDP stock line on tees | theme code | **Open.** Still "IN STOCK" once a size is chosen. Owner decision #2 says tees stop showing "IN STOCK". `label_in_stock` is one setting for every product, so tees need a code exception (`assets/crooks-record.js` + `sections/crooks-exhibit-record.liquid`). |
| A4 | PDP set-panel line | theme-editor | **Open.** Still "Free UK Tracked 24 included". Proposed: "The set ships free by Tracked 24". |
| A5 | PDP custody blocks (`templates/product.json`) | theme-editor | **LIVE.** s1 carries the tee 2–3 day exception; s3 carries the Tracked 24/48 aims and the "not guaranteed" line. s2 still says "over £30 … over £80", which is cosmetic. |
| A6 | FAQ (`templates/page.faq.json`, plus FAQPage schema) | theme-editor | **Open, unchanged since 16 Oct.** Still "1–2 working days in the UK" and same-day dispatch with no tee exception. Text below. |
| A7 | Terms page (`templates/page.terms.json`) | theme-editor | **Open, unchanged since 16 Oct.** Text below. |
| A8–A10 | Shipping, refund and contact policies | **this workstream** | **Prepared, waiting on George's typed go.** Exact edits: `policy-edits-ready.md`. |
| A11 | Product schema shipping (`snippets/crooks-schema-shipping.liquid`) | theme code | **Open, unchanged since 16 Oct.** Every offer still says handling 0–2 days and transit 1–2 days, tees included. |
| B | Cancellation policy | **this workstream** | **Prepared, waiting on George's typed go.** `policy-edits-ready.md` §4. |

---

## A6. FAQ (`templates/page.faq.json`), for theme-editor

- **q1 · When will my order be dispatched?** In-stock pieces ordered by 18:00, Monday to Saturday, are dispatched the same day; after 18:00, or on a Sunday, on the next dispatch day. T-shirts are printed to order and dispatched within 2–3 working days. Pre-orders are dispatched on the date shown on the product page.
- **q2 · How long does delivery take?** After dispatch, UK delivery by Royal Mail Tracked 24 typically takes 1–2 working days, and Tracked 48 typically 2–3. International orders typically take 7–14 working days. These are estimated delivery aims, not guaranteed dates, and delivery can occasionally take longer.
- **q3 · How much is shipping?** UK Tracked 48 is free from £30, and Tracked 24 is free from £80. Under that, Tracked 48 is £3 and Tracked 24 is £4.99. You choose at checkout.

## A7. Terms page (`templates/page.terms.json`), for theme-editor

- **01 Carriage:** UK delivery is free from £30 by Royal Mail Tracked 48, and free by Tracked 24 from £80. Below £30, Tracked 48 is £3 and Tracked 24 is £4.99, shown at checkout before you pay. After dispatch, Tracked 24 typically takes 1–2 working days and Tracked 48 typically 2–3; international orders typically take 7–14 working days. These are estimated delivery aims, not guaranteed dates, and delivery can occasionally take longer. Tracking is emailed the moment your parcel leaves us. International customers are responsible for any customs duties or import taxes. These are set by your country, not by us, and we cannot predict or refund them.
- **02 Dispatch:** keep it as it is, and add: "T-shirts are printed to order and dispatched within 2–3 working days."

## A4. Set-panel line (`templates/product.json` → `main` → `set_shipping_text`), for theme-editor

**Now:** Free UK Tracked 24 included → **Proposed:** The set ships free by Tracked 24

## A11. Schema values (`snippets/crooks-schema-shipping.liquid`), for the theme code owner

- **Transit:** 2–3 days. Schema prices Tracked 48, the cheapest UK rate. "Typically" can't be expressed in schema, so use the upper aim.
- **Handling:** in-stock stays 0–2 days (same day by 18:00; a Saturday-evening order leaves Monday). Tees, meaning products tagged `tee`, become 2–3 days. Pre-orders unchanged (delivery time left out).

## B. Pre-order cancellation policy

Final text is in `policy-edits-ready.md` §4.
