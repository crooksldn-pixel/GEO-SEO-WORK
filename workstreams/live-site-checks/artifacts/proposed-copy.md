# Proposed copy — shipping promise and pre-order cancellation policy

For approval in `QUESTIONS.md` (Q6, Q7). Nothing here is live. Every number matches the store's Shopify delivery settings, read 18 Oct 2026:
- Tracked 48: £3, free from £30.
- Tracked 24: £4.99, free from £80.

Delivery times use what checkout itself shows: Tracked 48 "2 to 3 business days", Tracked 24 "1 to 2 business days". Q2 confirms them.

**One fact is still missing: the tee print-on-demand lead time (Q1).** It appears once, written `{TEE LEAD TIME}`. Nothing else is left open.

Rules followed:
- **"from £30", not "over £30".** Shopify makes it free at exactly £30.
- **Same-day dispatch is promised flatly for in-stock pieces**, as store policy says. Only the Terms page keeps "where possible", because it's the legal fallback.
- **No manufacturing origin and no "London-based"** anywhere.

---

## A. Shipping promise

### A1. Status bar, message 1 (`sections/header-group.json` → `crooks_status_bar` → `m1`)

**Now:** FREE UK SHIPPING OVER £30 // ORDER BY 18:00 FOR SAME-DAY DISPATCH
**Proposed:** FREE UK DELIVERY FROM £30 // IN-STOCK ORDERS BY 18:00 LEAVE SAME DAY

### A2. Carriage bar (`templates/product.json` → `carriage`)

No change. "[amount] to free Tracked 48 / Tracked 24" already matches the settings.

### A3. PDP made-to-order line, used by tees once tagged `made-to-order` (`templates/product.json` → `main` → `made_to_order_text`)

**Now:** Made to order · Ships in 9–16 days (theme default, not a CROOKSLDN figure)
**Proposed:** Printed to order · leaves us within {TEE LEAD TIME} working days

No code change is needed: in `sections/crooks-exhibit-record.liquid`, a made-to-order product never renders the "Ordered now — leaves today/tomorrow" line.

### A4. PDP set panel (`templates/product.json` → `main` → `set_shipping_text`)

**Now:** Free UK Tracked 24 included
**Proposed:** The set ships free by Tracked 24

Every set total (£85–£110) clears £80. The line now names the set, not the £60 garment above it.

### A5. PDP "Chain of custody" blocks (`templates/product.json` and `templates/product.crooks.json` → `s1`, `s2`, `s3`)

- **Logged:** In-stock pieces ordered by 18:00, Monday to Saturday, leave the same day. Later orders leave on the next dispatch day. T-shirts are printed to order and leave within {TEE LEAD TIME} working days. Pre-orders leave on the date shown.
- **Dispatched:** Royal Mail, tracked. Free UK Tracked 48 from £30; free Tracked 24 from £80.
- **In transit:** Tracking by email. UK: Tracked 48 takes 2–3 working days, Tracked 24 takes 1–2. International: 7–14 working days.

### A6. FAQ (`templates/page.faq.json`). The FAQPage schema is built from the same text.

- **q1 · When will my order be dispatched?** In-stock pieces ordered by 18:00, Monday to Saturday, leave the same day. Orders after 18:00, or on a Sunday, leave on the next dispatch day. T-shirts are printed to order and leave within {TEE LEAD TIME} working days. Pre-orders leave on the date shown on the product page.
- **q2 · How long does delivery take?** Once it has left us: Royal Mail Tracked 48 takes 2–3 working days, Tracked 24 takes 1–2. International orders take 7–14 working days.
- **q3 · How much is shipping?** UK Tracked 48 is free from £30, and Tracked 24 is free from £80. Under that, Tracked 48 is £3 and Tracked 24 is £4.99. You choose at checkout.

### A7. Terms, "01 Carriage" (`templates/page.terms.json`)

UK delivery is free from £30 by Royal Mail Tracked 48, and free by Tracked 24 from £80. Below £30, Tracked 48 is £3 and Tracked 24 is £4.99, shown at checkout before you pay. Once dispatched, Tracked 48 orders arrive in 2–3 working days and Tracked 24 orders in 1–2. International orders take 7–14 working days. Tracking is emailed the moment your parcel leaves us. International customers are responsible for any customs duties or import taxes. These are set by your country, not by us, and we cannot predict or refund them.

"02 Dispatch" stays as it is ("…dispatched the same day where possible…"), plus one added sentence: "T-shirts are printed to order and leave within {TEE LEAD TIME} working days."

### A8. Shipping policy (Shopify admin → Settings → Policies → Shipping policy). Replaces the first three paragraphs only.

- **What it costs.** UK Royal Mail Tracked 48 is free from £30, and Tracked 24 is free from £80. Under that, Tracked 48 is £3 and Tracked 24 is £4.99. Shipping internationally? Add your items to your bag and the cost is worked out at checkout from weight and destination.
- **When it ships.** In-stock pieces ordered by 18:00, Monday to Saturday, go out the same day. After that, they go out on the next dispatch day. T-shirts are printed to order and leave within {TEE LEAD TIME} working days. Limited drops and pre-orders ship on the date shown on the product page.
- **When it lands.** Once dispatched: Tracked 48 takes 2–3 working days, Tracked 24 takes 1–2, international 7–14. Tracking is emailed the moment it leaves us.

### A9. Refund policy, "Shipping:" line (Settings → Policies → Refund policy)

**Shipping:** UK delivery is free from £30 (Tracked 48, 2–3 working days), and free by Tracked 24 from £80 (1–2 working days). International 7–14 working days. Tracking sent by email.

### A10. Contact policy, "Where's my order?" (Settings → Policies → Contact information)

• Where's my order? — Tracking is emailed once it ships. UK Tracked 48 takes 2–3 working days, Tracked 24 1–2, international 7–14. Can't find it? Message us with your order number.

### A11. Schema (`snippets/crooks-schema-shipping.liquid`)

- `transitTime` changes from 1–2 to **2–3** days. Schema prices Tracked 48, the cheapest UK rate.
- Tee offers get `handlingTime` 0–{TEE LEAD TIME} days.
- Pre-orders: unchanged (delivery time already left out).

---

## B. Pre-order cancellation policy (Settings → Policies → Cancellation policy)

Checkout already shows pre-order shoppers "I agree to the cancellation policy…", but no such policy exists. This text matches what the pre-order panel tells shoppers ("You pay the full price today. This item ships separately from anything in stock.") and the existing refund policy.

> **Pre-orders and cancellations**
>
> **How a pre-order works.** You pay the full price when you order. The expected dispatch date is shown on the product page and in your order confirmation. A pre-order ships on its own, separately from anything in stock in the same order.
>
> **Cancelling before dispatch.** You can cancel a pre-order at any time before it's dispatched, for a full refund to your original payment method. Email team@crooksldn.com or DM @crooksldn with your order number. Refunds land within 5–7 days of us confirming the cancellation.
>
> **If the date moves.** If the dispatch date changes, we email you the new date. You can keep your order or cancel it for a full refund.
>
> **After dispatch.** Once your pre-order has shipped, our normal Refund Policy applies: 14 days from delivery for a change of mind, 30 days for a faulty or wrong item.
>
> This doesn't affect your statutory rights.
