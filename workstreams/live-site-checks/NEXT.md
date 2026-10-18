# Next

Updated 18 Oct 2026, 20:40 BST, after George's answers ([ANSWERS.md](ANSWERS.md)) and the 18:58 UTC live theme (FINDINGS 12).

## Do next

1. **Policies: this workstream, on George's typed go in this chat.**
   - Write shipping, refund, contact and the new cancellation policy, one at a time, following the method in `artifacts/policy-edits-ready.md`: re-read, write, read back, byte-compare, then log in `CHANGES.md`.
   - Terms of service (Shopify policy) is untouched.
2. **Hand to `cowork/theme-editor`**, the only workstream that changes the live theme. Copy is in `artifacts/proposed-copy.md`:
   - **A6 FAQ** (`templates/page.faq.json`): q1 dispatch, q2 delivery, q3 cost. The FAQPage schema follows the same text.
   - **A7 Terms page** (`templates/page.terms.json`): 01 Carriage, plus one tee sentence in 02 Dispatch.
   - **A4 set-panel line** (`set_shipping_text`): "The set ships free by Tracked 24".
3. **Theme code** (theme-editor, or whoever it hands to):
   - **A3b:** no "IN STOCK" on products tagged `tee` (owner decision #2). `label_in_stock` is shared, so this needs an exception in `assets/crooks-record.js` and `sections/crooks-exhibit-record.liquid`.
   - **A11** (`snippets/crooks-schema-shipping.liquid`): set `transitTime` to 2–3 days, and `handlingTime` to 2–3 days for `tee` products. In-stock handling stays 0–2; pre-orders are unchanged.
   - **Small fixes:** no `label_low` when `inventory_policy == 'continue'`, and print `size` once when a product has two size options (sets).
4. **Hand to `cowork/product-data`:**
   - Turn tracking off on the 4 tees published 17:27 UTC (`og-crook-tee`, `3-clives-tee`, `broadcast-tee`, `evil-clive-tee`). Do the same for the 14 T-shirt Week tees **before** they're published.
   - Confirm every one of those 18 carries the `tee` tag. The made-to-order line and the status-bar exception key off it.
5. **George:** untick "Preselect the sign-up option" (Settings → Checkout → Marketing options). Q3 is still outstanding per `ANSWERS.md`. Also confirm whether the storefront password page is intended, and when it comes off (FINDINGS 11).
6. **When the password page comes off** (read-only):
   - PageSpeed on the homepage, mobile and desktop.
   - The Rich Results Test on the hoodie, tee and outerwear pages.
   - The 390 px popup check on the new teaser bar.
   - Re-open a tee PDP to check that "IN STOCK" and next-day dispatch are gone.
   - Open each policy URL, including `/policies/subscription-policy`.
   - Record everything against the 16 Oct baseline.

## Do not do yet

- **Don't write theme files from this workstream.** theme-editor owns the live theme.
- **Don't preview, publish or port the held "Claude P1 fixes" theme.** It stays held (owner decision). Its popup and Organization fixes are superseded on live by the 18 Oct evening theme.
- **Don't fill `crooks.origin`.** It renders in the PDP "Origin" row, and the brand rule is no manufacturing origin in consumer copy. Merchant Center origin, if needed, belongs in the feed (03-merchant-feed).
- **Don't add `aggregateRating`.** There is one 1.0★ Judge.me review on one tee.
- **Don't write products, variants or inventory.** `cowork/product-data` owns them.
- **Dropped or parked by George:**
  - the tee-only test cart (Q9)
  - turning the Mida embed off (Mida stays on)
  - turning the Forms embed off (parked)

## Decisions still required

- **George:** typed go for the four policy edits.
- **George:** whether the password page is intended, and when it lifts.
- **Repository (orchestrator):** check that the default branch is `main`, and whether `cowork/geo-measurement` and `cowork/product-data` need rebasing.

## Data still required

- **CrUX mobile INP for the homepage**, 28 days after the popup rebuild (18 Oct → check about 15 Nov).
- **`ctc_shown` / `ctc_run` / signup rate** per 1,000 homepage sessions under the new teaser bar.

## Recommended follow-up dates

- **Same day as the password page lifts:** the re-runs in Do next item 6.
- **Same day as any theme publish:** re-run the Rich Results Test on hoodie, tee and outerwear (IDs in `FINDINGS.md`, Finding 7).
- **29 Oct 2026:** re-check tee schema availability and handling before the Merchant Center auto-add decision (03-merchant-feed, due 29–30 Oct).
- **About 15 Nov 2026:** homepage CrUX INP after the popup rebuild.
