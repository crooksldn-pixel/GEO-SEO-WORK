# Findings

## Finding 1 — Live theme identity, unchanged since 16 Oct

**Finding:**
The published theme is **"CROOKSLDN — SEO round 2 (from live 16 Oct)"**, theme ID 207329132887, Horizon 3.5.0 base. Its last save was 16 Oct 2026 14:33 BST. Rechecked 18 Oct 16:34 BST: same theme, and identical file checksums for every file this workstream touches.

**Evidence:**
- Shopify Admin API `themes` query: only 207329132887 has `role: MAIN`. Confirmed on 16 Oct from a cookieless storefront fetch (`Shopify.theme.role = "main"`).
- File checksums (MD5) on 18 Oct, unchanged from 16 Oct:
  - `config/settings_data.json` ba7ae92f0d149979c5ff79238521f0a4 (updated 16 Oct 13:17 BST)
  - `sections/footer-group.json` fc89bbdf7ccb2cd8b24d9a53ab7e7d7d (12:49)
  - `sections/header-group.json` e5ba421bab9756e384ee10eb6dcf2456 (12:49)
  - `templates/product.json` 08a2b855a061c69eb975053a760b4339 (12:49)
  - `sections/crooks-exhibit-record.liquid` 879bfee51786227ca11cf18aad11c794 (14:03)
  - `assets/crooks-record.js` e3a8c97a2e631511f3c96c4bc1a7d779 (12:49)

**Why it matters:**
Any agent comparing before and after states can use these checksums to prove whether the live theme moved under them.

**Confidence:** High

**Recommended action:**
Recheck the checksums before every save. A mismatch means someone else has edited the live theme.

---

## Finding 2 — Draft themes copied from live on 16 Oct would undo live theme-editor changes if published

**Finding:**
Three unpublished themes are copies of the live theme as it stood on 16 Oct:
- "CROOKSLDN — Claude P1 fixes (copy of live 16 Oct)" (207340142935, saved 16 Oct 19:40 BST, ON HOLD)
- "CROOKSLDN — Puffa heat reaction (from live 16 Oct)" (207338668375, saved 16 Oct 19:54 BST)
- "CROOKSLDN — REVIEW: SEO + Tee Week + Returns" (207020425559, same timestamp as live)

Publishing any of them later replaces the live theme's `settings_data.json`, `footer-group.json` and `templates/product.json` with their own 16 Oct copies. That silently reverts every setting this workstream changes on the live theme: the Judge.me embeds, the footer OUTERWEAR link and the tee dispatch wording.

**Evidence:**
Shopify Admin API `themes` query, 18 Oct 16:34 BST. Theme names and timestamps as listed.

**Why it matters:**
This is the main cross-workstream conflict risk. The theme and code workstreams each assume their copy is the base.

**Confidence:** High

**Recommended action:**
Before any of these themes is published, re-apply the live changes listed in `CHANGES.md` to it, or copy the live theme's editor settings across. Whoever publishes must check `CHANGES.md` first.

`cowork/programme-records` (merge register item 6) and `cowork/live-site-checks` also record this for the P1 theme. This finding adds the other two copy-of-live drafts.

---

## Finding 3 — Judge.me core embed shows shoppers nothing

**Finding:**
The Judge.me core app embed is on, but renders no visible element on the homepage or product pages:
- no floating reviews tab
- no trust badge
- no medals
- no star badges on home, collection or product pages

On every page it loads a settings script of about 34 KB (`window.jdgmSettings`), three style blocks and the Judge.me loader. Its product JSON-LD is already off, so switching it off removes no structured data.

**Evidence:**
- Live page DOM checked on homepage and `/products/crxst-rz-t-shirt` after scripts loaded (16 Oct): 0 visible Judge.me elements.
- `window.jdgmSettings`:
  - `floating_reviews_tab_install_preference: "none"`
  - `trust_badge_enabled: false`
  - `judgeme_medals_install_preference: false`
  - `preview_badge_*_install_preference: false`
  - `verified_reviews_count_badge_install_preference: false`
  - `enable_json_ld_products: false`
- `config/settings_data.json` block 14060646107696862457 (`judge-me-reviews/blocks/judgeme_core`) has `disabled: false`.

**Why it matters:**
It costs page weight on every page for no visible output. That's a small Core Web Vitals cost. Review request emails are sent by Judge.me's backend, not this embed.

**Confidence:** High

**Recommended action:**
George decides (task C). If he doesn't want a floating tab or trust badge, switch the embed off.

---

## Finding 4 — Judge.me cart-drawer embed outputs only a hidden div

**Finding:**
The cart-drawer widget embed (block 13047258039897440615, `widget_type: review-widget`) is on. Its only output is a hidden `div#jdgm-cart-drawer-source` on every page. The site never opens a cart drawer, so it can never show anything.

**Evidence:**
Live DOM on homepage and tee product page (16 Oct): `DIV#jdgm-cart-drawer-source`, not visible. Settings block as above.

**Why it matters:**
A small, safe page-weight win.

**Confidence:** High

**Recommended action:**
Switch it off (task A, pre-approved).

---

## Finding 5 — Tee pages promise same-day dispatch from four separate sources; the theme editor can only scope two of them to tees

**Finding:**
All tees are print on demand, but tee product pages say they ship today. All products share one template (`templates/product.json`), so every setting below applies to every product unless scoped.

1. **Delivery line**
   - Location: section `main` (`crooks-exhibit-record`), setting `in_stock_text`.
   - Text: "Order before 18:00 and it ships today (Mon–Sat)".
   - Theme editor label: "In-stock delivery line".
2. **Dispatch state line**
   - Location: same section. Settings `dispatch_show: true`, `dispatch_today` "Ordered now — leaves today", `dispatch_tomorrow`, `dispatch_next_open`. Cutoff 18:00, Monday to Saturday.
   - Rendered client-side by `assets/crooks-record.js` `renderDispatch()`.
3. **Custody accordion step 01 "Logged"**
   - Location: block `s1` (`custody_step`).
   - Text: "Orders placed before 18:00 are dispatched the same day, Monday to Saturday. After 18:00, the next dispatch day."
   - One block shared by every product.
4. **Sitewide status bar**
   - Location: `sections/header-group.json`, section `crooks_status_bar`, block `m1`.
   - Text: "FREE UK SHIPPING OVER £30 // ORDER BY 18:00 FOR SAME-DAY DISPATCH".
   - Shown on every page.

The section already has a made-to-order switch (`sections/crooks-exhibit-record.liquid` lines 361–403). Products tagged with the value of setting `made_to_order_tag` (currently `made-to-order`) get these changes:
- They show `made_to_order_text` (currently "Made to order · Ships in 9–16 days") in place of source 1.
- They do not render source 2.

No product carries `made-to-order` today. The tag `tee` is on all 17 T-shirt products (3 active, 14 draft) and on no other product.

Sources 3 and 4 cannot be scoped to tees from the theme editor.

The stock labels also imply held stock on print-on-demand tees:
- Labels: `label_in_stock` "IN STOCK" and `label_low` "[n] LEFT IN SIZE [size]" (threshold 3), rendered by `crooks-record.js` `render()`.
- Cause: tee variants are inventory-tracked with "continue selling", so any size recorded at 1–3 units shows "[n] LEFT".

**Evidence:**
- Theme file contents via Admin API (16 Oct; checksums in Finding 1).
- Live tee page DOM showing `p.crk-stockline[data-crk-delivery]` with the ships-today text.
- Admin API products query for `tag:tee` and `tag:'made-to-order'`.
- Variant `inventoryPolicy: CONTINUE`, `tracked: true`.

**Why it matters:**
- **Commercial:** a false dispatch promise on every tee invites "where's my order" contacts and complaints.
- **GEO:** AI shopping answers will quote the page text as fact.
- **Merchant feed:** handling-time accuracy (see `03-merchant-feed-handoff` section D, not visible to this session).

**Confidence:** High

**Recommended action:**
- **Theme editor, after George gives the dispatch time:** set `made_to_order_text` to "Printed to order. Dispatched within [N] working days." and set `made_to_order_tag` to `tee`. This fixes sources 1 and 2 on tees only.
- **Held code work:** make custody step 01 respect the made-to-order tag, and skip the stock and low-stock lines for made-to-order products.
- **George's wording call:** the sitewide status bar (source 4).
- **Products workstream:** whether tee variants should stop tracking inventory.

**Related workstreams (checked 18 Oct):**
- `cowork/live-site-checks` Finding 1 measured the same problem on the live site. It proposes product-data tags all 17 tees `made-to-order`. This branch's route (a) reaches the same result with no product edits, by pointing the theme setting at the existing `tee` tag. George picks one route (STATUS Q4).
- `cowork/product-data` D2 turns off inventory tracking on the 30 tee variants. That stops the "[n] LEFT" line and the negative stock.
- "IN STOCK" still shows after D2. `crooks-record.js` `render()` prints `label_in_stock` for every available variant, tracked or not, and that label is shared by every product. Removing it from tees needs code (held theme work).
- `cowork/merchant-center` Q3 asks George for the same tee dispatch time, for the feed handling time. One answer covers both.

---

## Finding 6 — Outerwear collection is live; footer SHOP slot 6 is empty

**Finding:**
`/collections/outerwear` returns H1 "OUTERWEAR" with 2 products (HydroCuff Windbreaker, Double-Agent Puffa). In the footer SHOP column (`sections/footer-group.json`, section `crooks_footer_log`, block `c1`), `label_6` and `url_6` are empty. The live SHOP column shows NEW, TEES, DENIM, SWEATS, ACCESSORIES.

**Evidence:**
Live storefront fetch and footer DOM (16 Oct). Theme file as above.

**Why it matters:**
Adding the link gives the new collection a sitewide internal link from every page, for crawl discovery and topical linking.

**Confidence:** High

**Recommended action:**
Task B, pre-approved under change log C-001: label `OUTERWEAR`, link `/collections/outerwear`.

---

## Finding 7 — A different theme went live on 18 Oct; the "approved fixes" work copy is now stale

**Finding:**
Lineage worked out from file checksums (Admin API, 18 Oct 20:10 BST):

| Theme | Created (BST) | What it is |
|---|---|---|
| BACKUP of live 18 Oct (do not edit), 207468822871 | 18:15 | Identical to SEO round 2, the old live. Good rollback for the old live only |
| live + 18 Oct approved fixes, 207468855639 | 18:15 | Old live plus footer OUTERWEAR (`footer-group.json` 74b8fcd0…) and tee wording (`product.json` 4d38a614…) |
| Mobile UX + Reviews 18 Oct, 207466594647 | 17:50 | Someone else's. New `crooks-record.js`, `crooks-exhibit-record.liquid`, `crooks-ux.css`, header, index and product templates |
| T-shirt Week launch, 207470887255 | 18:42 | Approved-fixes copy plus T-shirt Week on (`crk_tw_on: true`) |
| TW launch + Mobile UX + Puffa (18 Oct), 207472165207 | 19:01 | Merge of the three above |
| **live 18 Oct + evening fixes, 207475147095 (MAIN)** | 19:37 | Copy of the TW+MUX+Puffa merge, edited at 19:55 (`layout/theme.liquid`, `header-group.json`, `crooks-ux.css`, tee-week and terminal JS). Now published |
| live 18 Oct + colour photos, 207476752727 | 20:04 | Copy of live. `crooks-record.js` and `crooks-exhibit-record.liquid` edited at 20:09 |

**Evidence:** Admin API `themes` list, plus `checksumMd5` on 12 key files across all 8 themes.

**Why it matters:**
- Publishing the approved-fixes copy now would remove the T-shirt Week launch, the Mobile UX work, the Puffa work and the evening fixes from the live site.
- The colour-photos copy edits the same two PDP files the tee stock fix needs. Two copies of live are being changed in parallel, and whichever is published second wipes the other.
- The current live theme has no backup. The 18 Oct backup is of the old live.

**Confidence:** High

**Recommended action:**
- Retire the approved-fixes copy (don't publish it).
- Make one integration theme at a time: whoever owns the colour-photos copy finishes and publishes, then the next change starts from a fresh copy of live.
- Back up the current live before the next publish.

---

## Finding 8 — Live state of this workstream's items, 18 Oct 20:15 BST

**Finding:**
- **Footer** (`sections/footer-group.json` block `c1`): `label_5`/`url_5` = OUTERWEAR, `/collections/outerwear`; `label_6`/`url_6` = ACCESSORIES. **B is done.**
- **Product template main section:**
  - `made_to_order_text` "Printed to order. Dispatched within 2–3 working days.", `made_to_order_tag` `tee`.
  - Custody step s1: "In-stock pieces ordered before 18:00 are dispatched the same day … T-shirts are printed to order and dispatched within 2–3 working days."
  - Custody step s3: Tracked 24 typically 1–2, Tracked 48 typically 2–3 working days, "estimated delivery aims, not guaranteed dates".
  - A new promises list shows the made-to-order line in place of promise 1 on tees.
  - **The wording half of D is done.**
- **App embeds** (`config/settings_data.json`): Judge.me core and Judge.me cart drawer are both `disabled: false`. Orderify, Mida and Partner Hub are on. **A and C are not done.**
- **Stock line:** the live section now also renders the stock line server-side (around lines 373–408) as well as in `crooks-record.js` `render()` (around lines 434–450). Neither checks the made-to-order flag, so tees show "IN STOCK", and "[n] LEFT" when a tracked quantity is 1–3. Tracking is now off on the 3 live tees (C-009), which removes "[n] LEFT" there. **"IN STOCK" remains.**
- **Schema:** `snippets/crooks-schema-shipping.liquid` sends `handlingTime` 0–2 and `transitTime` 1–2 for every product. Tees should be 2–3 handling (#1). The Tracked 48 rate it describes should be 2–3 transit (#3).
- **Status bar** (`sections/header-group.json`, `crooks_status_bar`), three messages:
  - m1 "FREE UK DELIVERY OVER £30"
  - m2 "ORDER BY 6PM — DISPATCHED TODAY"
  - m3 "FREE SIZE SWAPS WITHIN 14 DAYS"

  m2 promises same-day dispatch on tee pages too, against decision #1.

**Evidence:**
- Live theme 207475147095 files, read 18 Oct 20:10–20:20 BST.
- Tee page check on the Crooks Express tee, White / XL, in George's Chrome. The preview theme was byte-identical to live for the product template, section and script.

**Why it matters:**
"IN STOCK" on a print-on-demand tee and a sitewide "DISPATCHED TODAY" are the last false tee claims left on the site.

**Confidence:** High

**Recommended action:**
Code handoff in `artifacts/code-handoff-tee-stock-and-schema.md`. Status bar wording needs George's go.

---

## Finding 9 — The storefront is password-locked

**Finding:**
Shopify Online Store password protection is **enabled**. Every public URL (`/`, `/products/crooks-express-t-shirt`, `/collections/outerwear`) redirects to `/password` ("Enter password"). The site served normally without a login on 16 Oct around 20:30 BST.

**Evidence:**
- Admin API `onlineStore { passwordProtection { enabled } }` returns `true` (18 Oct 20:14 BST).
- A cookieless fetch of three URLs ends at `/password`.

**Why it matters:**
- No sales from anyone without the password.
- Google crawls a password page.
- Merchant Center can disapprove products whose landing pages don't load.

**Confidence:** High

**Recommended action:**
George confirms whether it's an intentional drop lock. If not, he turns it off in Online Store → Preferences. Not a theme setting, so this session hasn't touched it.
