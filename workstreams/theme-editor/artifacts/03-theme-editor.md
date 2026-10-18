# 03 — Theme editor results (live theme)

Session scope: live theme only, Theme editor settings and App embeds only, no code edits, no publishing.
Date: Fri 16 Oct 2026. All times BST.

## Live theme identified (20:26–20:35)

- Published theme: **CROOKSLDN — SEO round 2 (from live 16 Oct)**, ID 207329132887, Horizon 3.5.0 base. Confirmed `role: main` from a cookieless storefront fetch and from the Admin API.
- Live theme last saved 14:33 (Admin API `updatedAt`). File timestamps: `config/settings_data.json` 13:17; `sections/footer-group.json`, `sections/header-group.json`, `templates/product.json` 12:49; `sections/crooks-exhibit-record.liquid` 14:03 (a code push, not from this session).
- Held theme "CROOKSLDN — Claude P1 fixes (copy of live 16 Oct)": not opened.
- Draft "CROOKSLDN — Puffa heat reaction (from live 16 Oct)" was saved about 19:55, so someone was working in theme drafts this evening.

## Recheck, Sun 18 Oct 16:34

- Same published theme (207329132887, `role: MAIN`). Theme `updatedAt` is still 16 Oct 14:33.
- MD5 checksums of `config/settings_data.json`, `sections/footer-group.json`, `sections/header-group.json`, `templates/product.json`, `sections/crooks-exhibit-record.liquid` and `assets/crooks-record.js` are unchanged (see FINDINGS.md, Finding 1). Every before state below still holds.
- The theme editor still renders as a blank white page in Claude's Chrome tab, on three attempts across 16 and 18 Oct. No save attempted.

## Status

| Task | Status | Before | After | Time | Live-page check |
|---|---|---|---|---|---|
| A. Judge.me cart-drawer embed off | Not changed. Waiting for George to confirm nobody else is editing the live theme. | ON (block 13047258039897440615, `widget_type: review-widget`) | — | — | Before: `div#jdgm-cart-drawer-source` is output on every page, hidden, renders nothing. |
| B. OUTERWEAR in footer SHOP slot 6 | Not changed. Same wait. | Block `c1`: `label_6: ""`, `url_6: ""`. Live SHOP column: NEW, TEES, DENIM, SWEATS, ACCESSORIES | — | — | Target `/collections/outerwear` is live: H1 "OUTERWEAR", 2 products. |
| C. Judge.me core embed | Waiting on George's decision. | ON (block 14060646107696862457) | — | — | Findings below. |
| D. Tee dispatch wording | Waiting on George's dispatch time and go-ahead. | See below | — | — | Findings below. |

## App embeds before any change (`config/settings_data.json` → `current.blocks`)

| App embed | State | Rule |
|---|---|---|
| Forms | ON | — |
| Omnisend | ON | — |
| Judge.me core | ON | Task C, George decides |
| Orderify (script_js) | ON | Keep on |
| Judge.me cart-drawer widget | ON | Task A, switch off |
| Notify Me | OFF | — |
| Mida recorder | ON | Keep on |
| Crooks Partner Hub (creator-gift) | ON | Keep on |

## C. What the Judge.me core embed shows on the live site

Checked homepage and a tee product page on the live theme, after the scripts had loaded.

- No floating reviews tab. Judge.me's own setting `floating_reviews_tab_install_preference` is `none`, and no tab element is created.
- No trust badge (`trust_badge_enabled: false`), no medals (`judgeme_medals_install_preference: false`), no verified-count badge, no star preview badges on home, collection or product pages (all install preferences `false`).
- Visible Judge.me elements on the page: **none**.
- What it does load on every page: a ~34 KB settings script (`window.jdgmSettings`), three style blocks and the Judge.me loader script.
- Judge.me JSON-LD for products is off (`enable_json_ld_products: false`), so switching the core embed off removes no structured data.
- The cart-drawer source div above is output whether or not the core embed is on.

Conclusion for George: the core embed currently shows shoppers nothing. Switching it off removes page weight only. Review request emails are sent by Judge.me's backend and keep working either way.

## D. Where the tee "ships today" wording lives

Every product (tees, denim, sweats, outerwear, accessories) uses the same template, `templates/product.json` (section IDs `template--32222060151127__*`). Four sources put same-day or stock wording on tee pages:

1. **Delivery line** — `templates/product.json` → section `main` (type `crooks-exhibit-record`) → setting `in_stock_text` = "Order before 18:00 and it ships today (Mon–Sat)". Theme editor label: "In-stock delivery line". Shared by every product.
2. **Dispatch state line** — same section, `dispatch_show: true`, with `dispatch_today` "Ordered now — leaves today", `dispatch_tomorrow`, `dispatch_next_open`, cutoff 18, days Mon–Sat. Rendered by `assets/crooks-record.js` `renderDispatch()`.
3. **Custody accordion, step 01 "Logged"** — same section → block `s1` (`custody_step`) body: "Orders placed before 18:00 are dispatched the same day, Monday to Saturday. After 18:00, the next dispatch day." Shared by every product. Collapsed by default.
4. **Sitewide status bar** — `sections/header-group.json` → section `crooks_status_bar` → block `m1`: "FREE UK SHIPPING OVER £30 // ORDER BY 18:00 FOR SAME-DAY DISPATCH". Every page.

### What the theme editor can scope to tees

The section already has a made-to-order switch (`sections/crooks-exhibit-record.liquid` lines 361–403). If a product carries the tag named in the setting **"Made-to-order tag"** (`made_to_order_tag`, currently `made-to-order`), it shows **"Made-to-order delivery line"** (`made_to_order_text`, currently "Made to order · Ships in 9–16 days") instead of items 1 and 2.

- No product carries `made-to-order` today (Admin API check).
- The tag `tee` is on all 17 T-shirt products (3 active, 14 draft) and on nothing else.

Proposed theme-editor-only change, two settings on the Default product template → Exhibit record section:

| Setting | Before | After |
|---|---|---|
| Made-to-order delivery line | Made to order · Ships in 9–16 days | Printed to order. Dispatched within [N] working days. |
| Made-to-order tag | made-to-order | tee |

Effect: the 17 tees show the printed-to-order line and lose the "Ordered now — leaves today/tomorrow" line. Non-tee products keep their current wording. No product, tag or metafield edits needed.

### What the theme editor cannot scope to tees (for the held theme work)

- **Item 3, custody step "Logged"**: one block shared by every product. Needs code in `sections/crooks-exhibit-record.liquid` (custody loop around line 589) to swap the body when the product carries the made-to-order tag, or a sitewide rewording George approves.
- **Item 4, status bar `m1`**: sitewide. Needs a wording decision (e.g. limit it to in-stock items) or code.
- **Stock labels**: `label_in_stock` "IN STOCK" and `label_low` "[n] LEFT IN SIZE [size]" (threshold 3), rendered by `assets/crooks-record.js` `render()`. Tee variants are inventory-tracked with "continue selling", so any tee size recorded at 1–3 units shows a low-stock line (at least one active tee size does today). That implies stock on a print-on-demand item. Fix is either code (skip stock/low lines for made-to-order products) or product data (stop tracking inventory on tee variants), which belongs to the products session.
