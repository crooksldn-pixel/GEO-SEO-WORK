# Next

## Do next

1. **Tue 3 Nov:** download products and issues, and run `gmc_summary.py`. Then:
   - list the products auto-add brought in (a "Found by Google" source)
   - flag any duplicates of Shopify items, and anything George pulled from the Google channel (for example, a cap)
   - confirm UK disapprovals are still about 0
2. **When George types yes in this chat:**
   - Products → filter "Data source: Merchant Center" → select the 10 (`G-65230983` to `G-65230992`) → **Archive**.
   - Rebuild `artifacts/gmc-supplemental-tee-handling-GB.tsv` from a fresh export, with current variant IDs and the shipping prices Shopify is sending at the time (on 29 Oct: Tracked 48 £0.00; Tracked 24 £4.99, free from £50). The supplemental replaces the whole `shipping` value for those tees. Then Data sources → Add product source → supplemental → upload, and link it to the **GB** Shopify source only.
   - Log both in CHANGES.md.
3. **When the 14 T-shirt Week tees join the GB feed:** add them to the supplemental.

## Do not do yet

- **Opting out.** Decided 29 Oct: stay opted in. The UK is clean (FINDINGS 10).
- **Hard-deleting the 10 duplicates.** Archive them; a permanent delete is George's own action from the archive.
- **Anything for the GTIN issue.** No GTIN issue is live (FINDINGS 2), and attribute rules don't exist on these sources.
- **Editing Shopify-created shipping policies or the 76 Shopify sources in Merchant Center.** The Shopify app is likely to overwrite them. Fix shipping times in Shopify instead.
- **Liechtenstein, Bulgaria, Croatia, Malta or South Korea gaps.** These have low value and belong in Shopify Markets (FINDINGS 5).
- **Clicking "Add all products found" or "Add now".** Either one adds the 30 crawled products immediately.

## Decisions still required

- George: a typed yes in this chat for the archive and the tee supplemental.
- George: is the free UK shipping deliberate? If so, the policy page needs updating (FINDINGS 10).
- `cowork/international-markets-pricing`: why 76 variants per international label have no URL.

## Data still required

- None. All answers are in ANSWERS.md.

## Recommended follow-up date

**Tue 3 Nov 2026**, after Google's 2 Nov auto-add.

Raw downloads on George's Mac, in Downloads (not committed, because the repository is public):
- `products_2026-10-16_12-28-38.zip`: the 16 Oct baseline
- `product_issues_2026-10-18_08-35-43.csv`: before the lock
- `products_2026-10-18_12-22-35.zip` and `product_issues_2026-10-18_12-13-25.csv`: during the lock
- `products_2026-10-29_02-01-55.zip` and `product_issues_2026-10-29_02-01-15.csv`: the 29 Oct check
