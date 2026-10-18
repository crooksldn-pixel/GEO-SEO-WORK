# Workstream 3's 11 findings, checked against Merchant Center

Source of the findings: `cowork/project-files-import` → `project-files/seo/workstreams/03-merchant-feed.md` (audit 16 Oct, written without Merchant Center access).

Evidence for each column:
- **16 Oct:** the products export ([baseline-2026-10-16.md](baseline-2026-10-16.md)).
- **18 Oct 20:22:** a fresh products export, taken after product-data's writes landed and while the store was password-locked.
- Issues exports from 18 Oct, 16:35 and 20:13 BST.

| # | Workstream 3 said | 16 Oct | 18 Oct 20:22 | Status |
|---|---|---|---|---|
| F1 | Google will auto-add 30+ products on 2 Nov | Confirmed: "Google found 30 additional products". They can't be listed without adding them. | Same | Q4 rule: decide on 29 Oct |
| F2 | 112 invalid 8-digit GTINs; 5 codes shared | The feed sends a GTIN on only **8 variants** (2 codes, on L and XS of the Blue and Grey Yard jeans and jorts). No GTIN issue anywhere in Merchant Center. | Same 8 variants | No action. The 112 is the Shopify barcode count (Q6). Attribute rules aren't available on these sources (FINDINGS 2). |
| F3 | No gender or age group | None sent | **unisex / adult on 303 of 306 GB offers.** One Puffa variant is blank. | Done by product-data; re-check 29 Oct |
| F4 | Colour missing on HydroCuff, Puffa, sets, cap, Blue Yard Jeans | Missing only on Puffa and both socks. HydroCuff, sets and jeans had it. | Puffa **Black**. The Brown and Blue caps and both socks are still blank. | Socks and the new caps: product-data |
| F5 | No description on Crooks Express, 3 sets, cap | All present except the Cream Cap | All present, caps included | Done |
| F6 | Feed titles are ALL CAPS | Not true: the feed sends the SEO title. Only the crewneck and cap were all caps. | Crewneck and Puffa titles fixed. Caps are title-case. Tees now "CRX Garms T-Shirt \| CROOKSLDN" etc. | Done |
| F7 | Sets: category, is_bundle | Outfit Sets + `is_bundle = yes` on all 4 | Same | Done |
| F8 | Tee availability and "ships today" | in_stock; handling 0 days | Tees now £20, 30 variants each, still handling 0 | Task D: needs George's typed yes (CHANGES.md) |
| F9 | Cream Cap: no images or description | No image; disapproved in 76 labels | Cream, Brown and Blue caps all in feed **with images and descriptions** | Image issue resolved; Brown and Blue need colour |
| F10 | Category tidy-up (212/207 overrides) | Crewneck 212, shorts 207, others blank | Same | Low ROI; product-data |
| F11 | SKUs empty, weights zero | Weights mostly 0 | Real weights on most products; sets partly; jorts, Puffa, cap and White/Red socks still 0 | Parked by owner (#23) |

The new problem tonight isn't in workstream 3's list: the password lock has removed product links from the whole feed (FINDINGS 8).
