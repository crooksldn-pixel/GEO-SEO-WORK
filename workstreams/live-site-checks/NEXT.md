# Next

## Do next

1. **Tees: stop the false stock and dispatch claims.** Do this before any T-shirt week tee is published.
   - Tag all 17 T-Shirts products `made-to-order`: the 3 active ones (`crooks-express-t-shirt`, `crx-garms-t-shirt`, `crxst-rz-t-shirt`) and the 14 drafts tagged `t-shirt-week`.
   - Turn off "Track quantity" on their variants.
   - Then re-open a tee PDP and confirm "IN STOCK", "Ordered now — leaves tomorrow" and "1 LEFT" are gone.
   - Owner: product-data workstream / George.
2. **Checkout consent.** Turn off preselect for the email marketing box (Settings → Checkout → Marketing options). Check by opening checkout with any item: "Keep me updated." should start unticked. Owner: George.
3. **One delivery-time wording.** UK delivery is free from £30 by Royal Mail Tracked 48 (2–3 working days), and free Tracked 24 (1–2 working days) from £80. Under £30, Tracked 48 is £3 and Tracked 24 is £4.99. In-stock orders placed by 18:00 Mon–Sat leave the same day; tees are printed to order; pre-orders leave on the date shown.
   - Apply it to: shipping, refund and contact policies; FAQ (`templates/page.faq.json`); Terms (`templates/page.terms.json`); the PDP custody blocks (`templates/product.json`, `templates/product.crooks.json`); and the status bar.
   - Set schema `transitTime` to 2–3 for Tracked 48 in `snippets/crooks-schema-shipping.liquid`.
   - The exact place list is in the report, section 3.
4. **Performance (apps).** Sample Mida recording or exclude the homepage. Limit the Shopify Forms embed to pages that use it, or remove it.
5. **Pre-order cancellation policy.** Draft and add it under Settings → Policies, after George approves the wording.
6. **Theme code, small fixes:**
   - `sections/crooks-exhibit-record.liquid`: no `label_low` when `inventory_policy == 'continue'`.
   - `snippets/crooks-schema-product.liquid`: print `size` once when a product has two size options (sets).
   - Tee `handlingTime` from the POD lead time.
   - Set-panel line (`set_shipping_text`): "The set ships free by Tracked 24 (orders £80+)".

## Do not do yet

- **Don't build a new popup fix.** One is already built and staged in "CROOKSLDN — Claude P1 fixes (copy of live 16 Oct)" (09-performance workstream). Wait for George to lift that theme's hold.
- **Don't edit `snippets/crack-the-cuffs.liquid` or `snippets/crooks-schema-site.liquid` on the live theme.** Both have staged versions in the held theme; editing live now creates a merge conflict when it publishes.
- **Don't make theme edits (Do next items 3 and 6) until the theme vehicle is decided.** "Claude P1 fixes" is a full copy of live as of 16 Oct. If live is edited and the held theme is published afterwards, every live edit since 16 Oct is silently reverted. Pick one route first:
  - **(a)** Port the two changed files from the held theme into live, retire the held copy, then edit live.
  - **(b)** Make every edit in both themes.

  Policies (Shopify settings) and product data (tags, inventory tracking) are not theme-bound and can go ahead now.
- **Don't put a number in the tee made-to-order line until George confirms the POD lead time.** The theme default "9–16 days" is not a CROOKSLDN figure.
- **Don't fill `crooks.origin`.** It renders in the PDP "Origin" row, and the brand rule is no manufacturing origin in consumer copy. Merchant Center origin, if needed, belongs in the feed (03-merchant-feed).
- **Don't add `aggregateRating`.** There is one 1.0★ Judge.me review on one tee.

## Decisions still required

- POD lead time for tees (George).
- Mida: keep full recording, sample it, or drop it (George — app spend).
- Shopify Forms vs Omnisend as the single signup stack (George).
- Cancellation policy wording for pre-orders (George).
- When to lift the hold on "Claude P1 fixes" (George).
- **Repository (orchestrator):** the repo had no `main` when this branch was pushed. This branch, like `cowork/geo-measurement`, is a root branch with no shared history. GitHub currently shows `cowork/geo-measurement` as the default branch. Create `main`, then merge workstream branches with `--allow-unrelated-histories` or rebase them onto `main`.

## Data still required

- POD lead time (above).
- Post-fix CrUX homepage INP, mobile.
- `ctc_shown` / `ctc_run` / signup rate per 1,000 homepage sessions, after the staged popup ships.

## Recommended follow-up date

- **29 Oct 2026:** re-check tee PDP lines and tee schema availability/handling. The Merchant Center auto-add decision (03-merchant-feed) is due 29–30 Oct, and tee offers currently claim InStock with 0–2 day handling.
- **28 days after the Mida/Forms change:** re-run PageSpeed on the homepage and read CrUX mobile INP. For example, a change on 20 Oct → check 17 Nov.
- **Same day as any theme publish:** re-run the Rich Results Test on the hoodie, tee and outerwear URLs (IDs in `FINDINGS.md`, Finding 7) to confirm nothing regressed.
