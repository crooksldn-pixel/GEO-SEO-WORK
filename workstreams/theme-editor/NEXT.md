# Next

## Do next

Before every save, recheck the live theme file checksums against FINDINGS 1. If they differ, stop and ask George. Make one change, save, check the live page, then move to the next.

1. **A — Judge.me cart-drawer embed off.** Needs Blockers 1 and 2 cleared.
   - Theme editor on the live theme → App embeds → "Judge.me cart drawer widget" → off → Save.
   - Live check: on the homepage, `#jdgm-cart-drawer-source` is gone.
   - Live check: Orderify, Mida and Partner Hub are still loading.
   - Log it in `CHANGES.md` with the time.
2. **B — footer OUTERWEAR.** Needs Blockers 1 and 2 cleared.
   - Theme editor → Footer → "crooks-footer-log" section → SHOP column block → slot 6.
   - Label `OUTERWEAR`. Link: pick the Outerwear collection.
   - Save.
   - Live check: the footer SHOP column reads NEW, TEES, DENIM, SWEATS, ACCESSORIES, OUTERWEAR, and the new link goes to `/collections/outerwear`.
3. **D — tee dispatch wording.** Needs Blockers 1–3 cleared and George's approval of the approach.
   - Theme editor → Products → Default product → Exhibit record section.
   - Set "Made-to-order delivery line" to `Printed to order. Dispatched within [N] working days.`
   - Set "Made-to-order tag" to `tee`.
   - Save.
   - Live check on one active tee (`/products/crxst-rz-t-shirt`): the new line shows and there's no "leaves today/tomorrow" line.
   - Live check on one non-tee (e.g. `/products/pink-crsdr-hoodie`): still the original wording.
4. **C — Judge.me core embed.** Only if George says off.
   - App embeds → "Judge.me" core → off → Save.
   - Live check: no `jdgm` scripts or styles on the homepage, and Orderify, Mida and Partner Hub are unaffected.
5. Hand the out-of-scope items over:
   - Custody step 01 "Logged" (sitewide same-day text) and the "IN STOCK" / "[n] LEFT" stock labels on made-to-order products: code in `sections/crooks-exhibit-record.liquid` (custody loop around line 589) and `assets/crooks-record.js` `render()`. Goes to the held theme work.
   - Status bar `m1` "ORDER BY 18:00 FOR SAME-DAY DISPATCH": sitewide, so George needs to choose the wording.
   - Tee variants tracked with "continue selling": products workstream.

## Do not do yet

- Do not publish any theme.
- Do not open or copy from "CROOKSLDN — Claude P1 fixes (copy of live 16 Oct)". It is on hold.
- Do not switch off Orderify, Mida or Crooks Partner Hub.
- Do not turn on Judge.me review display or stars.
- Do not change custody step 01 or the status bar sitewide without George's wording. Both also cover in-stock products, where same-day dispatch is true.
- Do not touch products, collections, menus or Merchant Center. Other sessions own them.
- Do not use the Admin API to write theme files unless George explicitly approves it as a fallback for Blocker 2.

## Decisions still required

- **C:** is the Judge.me core embed on or off?
- **D:** approve the tag-scoped approach and the exact wording.
- **Status bar wording.** "SAME-DAY DISPATCH" sits on tee pages too.
- **Blocker 2 fallback:** if the theme editor still won't render, is an Admin API settings write allowed for A and B?
- **Before any 16 Oct copy-of-live draft is published:** who re-applies the live changes to it (FINDINGS 2)?

## Data still required

- Tee dispatch time in working days.

## Recommended follow-up date

- About 1 Nov 2026, two weeks after B goes live: check Search Console → Links → internal links to `/collections/outerwear`, and the collection's crawl status.
