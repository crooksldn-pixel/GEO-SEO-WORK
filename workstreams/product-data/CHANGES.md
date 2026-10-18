# Changes

Approval for every change below: owner decisions of 18 Oct 2026, 17:03 UTC, and George's "go" at 18:45 UTC (both in [ANSWERS.md](ANSWERS.md)), plus George's "answered" in the product-data Cowork chat at 20:07 BST. Writes ran 18 Oct 2026, 20:10–20:20 BST, through the Shopify Admin API (2026-01). Each item was re-read live just before writing. Barcodes, prices and inventory policy were untouched throughout.

---

## 18 Oct 2026 ~20:12 BST — Tee stock tracking off on the 18 remaining tees

**State:** LIVE

**Affected:** these 18 T-Shirts products, 540 variants:
- the 14 T-shirt Week tees: COCO CROOKS, CREGGS, CROOKS DIRECT, CROOKSBURY'S, CUCCI, FERAL, GETAWAY CLIVE, MAJOR LEAGUE CROOKS T-SHIRT, NATIONAL CROOKS, PHANTOM, SPECIAL DELIVERY, V.C.T.I.M.L, WHO NOSE?, WORLD WIDE;
- 4 older tees that went live today with the same `t-shirt-week` tag: 3 CLIVES, BROADCAST, MONEY CLIVE, OG CROOK.

The other 3 tees (CROOKS EXPRESS, CRX GARMS, CRXST★RZ) were already untracked by the project thread (change-log C-009).

**Before:** `inventoryItem.tracked = true` on all 540. Stock 0 on all of them, policy CONTINUE.

**After:** `tracked = false` on all 540. Policy is still CONTINUE.

**Reason:** owner decisions #2 and #12. All tees are print on demand, so tracked stock produces negative counts and "[n] LEFT" lines.

**Target:** false stock and scarcity claims on tee pages; honest availability in the feed.

**Validation:** Admin read-back, 21 of 21 T-Shirts products show `tracksInventory: false`, and all 630 tee variants show `tracked: false` and `inventoryPolicy: CONTINUE`. No userErrors.

**Expected metric:** no negative tee stock in Admin, and no "[n] LEFT" on tee pages. The "IN STOCK" and dispatch lines are theme output and stay until the theme fix.

## 18 Oct 2026 ~20:14 BST — Fabric-claim cleanup (C1–C9)

**State:** LIVE

**Affected and changed:**
- CHARCOAL CELLBLOCK SHORTS: `shopify.fabric` Cotton + Fleece → Fleece only.
- CROOKS EXPRESS, CRX GARMS, CRXST★RZ:
  - `crooks.fabric` deleted (was "Cotton", "Premium cotton", "Cotton");
  - CRX GARMS `shopify.fabric` Cotton → empty;
  - the `cotton` tag removed from all three.
- BLACK/BLUE and WHITE/RED MOTIONTEC™️ SOCKS:
  - "cotton blend" removed from the description and the SEO description;
  - `crooks.fabric` deleted (was "Cotton blend, reinforced heel");
  - `shopify.fabric` Cotton → empty.
- OG JEANS: "14oz" added in three places:
  - `crooks.fabric`: "Heavyweight denim" → "14oz denim";
  - description: "…Heavyweight 14oz denim with a baggy, stacked fit.";
  - SEO description: "OG Jeans in heavyweight 14oz denim with…".

**Not applied, because the "before" had already changed:** the description, SEO title, SEO description and alt rows of C2–C4. The three tees were rewritten earlier on 18 Oct, outside this workstream, and no longer mention cotton. Strings are in [artifacts/c-fabric-claim-fixes.md](artifacts/c-fabric-claim-fixes.md).

**Reason:** owner decision #12. The cotton claim covers hoodies and joggers only, and OG Jeans is 14oz.

**Target:** unconfirmed composition in copy and in Google's material attribute; a consistent spec across the denim line.

**Validation:** Admin read-back. Every field matches the "after" value.
- The first delete attempt failed as a batch: Shopify refuses `metafieldsDelete` on the `shopify` namespace.
- The `crooks.fabric` fields were deleted separately.
- `shopify.fabric` was cleared by setting an empty list `[]`.

**Expected metric:** no "cotton" in Merchant Center material for tees and socks; "14oz" on the OG Jeans snippet.

## 18 Oct 2026 ~20:14 BST — Crewneck and Puffa SEO titles (also their Shopping titles)

**State:** LIVE

**Affected:** CHARCOAL CELLBLOCK CREWNECK; DOUBLE-AGENT PUFFA.

**Before:**
- Crewneck: no SEO title, so Google showed "CHARCOAL CELLBLOCK CREWNECK".
- Puffa: "Double-Agent Puffa | Heat-Reactive Puffer Jacket".

**After:**
- Crewneck: "Charcoal Cellblock Crewneck — 450gsm Fleece | CROOKSLDN".
- Puffa: "Double-Agent Puffa — Heat-Reactive Puffer Jacket | CROOKSLDN".
- SEO descriptions unchanged.

**Reason:** owner decision #12, and the `cowork/merchant-center` task F proposals.

**Validation:** Admin read-back matches.

**Expected metric:** Merchant Center feed titles in mixed case with the brand.

## 18 Oct 2026 ~20:15 BST — HydroCuff and Puffa descriptions

**State:** LIVE

**Affected:** HYDROCUFF WINDBREAKER; DOUBLE-AGENT PUFFA.

**Before:**
- HydroCuff: "HydroCuff windbreaker, engineered to react on contact. Water-activated cuff pattern emerges in the rain."
- Puffa: "Heat-reactive puffer with signature Crooks handcuff embroidery to the chest and hood. Changes appearance with temperature, finished with a padded streetwear fit and concealed hand pockets." The stored HTML also contained a stray `<meta charset>` tag.

**After, HydroCuff:**
> "HydroCuff Windbreaker. Rain brings it out. When the jacket gets wet, a cuff pattern comes through on the fabric; once it dries, it goes back to black. Made to react wear after wear. / Hooded, with zipped front pockets and contrast stitching. / Care: wash cold. Do not iron."

**After, Puffa:**
> "Double-Agent Puffa. A heat-reactive puffer: the black shell turns white with heat and goes back to black as it cools. / Crooks handcuff embroidery on the chest and hood, a padded fit and concealed hand pockets. / Care: avoid washing where possible."

**Reason:** owner decisions #11 and #15, and `05-reactive-drafts.md` sections 1–2. The draft said "goes back to plain black"; this uses "goes back to black", because the jacket has white contrast stitching and the dry-state photo couldn't be checked from here. "Spot clean" was dropped, as George instructed.

**Validation:** Admin read-back matches.

**Expected metric:** GSC impressions and clicks for "water reactive jacket" and "heat reactive puffer" on the two product pages; the GEO specialist queries.

## 18 Oct 2026 ~20:16 BST — Age group "Adults" and gender "Unisex" on all 45 live products

**State:** LIVE

**Affected:** every ACTIVE product (45), including the 18 tees and 2 caps that went live today.

**Before:** no age group or gender on any product, and neither category metafield definition existed.

**After:**
- Enabled the standard definitions `shopify.age-group` (MetafieldDefinition 555043488087) and `shopify.target-gender` (555043586391).
- Created metaobjects "Adults" (668345794903, taxonomy value 2403) and "Unisex" (668345827671, taxonomy value 20).
- Set both on all 45 products.

**Reason:** owner decisions #10 (every product unisex, the 14 tees included) and #12 (age group adult). The decision said "all 25" when 25 were live. It's applied to all 45 now live, since every one is adult apparel or an accessory.

**Validation:** read-back, 45 of 45 carry both values. 90 metafields, no userErrors.

**Expected metric:** Merchant Center gender and age_group present on every offer; no new item issues.

## 18 Oct 2026 ~20:14 BST — Double-Agent Puffa colour Black

**State:** LIVE

**Affected:** DOUBLE-AGENT PUFFA `shopify.color-pattern`.

**Before:** none.

**After:** Black (`gid://shopify/Metaobject/450303197527`).

**Reason:** owner decision #11.

**Validation:** read-back matches.

**Expected metric:** colour present on the Puffa in Merchant Center.

## 18 Oct 2026 ~20:18 BST — Shipping weights

**State:** LIVE

**Affected:** BLACK SET and GREY SET (25 variants each); CELLBLOCK SET (25); CRX GARMS and CRXST★RZ (30 each).

**Before:** 0 on all 135 variants.

**After:**

| Product | Weight |
|---|---|
| Black Set | 1,700g |
| Grey Set | 1,700g |
| Cellblock Set | 1,450g |
| CRX Garms | 250g |
| CRXST★RZ | 250g |

**Reason:** owner decision #23. Sets are the sum of their parts; the two tees match the Express tee.

**Validation:** read-back, all 135 variants at the new weight.

**Expected metric:** correct label weights in Click & Drop; no shipping-weight issues in Merchant Center.

---

## Not done (attempted or skipped)

- **Cream Cap off Google & YouTube (item A):** skipped. On 18 Oct the cap has 4 photos, a description and an SEO title (added outside this workstream), so pulling it would undo a fix.
- **Store description:** not saved. Online Store → Preferences renders in an embedded frame that didn't take input from the browser tool after 3 attempts. The first attempt's keystrokes reached the admin page instead, which read them as a barcode scan and showed "Barcode … not found". That panel was closed; nothing was assigned or saved. Read-back confirms `shop.description` is still empty. Handed to George.
- **ReStock plan removal:** not done.
  - The API call was denied because the connector lacks the purchase-options scope.
  - The plan's app tag is "ReStock". The installed app with a PreOrder section is Notify Me! (bestpush), which opened behind upsell modals, so it wasn't operated.
  - Handed to George.
