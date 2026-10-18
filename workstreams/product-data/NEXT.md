# Next

## Do next

1. Get George's yes in chat, then unpublish MAJOR LEAGUE CROOKS CAP (CREAM) (`gid://shopify/Product/11236081402199`) from Google & YouTube (`gid://shopify/Publication/333206487383`) with `publishableUnpublish`. Leave every other channel on. Read back `resourcePublicationsV2`, then log it in CHANGES.md and `artifacts/01-product-data.md`.
2. With George's yes on C, re-read each product, apply C1–C8 exactly as written in `artifacts/c-fabric-claim-fixes.md`, and read back every field. Then open each product page and check how the theme shows a cleared `crooks.fabric`. If it shows an empty label, report it to the theme workstream; don't fix it from here.
3. Once George answers D1, E and F, enable the `shopify.age-group` and `shopify.target-gender` category metafield definitions, or fall back to the Google & YouTube channel fields if the connector can't create them. Then write age group, gender per product and the Puffa colour. Never default gender to male.
4. With George's yes on D2, set `inventoryItem.tracked = false` on the 30 tee variants. Don't touch barcodes. Read back tracked status and check that a tee page's product schema says InStock.
5. Enter the derived H weights once approved, then the remaining weights as George supplies them.
6. With George's OK on I, remove the ReStock "preorder" plan inside the ReStock app in the browser, not by uninstalling. Whether the PINK CONVICT SWEATS are included is his call.
7. B: set the store description in Shopify admin in the browser. There's no API route.

## Do not do yet

- Don't write anything to Shopify without George's yes in this chat. The connector enforces this.
- Don't write gender until George has corrected the suggested list.
- Don't change the jeans size charts until George sends real measurements. Keep the current values rather than blanking them.
- Don't touch G until `05-reactive-drafts.md` is readable and George has made both wording calls. Re-read the live product before editing.
- Don't attach any image until real photos are in `seo/assets/incoming/`. No placeholders.
- Don't clear, change or move barcodes, ever. K is report only.
- Don't uninstall ReStock without an explicit OK. It's hard to undo.
- Don't merge this branch; the orchestrator decides what gets merged.

## Decisions still required

- A, B, C, D2: yes or no.
- D1: age group on all 25 products, or 24.
- E: gender for each product.
- I: tees only, or Pink Convict Sweats as well.
- Who set the Crewneck and Pink Sweats weights on 17 Oct? The orchestrator needs to confirm whether another writer is active (Finding 6).

## Data still required

- Puffa base colour (one word).
- Shipping weights: Blue and Grey Yard Jorts, Puffa, Cream Cap, and WHITE/RED MOTIONTEC SOCKS per pack size. Also confirmation of Pink Convict Sweats at 700g, and per-pack weights for BLACK/BLUE socks (currently 20g on every pack).
- Real measurements for BLUE WASH YARD JEANS, GREY WASH YARD JEANS and OG JEANS.
- `workstreams/05-reactive-drafts.md` (sections 1–2), `assets/README.md`, `workstreams/02-product-schema.md` (last two sections) and `workstreams/03-merchant-feed-handoff.md` (A–D).
- Photos: Cream Cap; HydroCuff dry and wet with matching framing; on-body shots; Puffa normal and reacted.
- Bag-label photos for K.

## Recommended follow-up date

- Check Merchant Center item issues 2–3 days after A, D1, E and F go live.
- Aim to land A, D1, E and F by 25 Oct. That gives Merchant Center time to reprocess before the Merchant Center workstream decides around 29–30 Oct whether to stay opted in to Google's auto-add of site products.
