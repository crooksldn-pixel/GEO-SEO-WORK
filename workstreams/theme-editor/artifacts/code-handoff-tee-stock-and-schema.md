# Code handoff — tee stock lines and tee shipping schema

**For:** whichever session is allowed to edit theme code. This session is limited to theme-editor settings and makes no code edits.  
**Owner decisions:** #1 (tees dispatch 2–3 working days), #2 (tees show no "IN STOCK" or "1 LEFT" and stay purchasable), #3 (Tracked 24 typically 1–2, Tracked 48 typically 2–3 working days after dispatch).  
**Base:** live theme "CROOKSLDN — live 18 Oct + evening fixes" (207475147095), read 18 Oct 20:15 BST. File checksums at that time are below. Re-read each file before editing. The "live 18 Oct + colour photos" copy was already changing two of them at 20:09 BST.

| File | Checksum on live |
|---|---|
| `sections/crooks-exhibit-record.liquid` | ba93a9853c3b84fe354ed6cfa637b81c |
| `assets/crooks-record.js` | e257b64a635e4b88fdc7cf38f21e1c22 |
| `snippets/crooks-schema-product.liquid` | eda3cdc89001ec3998a993331df1cc5d |
| `snippets/crooks-schema-shipping.liquid` | c6a446723e801e0c40b8995c22262003 |

## 1. Tees: no "IN STOCK" or "[n] LEFT"

Today the made-to-order flag `crk_mto` is assigned at around line 417 of `sections/crooks-exhibit-record.liquid`. That's after the stock line is printed (around lines 373–408), and nothing passes it to the script.

1. Assign `crk_mto` once, before `{%- render 'crooks-schema-product', product: product -%}` (around line 104). It's true when `section.settings.made_to_order_tag` is not blank and the product carries that tag (currently `tee`). The later assignment can stay or go.
2. On the root `<div class="crk-root crk-record" …>` (around lines 106–120), add `data-crk-mto="true|false"` next to `data-crk-low-threshold`.
3. Server-rendered stock line, multi-variant branch (around line 373):
   - Add a branch `elsif crk_mto` that prints nothing. Put it after the "select" and "sold out" branches and before the low-stock and in-stock branches.
   - Add `hidden` to the `<p data-crk-stockline>` when `crk_mto` is true and a buyable variant is chosen.
4. Server-rendered stock line, single-variant branch (around line 401): print nothing and add `hidden` when `crk_mto` is true.
5. `assets/crooks-record.js`:
   - In `initRecord`, next to `var LOW = …` (line 44), read `var MTO = root.getAttribute('data-crk-mto') === 'true';`.
   - In `render()`, stock-line block (around lines 434–450), add `else if (MTO) { stockLine.textContent = ''; … }` before the low-stock branch.
   - At the end of that block, set `stockLine.hidden = !!(MTO && complete && v && v.available);`.

   The "choose a size" and "sold out" messages keep working for tees.

**Check in preview before publishing:**
- A tee (e.g. `/products/crooks-express-t-shirt`): pick a colour and size. No stock line shows, "Printed to order. Dispatched within 2–3 working days." shows, and ADD TO BAG works.
- A hoodie: "IN STOCK" still shows, and the same-day line still shows.

## 2. Tee shipping schema timings

1. `sections/crooks-exhibit-record.liquid`: pass the flag, `render 'crooks-schema-product', product: product, mto: crk_mto`.
2. `snippets/crooks-schema-product.liquid`: both `render 'crooks-schema-shipping'` calls (around lines 149 and 212) add `mto: mto`. Update the `Accepts:` comment.
3. `snippets/crooks-schema-shipping.liquid`:
   - `handlingTime`: minValue 2, maxValue 3 when `mto`. Otherwise keep 0–2.
   - `transitTime`: 2–3 days. The snippet states the Tracked 48 rate (£3, free from £30), and decision #3 puts Tracked 48 at typically 2–3 working days after dispatch. It's 1–2 today.

**Check:** Rich Results Test on a tee and a hoodie. Tee offers show handling 2–3 and transit 2–3. Hoodie offers show handling 0–2 and transit 2–3. Still 0 errors.

## Not in this handoff

- Status bar m2 "ORDER BY 6PM — DISPATCHED TODAY" (`sections/header-group.json`). That's a theme-editor text change, waiting on George's wording.
- The Merchant Center tee handling time belongs to `cowork/merchant-center`.
- Collection cards and "More from this drop" were not checked for stock wording on tees.
