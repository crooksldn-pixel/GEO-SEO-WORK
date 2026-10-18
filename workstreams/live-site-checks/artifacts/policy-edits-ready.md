# Shopify policy edits — ready to apply on George's typed go

**Approved:** owner decisions #1, #3 and #4 (18 Oct 2026, 17:03 UTC). This branch's `ANSWERS.md` records Q6 and Q7 as YES.
**State:** PREPARED. Nothing has been written. Each edit waits for George to type **go** in this workstream's Cowork chat.
**Scope:** Shopify admin → Settings → Policies only. The FAQ, Terms page, PDP and status bar are theme files and belong to `cowork/theme-editor` (see `NEXT.md`).

All four were built from the live bodies read at 18 Oct 20:15 BST, which were last updated 16 Oct 14:04–14:06 BST. Every "before" string below matched the live body exactly once. Full bodies are in [`policy-bodies/`](policy-bodies/): `*.before.html` is the live body, which is also the rollback, and `*.after.html` is what gets written.

**Method:** one `shopPolicyUpdate` per policy, in the order below.
1. Re-read the live body first. If it no longer matches `*.before.html`, stop and re-base.
2. Write the change.
3. Read the body back and compare it byte-for-byte with `*.after.html`.
4. Log it in `CHANGES.md`.

**Rollback:** write `*.before.html` back. For the new Cancellation policy, empty its body.

---

## 1. Shipping policy (`SHIPPING_POLICY`)

Three paragraphs change. The opening line, "Heading overseas?", "Lost or damaged?" and "How:" are unchanged.

| | Before (live) | After |
|---|---|---|
| What it costs | Free UK shipping over £30, and free Tracked 24 over £80. Under that: standard £3, Tracked 24 £4.99. Shipping internationally? add your items to cart and your shipping is calculated at checkout based on item weight and location. | UK Royal Mail Tracked 48 is free from £30, and Tracked 24 is free from £80. Under that, Tracked 48 is £3 and Tracked 24 is £4.99. Shipping internationally? Add your items to your bag and the cost is worked out at checkout from weight and destination. |
| When it ships | Order before 18:00 (Mon–Sat) and it goes out the same day — after that, the next dispatch day. Limited drops and pre-orders ship on the date shown on the product page. | In-stock pieces ordered by 18:00, Monday to Saturday, go out the same day; after that, on the next dispatch day. **T-shirts are printed to order and dispatched within 2–3 working days.** Limited drops and pre-orders ship on the date shown on the product page. |
| When it lands | Once dispatched: UK 1–2 working days, international 7–14. Tracking is emailed the moment it leaves us. | After dispatch, UK delivery by Tracked 24 typically takes 1–2 working days and by Tracked 48 typically 2–3. International orders typically take 7–14 working days. **These are estimated delivery aims, not guaranteed dates, and delivery can occasionally take longer.** Tracking is emailed the moment your parcel leaves us. |

This removes the only same-day dispatch promise outside the theme that covered tees.

## 2. Refund policy (`REFUND_POLICY`)

The "Shipping:" line is replaced, and one "Pre-orders:" line is added after it. Nothing else changes.

- **Before:** Shipping: Free UK shipping over £30 (free Tracked 24 over £80). UK delivery 1–2 working days, international 7–14. Tracking sent by email.
- **After:**
  - Shipping: Free UK Tracked 48 from £30, free Tracked 24 from £80. After dispatch, UK delivery typically takes 1–2 working days by Tracked 24 and 2–3 by Tracked 48; international 7–14. These are estimated delivery aims, not guaranteed dates. Tracking sent by email.
  - **Pre-orders:** cancel any time before dispatch for a full refund. Full details are in our Cancellation policy.

## 3. Contact information (`CONTACT_INFORMATION`)

The "Where's my order?" bullet is replaced. Nothing else changes.

- **Before:** • Where's my order? — Tracking is emailed once it ships (UK 1–2 working days, international 7–14). Can't find it? Message us with your order number.
- **After:** • Where's my order? — Tracking is emailed once it ships. After dispatch, UK delivery typically takes 1–2 working days by Tracked 24 or 2–3 by Tracked 48, international 7–14. These are estimates, not guaranteed dates. Can't find it? Message us with your order number.

## 4. Cancellation policy (`SUBSCRIPTION_POLICY`, new)

This is the policy checkout links to as "cancellation policy" when a pre-order is in the bag. It doesn't exist today, so the link is dead and `/policies/subscription-policy` returns 404. The text is §B of `proposed-copy.md`, with owner decision #4's "if the date materially changes" wording:

> **Pre-orders and cancellations**
>
> **How a pre-order works.** You pay the full price when you order. The expected dispatch date is shown on the product page and in your order confirmation. A pre-order ships on its own, separately from anything in stock in the same order.
>
> **Cancelling before dispatch.** You can cancel a pre-order at any time before it's dispatched, for a full refund to your original payment method. Email team@crooksldn.com or DM @crooksldn with your order number. Refunds land within 5–7 days of us confirming the cancellation.
>
> **If the date changes.** If the dispatch date changes materially, we'll email you the new date. You can keep your order or cancel it for a full refund.
>
> **After dispatch.** Once your pre-order has shipped, our normal Refund policy applies: 14 days from delivery for a change of mind, 30 days for a faulty or wrong item.
>
> This doesn't affect your statutory rights.

## Not touched

- **Terms of service** (Shopify policy): it makes no dispatch or delivery promise.
- **Privacy policy:** out of scope.

## Validation after the writes

- Each body read back equals its `*.after.html`.
- The cancellation policy has a public URL. With a pre-order in the bag, the checkout "cancellation policy" link opens it. Read-only check, using the cart already in George's built-in browser if it still holds a pre-order. Nothing is added to the cart.
- The store is behind its password page as of 18 Oct ~20:10 BST, so public URLs can only be checked once it reopens. The Admin API read-back is the proof until then.
