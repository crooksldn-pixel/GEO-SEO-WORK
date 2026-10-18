# Next

## Do next

When George says **"answered"** in the product-data chat:

1. Fetch this branch and `cowork/project-files-import` (if it exists). Read [QUESTIONS.md](QUESTIONS.md) and any files under `artifacts/inputs/`.
2. List back to George, in one message, the writes his YES answers authorise. Then make them in the order below. Before each write, re-read the product live and confirm the "before" still matches. If it doesn't, stop on that item and show George the difference.
3. Write order:
   - **Q1 (A):** `publishableUnpublish` on MAJOR LEAGUE CROOKS CAP (CREAM) (`gid://shopify/Product/11236081402199`) from Google & YouTube (`gid://shopify/Publication/333206487383`). Read back `resourcePublicationsV2`.
   - **Q5:**
     - `inventoryItem.tracked = false` on every variant of the 17 T-Shirts products (30 live and 420 draft variants);
     - add the tag `made-to-order` to all 17;
     - don't touch barcodes;
     - then open a live tee page and confirm "IN STOCK", "Ordered now — leaves tomorrow" and "1 LEFT" are gone.
   - **Q3 and Q4:** apply [artifacts/c-fabric-claim-fixes.md](artifacts/c-fabric-claim-fixes.md) exactly, and remove the tag `cotton` from the 3 live tees. Read back every field. Open each product page and check how the theme shows a cleared `crooks.fabric`; if it shows an empty label, report it to the theme workstream.
   - **Q6:** the Crewneck and Puffa SEO titles.
   - **Q8 and Q13:** variant weights in grams.
   - **Q7, Q10, Q11:**
     - enable the `shopify.age-group` and `shopify.target-gender` category metafield definitions, or use the Google & YouTube channel fields if the connector can't;
     - write age group and gender per product as answered, and the Puffa colour (Black is `gid://shopify/Metaobject/450303197527` if that's the answer);
     - never default gender to male.
   - **Q9:** remove the ReStock plan inside the ReStock app in the browser, on the products George picked. Don't uninstall.
   - **Q2:** set the store description in Shopify admin in the browser.
   - **Q14:** write `crooks.measurements` on the three jeans products once real values are supplied.
4. Log every write in `CHANGES.md`: before, after, approval (George's "answered" plus the time), read-back and expected metric. Move each item's status in `artifacts/01-product-data.md` from pending to live.
5. Tell `cowork/merchant-center`, through this branch's STATUS, when A, the titles and the attributes are live, so its 29 Oct export can be read against them.

## Do not do yet

- Don't write anything without a YES in QUESTIONS.md and George's "answered" in the chat.
- Don't write gender from the Suggested column. Use George's Answer column only.
- Don't change the jeans size charts until real measurements are supplied. Keep the current values rather than blanking them.
- G waits for `05-reactive-drafts.md` and George's two wording calls (Q15). Re-read the live product before editing. `cowork/geo-measurement` Finding suggests also using the terms "water-reactive (hydrochromic)" and "heat-reactive (thermochromic)". Raise that with George when drafting G; don't add it on our own.
- No images until real photos arrive. No placeholders.
- Never clear, change or move barcodes. K is report only.
- Don't uninstall ReStock.
- Don't merge this branch; the orchestrator decides what gets merged.

## Decisions still required

- Q1–Q9 (YES or NO), Q10 (gender per product), Q12(b): who changed the weights on 17 Oct.
- Orchestrator: confirm no other session or process writes product data. Two weights were changed outside this session on 17 Oct (FINDINGS 6).

## Data still required

- Q11 Puffa colour, Q12(a) Pink Sweats weight, Q13 missing weights, Q14 jeans measurements, Q15 the two wording calls.
- Q16 Project files, Q17 product photos, Q18 bag-label photos.

## Recommended follow-up date

- **Before 25 Oct:** land A, the tee fixes, C and the Q6 titles. That gives Merchant Center time to reprocess before `cowork/merchant-center` re-exports on 29 Oct for the auto-add decision (opt-out deadline 1 Nov).
- **2–3 days after A:** confirm with `cowork/merchant-center` that the cap's disapprovals have cleared.
- **After Merchant Center reprocesses:** ask `cowork/geo-measurement` to re-run the Shopping-pack queries (FINDINGS 11).
