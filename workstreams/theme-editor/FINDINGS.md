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
