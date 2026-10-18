# Next

## Do next

1. **Get George's answers to the two Merchant Center questions** in `artifacts/04-merchant-center.md`, sections P1 and P2:
   - delete the 10 `CROOKSRELEASESEPT` duplicates?
   - business name "Crooks LDN"?
   
   Make each change only after his "yes" in chat. Log before, after, time and approval in `CHANGES.md`.
2. **Task D, once George gives the tee print-on-demand time:**
   - In Settings > Data sources > Add product source, check whether a supplemental source (Google Sheet) can be linked to the "Shopify App API" Merchant API sources, and whether its values override Shopify's item-level `shipping` handling time.
   - If yes, prepare a sheet for the 30 tee variants with `min_handling_time`, `max_handling_time` and `shipping_label` = `print-on-demand`, keyed on the `shopify_ZZ_…` IDs. Start with feed label GB.
   - Show George before linking.
   - If no, record that the fix has to come from the Shopify side, which needs a decision on who owns Shopify shipping settings.
3. **29 Oct (task E), before the 1 Nov opt-out deadline:**
   - Download Products > All products and Needs attention > all issues.
   - Run `artifacts/gmc_summary.py` on the new files and compare with `artifacts/baseline-2026-10-16.md`.
   - Check the "Found by Google" count and the account issues.
   - Send George one line: stay opted in, or opt out before 1 Nov, with the evidence.
   - A reminder is scheduled in the Cowork chat for 29 Oct 09:00 GMT.
4. **When product-data's item A goes live** (Cream Cap off Google & YouTube), confirm the cap's 76 disapprovals clear within 1–3 days.
5. **Task F:** pass the title proposals to `cowork/product-data` through the orchestrator. Titles can only change from Shopify (FINDINGS 6).

## Do not do yet

- **Opting out.** That's George's call on 29–30 Oct, and only if core items are still disapproved, or he decides auto-add is too risky (FINDINGS 7).
- **Anything for the GTIN issue.** No GTIN issue is live (FINDINGS 2), and attribute rules don't exist on these sources.
- **Editing Shopify-created shipping policies or the 76 Shopify sources in Merchant Center.** The Shopify app is likely to overwrite them. Fix shipping times in Shopify instead.
- **Liechtenstein, Bulgaria, Croatia, Malta or South Korea gaps.** These have low value and belong in Shopify Markets (FINDINGS 5).
- **Clicking "Add all products found" or "Add now".** Either one adds the 30 crawled products immediately.

## Decisions still required

- George: delete the 10 `CROOKSRELEASESEPT` products (yes/no).
- George: business name "Crooks LDN" (yes/no, or another confirmed alternate).
- George, 29–30 Oct: stay opted in to auto-add, or opt out.
- Orchestrator: who owns Shopify Settings > Shipping? It drives the 2–4 day free tiers, the 12:00 AM cut-off and item-level handling time.

## Data still required

- The tee print-on-demand production + dispatch time, in working days.
- `workstreams/03-merchant-feed.md` (the 11 findings) and `03-merchant-feed-handoff.md` (corrections A–E), so this record can be checked against them.
- Optional: where the brief's "112 invalid codes" figure came from.

## Recommended follow-up date

**Thu 29 Oct 2026**, for the export and the opt-in call. A final check on Sat 31 Oct if anything is still processing. The opt-out deadline is Sun 1 Nov and auto-add starts Mon 2 Nov.

Baseline raw files on George's Mac, in Downloads (not committed, because the repository is public):
- `products_2026-10-16_12-28-38.zip`
- `product_issues_2026-10-18_08-35-43.csv`
