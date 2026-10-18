# Questions for George — product data

**Branch:** cowork/product-data
**Prepared:** 18 Oct 2026, 17:30 BST, from live Shopify Admin reads at 16:30–17:20 BST

## How to answer

- Fill in the **Answer:** line under each question (and the Answer column in the Q10 table), on this branch, and commit. Replying in the product-data Cowork chat works too.
- When George says **"answered"** in the product-data chat, this session will:
  1. read this file;
  2. take each **YES** as George's approval for exactly the change written next to it;
  3. re-read every product live, make the writes, read them back, and log each one in `CHANGES.md`.
- Anything left blank, or marked NO, is not written.
- This repo is public. Don't commit anything private; Q17 and Q18 say where files can go instead.

Already confirmed, so not asked again:
- The cotton claim covers hoodies and joggers only.
- Weights: 550gsm hoodies and joggers, 450gsm crewnecks and shorts, 14oz jeans and jorts. No weight for tees.
- All tees are print on demand.
- Never touch barcodes.
- Products are made in China (origin fields only).

---

## Part 1 — Approvals (YES or NO)

### Q1. Take the Cream Cap off Google & YouTube

- **Product:** MAJOR LEAGUE CROOKS CAP (CREAM).
- **Change:** unpublish from the Google & YouTube channel only. It stays on Online Store, Shop, POS, Click & Drop, Facebook & Instagram and TikTok.
- **Why:** it has no images, and it's the only product disapproved for the UK in Merchant Center (`cowork/merchant-center` Finding 1 and its status).
- **Watch:** Google's auto-add starts on 2 Nov. Once the cap is off the channel, Google may re-add it from the site crawl, and it would be disapproved again with no image (`cowork/merchant-center` Finding 7). A cap photo (Q17) before then avoids that, as does the opt-out call Merchant Center makes on 29 Oct.
- **Recommend:** YES.

**Answer:**

### Q2. Store description

- **Change:** set Settings > Store details > store description, now empty, to exactly: "CROOKSLDN is an independent British streetwear brand making heavyweight fleece, baggy denim, graphic tees and reactive outerwear, cut in oversized, street-led silhouettes and released in drops."
- **How:** there's no API for this field, so it gets typed in Shopify admin in George's Chrome.
- **Recommend:** YES.

**Answer:**

### Q3. Fabric claim fixes C1–C8

- **Change:** apply every row in [artifacts/c-fabric-claim-fixes.md](artifacts/c-fabric-claim-fixes.md):
  - remove "cotton", "premium cotton" and "cotton blend" from the 3 live tees and both MotionTec socks: descriptions, SEO titles, SEO descriptions, alt text and fabric fields;
  - set the Cellblock Shorts' Google fabric attribute to Fleece only;
  - add "14oz" to OG Jeans in three places.
- **Side effect:** the three tee SEO titles are also their Google Shopping titles, so this removes "cotton" from Shopping too (`cowork/merchant-center` Finding 6).
- **Exception:** if the tee blanks or the socks really are cotton, give the exact composition here instead. It becomes a confirmed fact and stays in the copy.
- **Recommend:** YES.

**Answer:**

### Q4. Remove the `cotton` tag from the 3 live tees

- **Products:** CROOKS EXPRESS TEE, CRX GARMS T-SHIRT, CRXST★RZ T-SHIRT. Each has the tags black, cotton, tee, white; this removes `cotton`.
- **Safe to remove:** no collection rule uses that tag (checked 18 Oct).
- **Recommend:** YES.

**Answer:**

### Q5. Tees: stop the false stock and "leaves tomorrow" claims

- **Change (a):** turn off inventory tracking on every tee variant:
  - the 30 live variants (3 tees);
  - the 420 variants on the 14 draft T-shirt week tees (30 each).
  - Barcodes are not touched.
- **Change (b):** add the tag `made-to-order` to all 17 tees: the 3 live tees and the 14 drafts tagged `t-shirt-week`.
- **Why:** live tee pages say "IN STOCK" and "Ordered now — leaves tomorrow", and one shows a false "1 LEFT". The tag switches the product page to its made-to-order line. Untracking removes the negative stock (Express White XS −4, White M −4; CRXST★RZ Black S −2) and the "1 LEFT" line. The drafts would launch with the same problem (`cowork/live-site-checks` Finding 1, rated P1).
- **Not part of this:** the made-to-order line currently shows the theme's default "9–16 days". Setting the real print-on-demand lead time is a theme job, and the number is already asked for by `cowork/merchant-center` and `cowork/live-site-checks`.
- **Recommend:** YES, before any T-shirt week tee is published.

**Answer (a):**
**Answer (b):**

### Q6. Two SEO titles (also the Google Shopping titles)

These come from `cowork/merchant-center`, artifacts/04-merchant-center.md, task F.

| Product | Now | Proposed |
|---|---|---|
| CHARCOAL CELLBLOCK CREWNECK | no SEO title, so Google shows "CHARCOAL CELLBLOCK CREWNECK" | Charcoal Cellblock Crewneck — 450gsm Fleece \| CROOKSLDN |
| DOUBLE-AGENT PUFFA | Double-Agent Puffa \| Heat-Reactive Puffer Jacket | Double-Agent Puffa — Heat-Reactive Puffer Jacket \| CROOKSLDN |

The Cream Cap's title waits until it has a photo and goes back on Google.

- **Recommend:** YES to both.

**Answer:**

### Q7. Age group "adult"

- **Change:** set age group "adult" on the active products.
- **Count:** the brief said 24, but all 25 active products sit under Apparel & Accessories, the cap included.
- **Note:** Merchant Center shows no missing-age-group issue today. This is about completeness, not fixing a disapproval.
- **Answer with:** "25", or name the product to leave out.
- **Recommend:** 25.

**Answer:**

### Q8. Shipping weights worked out from other products

All these are 0g today.

| Product | Variants | Proposed | Basis |
|---|---|---|---|
| BLACK SET | 25 | 1,700g | hoodie 900g + sweats 800g |
| GREY SET | 25 | 1,700g | hoodie 900g + sweats 800g |
| PINK SET | 50 | 1,600g, or 1,700g | hoodie 900g + sweats 700g; 1,700g if Q12 says 800g |
| CELLBLOCK SET | 25 | 1,450g | crewneck 800g + shorts 650g |
| CRX GARMS T-SHIRT | 10 live | 250g | same as CROOKS EXPRESS TEE |
| CRXST★RZ T-SHIRT | 10 live | 250g | same as CROOKS EXPRESS TEE |

- **Recommend:** YES.

**Answer:**

### Q9. Remove the old ReStock "preorder" plan

- **Change:** remove the plan inside the ReStock app in the browser. ReStock is not uninstalled, which would be hard to undo.
- **Which products? Pick one:**
  - **(a)** the 3 live tees only;
  - **(b)** the 3 live tees and PINK CONVICT SWEATS.
- **Context on the Pink Sweats:** they also carry the CLIVE pre-order plan ("Pre-order: expected to dispatch by 31 October"). That's the plan the theme uses for PreOrder, and it stays. The brief says none of the last 250 orders used the ReStock plan.
- **Recommend:** (b).

**Answer:**

---

## Part 2 — Facts only George has

### Q10. Gender for each product

- **Background:** nothing in Shopify says which items are women's. The catalogue is men's and women's.
- **The Suggested column:** is only a starting point, read from sizing and cut. Correct every row.
- **Rules:** never default everything to male. Sets take the same answer as their two pieces unless stated.
- **Answer with:** female, male or unisex in each row.

| Product | Sizing on record | Suggested | Answer |
|---|---|---|---|
| BLACK CONVICT HOODIE | XS–XL, chart covers heights ~5'4" and under to ~6'2" and up | unisex | |
| GREY CONVICT HOODIE | same | unisex | |
| PINK CONVICT HOODIE | same, V1 and V2 | unisex | |
| BLACK CONVICT SWEATS | XS–XL, waist 76.2–96.5cm | unisex | |
| GREY CONVICT SWEATS | same | unisex | |
| PINK CONVICT SWEATS | same | unisex | |
| BLACK SET | hoodie + sweats sizes | as its pieces | |
| GREY SET | hoodie + sweats sizes | as its pieces | |
| PINK SET | hoodie + sweats sizes | as its pieces | |
| CHARCOAL CELLBLOCK CREWNECK | XS–XL, chest 109.2cm at XS | unisex | |
| CHARCOAL CELLBLOCK SHORTS | XS–XL, fits waist 71.1cm at XS | unisex | |
| CELLBLOCK SET | crewneck + shorts sizes | as its pieces | |
| BLUE WASH YARD JEANS | XS–XL (chart unreliable, see Q14) | George to say | |
| GREY WASH YARD JEANS | XS–XL (chart unreliable, see Q14) | George to say | |
| OG JEANS | XS–XL (chart unreliable, see Q14) | George to say | |
| BLUE WASH YARD JORTS | XS–XL, waist 76.2–96.5cm | George to say | |
| GREY WASH YARD JORTS | XS–XL, waist 76.2–96.5cm | George to say | |
| HYDROCUFF WINDBREAKER | XS–XL, chest 110–134cm | unisex | |
| DOUBLE-AGENT PUFFA | XS–XL, no chart | unisex | |
| CROOKS EXPRESS TEE | XS–XL, shared tee chart | unisex | |
| CRX GARMS T-SHIRT | same | unisex | |
| CRXST★RZ T-SHIRT | same | unisex | |
| BLACK/BLUE MOTIONTEC™️ SOCKS | 1/3/6/12 packs, no foot size | unisex | |
| WHITE/RED MOTIONTEC™️ SOCKS | 1/3/6/12 packs, no foot size | unisex | |
| MAJOR LEAGUE CROOKS CAP (CREAM) | one size | unisex | |

Also: should the 14 T-shirt week draft tees get the same answer as the live tees?

**Answer (drafts):**

### Q11. Double-Agent Puffa base colour

- **Background:** one word, for Google's colour attribute. The Puffa is the only product with no colour set. Its own image alt text says "the black shell".

**Answer:**

### Q12. Weights changed on 17 Oct

On 17 Oct, outside this session, CHARCOAL CELLBLOCK CREWNECK was set to 800g (20:42 BST) and PINK CONVICT SWEATS to 700g (20:43 BST). The Black and Grey Convict Sweats are 800g.

- **(a)** Should Pink Convict Sweats be 700g, or 800g?
- **(b)** Who made those two changes: George in admin, an app, or another session? This session is meant to be the only one writing product data.

**Answer (a):**
**Answer (b):**

### Q13. Shipping weights still missing

Give grams per variant. One number is fine if every size is the same.

| Product | Variants | Now | Answer |
|---|---|---|---|
| BLUE WASH YARD JORTS | XS–XL | 0 | |
| GREY WASH YARD JORTS | XS–XL | 0 | |
| DOUBLE-AGENT PUFFA | XS–XL | 0 | |
| MAJOR LEAGUE CROOKS CAP (CREAM) | one size | 0 | |
| WHITE/RED MOTIONTEC™️ SOCKS 1pc | | 0 | |
| WHITE/RED MOTIONTEC™️ SOCKS 3pc | | 0 | |
| WHITE/RED MOTIONTEC™️ SOCKS 6pc | | 0 | |
| WHITE/RED MOTIONTEC™️ SOCKS 12pc | | 0 | |
| BLACK/BLUE MOTIONTEC™️ SOCKS 3pc | | 20g (same as 1 pair) | |
| BLACK/BLUE MOTIONTEC™️ SOCKS 6pc | | 20g (same as 1 pair) | |
| BLACK/BLUE MOTIONTEC™️ SOCKS 12pc | | 20g (same as 1 pair) | |

Also: is 20g right for one pair of Black/Blue socks?

**Answer:**

### Q14. Real size charts for the jeans

- **Problem:** the charts on BLUE WASH YARD JEANS, GREY WASH YARD JEANS and OG JEANS are copied value for value from the Convict Sweats chart, and customers size from them.
- **What's needed:** real measurements in cm for XS, S, M, L and XL:
  - waist, inseam and leg opening;
  - plus rise, thigh or hip if George wants them shown.
- **Format:** say whether the Yard and OG fits share one chart or have separate ones. Any table works, pasted here.

**Answer:**

---

## Part 3 — Files

### Q15. Reactive descriptions: two wording calls (needed for G)

- **(a)** HydroCuff is confirmed as "reasonably durable". Is "made to react wear after wear" a fair way to say that?
- **(b)** Does the Double-Agent Puffa return to its normal look as it cools?

**Answer (a):**
**Answer (b):**

### Q16. Project files this workstream needs

From the claude.ai Project `seo/` folder:
- `workstreams/05-reactive-drafts.md` (sections 1–2, the HydroCuff and Puffa descriptions)
- `assets/README.md`
- `workstreams/02-product-schema.md` (last two sections)
- `workstreams/03-merchant-feed-handoff.md` (sections A–D)
- `change-log.md` (C-006 and C-WS02-1)

Where they can go:
- this branch, at `workstreams/product-data/artifacts/inputs/`; or
- the shared `cowork/project-files-import` branch suggested in GitHub issue #1.

This session will look in both.

**Answer (where committed):**

### Q17. Product photos

- **Needed, in this order:**
  1. Cream Cap;
  2. a HydroCuff dry and wet pair with identical framing;
  3. on-body shots;
  4. the Puffa, normal and reacted.
- **Where:** they'll be public on the site anyway, so committing them to `workstreams/product-data/artifacts/inputs/photos/` is fine. Attaching them in the product-data chat works too.
- **Rule:** no placeholders. Only real photos get attached.

**Answer (where):**

### Q18. Bag-label photos (for K)

- **Needed:** one photo per product, denim first. Each is checked against its variant's Shopify barcode, report only.
- **Where:** attach them in the product-data chat rather than committing them, since the repo is public.

**Answer:**
