# Workstream: Live theme — Theme editor settings and App embeds

**Branch:** cowork/theme-editor  
**Owner:** Cowork session  
**Last updated:** Sun 18 Oct 2026, 20:30 UK  
**Priority:** P0 (store password-locked, see Blocker 1), otherwise P1  
**Overall status:** BLOCKED

George's answers of 18 Oct are in [ANSWERS.md](ANSWERS.md) and are applied below. The work-copy plan in ANSWERS.md ("publish 'live + 18 Oct approved fixes'") is **out of date and must not be followed**: a different theme went live at about 19:37 BST (FINDINGS 7).

## Objective

Make George's approved theme fixes on the live theme without losing anyone else's live work:

- **A.** Judge.me cart-drawer embed off.
- **B.** OUTERWEAR in the footer SHOP column.
- **C.** Judge.me core embed off (decision #22).
- **D.** Tee pages tell the truth: "Printed to order. Dispatched within 2–3 working days." (decision #1), with no "IN STOCK" or "[n] LEFT" (decision #2).

Keep Orderify (decision #26). Never publish "Claude P1 fixes".

## Current state

The live theme is now **"CROOKSLDN — live 18 Oct + evening fixes"** (207475147095). Other sessions built it tonight from "TW launch + Mobile UX + Puffa", and it already contains B and the wording half of D. Checked against the live theme files at 20:15 BST (FINDINGS 7 and 8).

| Item | Live now | Who did it |
|---|---|---|
| B. Footer OUTERWEAR | **Done.** SHOP slot 5 is OUTERWEAR and ACCESSORIES moved to slot 6 | Another session, tonight |
| D. Tee wording and `tee` tag | **Done.** Made-to-order line "Printed to order. Dispatched within 2–3 working days.", tag `tee`, custody steps reworded | Another session, tonight |
| A. Judge.me cart-drawer embed | **Still on** | Not done |
| C. Judge.me core embed | **Still on** | Not done |
| D. No "IN STOCK" / "[n] LEFT" on tees | **Not done.** A live tee shows "IN STOCK" after a size is picked. Needs code | Held theme work (`artifacts/code-handoff-tee-stock-and-schema.md`) |
| Tee `handlingTime` in product schema | **Not done.** Every product still says 0–2 days handling and 1–2 days transit. Needs code | Same handoff file |
| Status bar | Now three rotating messages. m2 reads **"ORDER BY 6PM — DISPATCHED TODAY"** sitewide, tee pages included | George's wording call |

This session has changed nothing on any theme. CHANGES.md is still empty.

## Completed

- Audited the before state on 16 Oct and rechecked it on 18 Oct (FINDINGS 1–6).
- Read George's answers and owner decisions #1, #2, #3, #7, #22 and #26.
- Traced the lineage of all 18 Oct themes by file checksum (FINDINGS 7).
- Read the live footer, product template, status bar, app embeds, and stock-line and schema code (FINDINGS 8).
- Page check on the Crooks Express tee, White / XL: it shows "IN STOCK" after a size is picked, and the 2–3 day line is present.
  - George's Chrome was previewing "TW launch + Mobile UX + Puffa", not live.
  - That theme's `templates/product.json`, `sections/crooks-exhibit-record.liquid` and `assets/crooks-record.js` have the same checksums as live, so live behaves the same.
  - The public site couldn't be checked because it's password-locked.
- Found the store password lock and confirmed it with the Admin API (`onlineStore.passwordProtection.enabled = true`). Told George at 20:16 BST (FINDINGS 9).
- Wrote the exact code locations for the tee stock lines and schema timings (`artifacts/code-handoff-tee-stock-and-schema.md`).

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — Storefront password-locked

**Blocking:** All public traffic, sales, crawling and live-page checks.  
**Needs:** George to confirm the lock is intentional (a drop lock), or to turn it off in Online Store → Preferences → Password protection.  
**From:** George  
**Severity:** P0  
**Can work around it?:** For checks only. Logged-in preview still works. Shoppers can't get in.  
**Workaround:** None for customers.

### Blocker 2 — Someone is building another copy of live right now

**Blocking:** A and C. Any write to live or to a copy of it.  
**Needs:** George to say who owns "CROOKSLDN — live 18 Oct + colour photos" (207476752727) and whether it will be published.
- That copy was made from live at 20:04 BST and edited at 20:09 BST.
- Its edits are to `assets/crooks-record.js` and `sections/crooks-exhibit-record.liquid`, the same two files the tee stock fix needs.
- Whichever copy is published second wipes the first one's changes.

**From:** George  
**Severity:** P1  
**Can work around it?:** No.  
**Workaround:** None. Writing now risks wiping someone's work.

### Blocker 3 — No route for this session to write the live theme

**Blocking:** A and C on live.  
**Needs:** One of these:
- George flips the two Judge.me toggles himself in Theme editor → App embeds. About a minute.
- The theme editor renders in Claude's Chrome tab. It's been blank on three tries.
- The toggles go into the next theme copy before George publishes it.

The Shopify connector can't write the published theme (change-log C-001).  
**From:** George  
**Severity:** P2  
**Can work around it?:** Yes, through the next copy to be published.  
**Workaround:** Put the toggles into that copy.

## Waiting on George

1. **Password lock:** is it a deliberate T-shirt Week drop lock? If not, turn it off (Online Store → Preferences → Password protection).
2. **"live 18 Oct + colour photos":** whose is it, and is it the next theme to be published?
   - If yes, its owner should also switch off the two Judge.me embeds and apply the tee stock fix in that copy before you publish it.
   - If not, flip the two Judge.me toggles on live yourself (Theme editor → App embeds → "Judge.me" and "Judge.me cart drawer widget" → off → Save). Leave Orderify, Mida and Partner Hub on.
3. **Status bar m2:** it now says "ORDER BY 6PM — DISPATCHED TODAY" on every page, tees included. Proposed replacement: "IN-STOCK ORDERS BY 6PM DISPATCHED TODAY". Say yes, or give other wording.

## Waiting on external systems

Google recrawl of the footer OUTERWEAR link and the tee wording, once the password lock is off.

## Next actions

1. George settles the password lock. It's P0, and nothing else matters while shoppers can't get in.
2. George names the next theme to publish. Apply A, C and the tee stock and schema code there. Preview-check a tee and a hoodie, then George publishes.
3. Status bar m2 wording, once George says yes.
4. After the publish: check a live tee (no "IN STOCK", 2–3 day line, `handlingTime` 2–3 in the JSON-LD), a live hoodie (unchanged, "IN STOCK" and same-day line), the footer and the Judge.me scripts. Then log it.

## Expected impact

**Commercial:** Very high while the password lock is on. Otherwise Medium: the tee claims are honest now, apart from "IN STOCK".  
**SEO:** High if the password lock persists (Google sees a password page). Otherwise Low–Medium.  
**GEO:** Low–Medium. The schema handling time feeds AI shopping answers.  
**Confidence:** High on the findings.

## Notes for the orchestrator

- **Do not publish "CROOKSLDN — live + 18 Oct approved fixes" (207468855639).**
  - It was copied from the old live theme (SEO round 2) at 18:15 BST.
  - Publishing it now would wipe out tonight's TW launch, Mobile UX, Puffa and evening fixes.
  - Everything useful in it (footer OUTERWEAR, tee wording) is already live.
- The backup "CROOKSLDN — BACKUP of live 18 Oct (do not edit)" is a backup of the old live (SEO round 2), not the current live. The current live has no backup.
- Overlap on tees is unchanged: product-data turned tracking off on the 3 live tees (C-009); merchant-center owns the feed handling time; the stock lines and schema are code.
- The repo is public. This branch leaves out admin URLs and exact stock counts.
