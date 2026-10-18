# Next

## Do next

1. **When George types yes in this chat** to the two writes (STATUS Blocker 2):
   - Products → filter "Data source: Merchant Center" → select all 10 (`G-65230983` to `G-65230992`) → **Archive** (not delete). Read back. Log it in CHANGES.md.
   - Data sources → Add product source → supplemental → upload `artifacts/gmc-supplemental-tee-handling-GB.tsv` (a copy is in George's Downloads). Link it to the **GB** "Shopify App API" source only. Check the link and the row match. Log it.
2. **After the store reopens:** re-export products and issues within 24 hours. Run `gmc_summary.py` and confirm:
   - every GB offer has a `link`
   - "Missing product page" and "Invalid checkout URL" are gone
   - the tee supplemental has applied (handling 2–3, label print-on-demand)
3. **When the 14 T-shirt Week tees appear in the GB feed:** add their variant IDs to the supplemental file and re-upload.
4. **29 Oct (task E):** re-export, compare with the baseline, and apply George's Q4 rule. Stay in if the UK is clean, otherwise opt out by 1 Nov. The reminder is set for 09:00 GMT.

## Do not do yet

- **Opting out.** George's rule (Q4): decide on 29 Oct. Stay in only if the UK is clean.
- **Hard-deleting the 10 duplicates.** Archive them; a permanent delete is George's own action from the archive.
- **Anything for the GTIN issue.** No GTIN issue is live (FINDINGS 2), and attribute rules don't exist on these sources.
- **Editing Shopify-created shipping policies or the 76 Shopify sources in Merchant Center.** The Shopify app is likely to overwrite them. Fix shipping times in Shopify instead.
- **Liechtenstein, Bulgaria, Croatia, Malta or South Korea gaps.** These have low value and belong in Shopify Markets (FINDINGS 5).
- **Clicking "Add all products found" or "Add now".** Either one adds the 30 crawled products immediately.

## Decisions still required

- George: is the password lock deliberate, and when does it lift?
- George: a typed yes in this chat for the archive and the tee supplemental. Both are already approved in ANSWERS.md, but this session's permission check needs it in chat.

## Data still required

- None. All answers are in ANSWERS.md.

## Recommended follow-up date

**Thu 29 Oct 2026**, for the export and the opt-in call. A final check on Sat 31 Oct if anything is still processing. The opt-out deadline is Sun 1 Nov and auto-add starts Mon 2 Nov.

Raw downloads on George's Mac, in Downloads (not committed, because the repository is public):
- `products_2026-10-16_12-28-38.zip`: the 16 Oct baseline
- `product_issues_2026-10-18_08-35-43.csv`: before the lock
- `products_2026-10-18_12-22-35.zip` and `product_issues_2026-10-18_12-13-25.csv`: during the lock
