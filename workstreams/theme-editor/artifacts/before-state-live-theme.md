# Before state — live theme settings this workstream will touch

Theme: "CROOKSLDN — SEO round 2 (from live 16 Oct)", ID 207329132887, role MAIN.

Read via the Shopify Admin API on 16 Oct 2026. Rechecked 18 Oct 16:34 BST: identical checksums (see FINDINGS.md, Finding 1).

## App embeds — `config/settings_data.json` → `current.blocks`

| Block ID | App embed | `disabled` | Rule for this workstream |
|---|---|---|---|
| 13768625480086291342 | Shopify Forms | false | Leave |
| 1513253815146976218 | Omnisend | false | Leave |
| 14060646107696862457 | Judge.me — judgeme_core | false | Task C, George decides |
| 13379946638294866266 | Orderify — script_js | false | **Never switch off** (customers cancel and edit orders with it) |
| 13047258039897440615 | Judge.me — cart_drawer_widget (`widget_type: review-widget`) | false | Task A, switch off |
| 11349500561483629931 | Notify Me | true | Leave |
| 15599951759576395258 | Mida recorder | false | **Never switch off** |
| 51900412247342673 | Crooks Partner Hub — creator-gift | false | **Never switch off** |

Judge.me review display and stars must not be turned on (George's decision).

## Footer SHOP column — `sections/footer-group.json` → `crooks_footer_log` → block `c1`

```json
"heading": "SHOP",
"label_1": "NEW",          "url_1": "shopify://collections/new",
"label_2": "TEES",         "url_2": "shopify://collections/tees",
"label_3": "DENIM",        "url_3": "shopify://collections/denim",
"label_4": "SWEATS",       "url_4": "shopify://collections/sweats",
"label_5": "ACCESSORIES",  "url_5": "shopify://collections/accessories",
"label_6": "",             "url_6": ""
```

Target for task B: `label_6` = `OUTERWEAR`, `url_6` = the Outerwear collection (`/collections/outerwear`).

## Product page dispatch settings — `templates/product.json` → section `main` (`crooks-exhibit-record`)

```json
"in_stock_text": "Order before 18:00 and it ships today (Mon–Sat)",
"made_to_order_text": "Made to order · Ships in 9–16 days",
"made_to_order_tag": "made-to-order",
"dispatch_show": true,
"dispatch_cutoff_hour": 18,
"dispatch_days": "1,2,3,4,5,6",
"dispatch_timezone": "Europe/London",
"dispatch_today": "Ordered now — leaves today",
"dispatch_tomorrow": "Ordered now — leaves tomorrow",
"dispatch_next_open": "Ordered now — leaves Monday",
"label_in_stock": "IN STOCK",
"label_low": "[n] LEFT IN SIZE [size]",
"low_stock_threshold": 3
```

Custody block `s1` (label "Logged"): "Orders placed before 18:00 are dispatched the same day, Monday to Saturday. After 18:00, the next dispatch day."

## Status bar — `sections/header-group.json` → `crooks_status_bar`

- `m1`: "FREE UK SHIPPING OVER £30 // ORDER BY 18:00 FOR SAME-DAY DISPATCH"
- `m2`: "FREE SIZE SWAPS // EASY RETURNS, NO PRINTER NEEDED"

## How the made-to-order switch works (`sections/crooks-exhibit-record.liquid` lines 360–403)

```liquid
assign crk_mto = false
if product.tags contains section.settings.made_to_order_tag
  assign crk_mto = true
endif
{%- if crk_mto and section.settings.made_to_order_text != blank -%}
  <p class="crk-stockline" data-crk-delivery ...>{{ section.settings.made_to_order_text }}</p>
{%- elsif section.settings.in_stock_text != blank -%}
  <p class="crk-stockline" data-crk-delivery ...>{{ section.settings.in_stock_text }}</p>
  {%- if section.settings.dispatch_show -%} ... dispatch state line ... {%- endif -%}
{%- endif -%}
```

So setting `made_to_order_tag` to `tee` swaps the delivery line and drops the "leaves today" line on tagged products only. The custody accordion (around line 589) and the stock labels in `crooks-record.js` do not check this tag.
