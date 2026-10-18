# Workstream: Live theme — Theme editor settings and App embeds

**Branch:** cowork/theme-editor  
**Owner:** Cowork session  
**Last updated:** Sun 18 Oct 2026, 17:15 UK  
**Priority:** P1  
**Overall status:** BLOCKED

## Objective

Make the approved fixes on the **live** theme ("CROOKSLDN — SEO round 2 (from live 16 Oct)"), using only Theme editor settings and App embeds. No code edits, no publishing.

- **A.** Switch off the Judge.me cart-drawer embed. Pre-approved.
- **B.** Add OUTERWEAR (`/collections/outerwear`) to the footer SHOP column, slot 6. Pre-approved under C-001.
- **C.** Decide whether the Judge.me core embed also goes off. Waiting on George.
- **D.** Replace "Order before 18:00 and it ships today" on print-on-demand tee pages with true wording. If the theme editor can't scope it to tees, record exactly where the text lives for the held code work.

This is the only workstream allowed to change the live theme.

## Current state

Nothing has been changed on the live theme.

- **Done, read-only:**
  - Every setting this workstream touches has been audited on the live theme, and the before state is recorded.
  - The live theme was rechecked on 18 Oct: no file this workstream touches has changed since 16 Oct 14:33 BST.
- **Waiting on George:**
  - A and B are ready. They need George to confirm nobody else is editing the live theme. The brief requires that confirmation before any save.
  - C needs his decision.
  - D needs his tee dispatch time.
- **Tooling problem:** the Shopify theme editor loads as a blank white page in Claude's Chrome tab, on three attempts across 16 and 18 Oct. Saves can't be made until it renders.

## Completed

- Audited the live app embed states (8 embeds, see `artifacts/before-state-live-theme.md`).
- Audited Judge.me core embed output on the live site. It shows nothing (FINDINGS 3).
- Audited Judge.me cart-drawer embed output. It is a hidden div only (FINDINGS 4).
- Audited footer SHOP column block `c1`. Slot 6 is empty. Checked `/collections/outerwear` is live with 2 products (FINDINGS 6).
- Traced all four sources of the same-day dispatch claim on tee pages, and which of them the theme editor can scope to tees (FINDINGS 5).
- Prepared the exact theme-editor change for D, pending the dispatch time (FINDINGS 5, NEXT).
- Recorded file checksums for drift detection (FINDINGS 1).
- Identified the risk that publishing 16 Oct copy-of-live drafts reverts live changes (FINDINGS 2).

Nothing has been deployed, staged or changed live.

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — Confirmation that nobody else is editing the live theme

**Blocking:** A and B saves. Every later save too.  
**Needs:** George to say "clear, nobody else is editing the live theme".  
**From:** George  
**Severity:** P1  
**Can work around it?:** No. The brief makes this a hard rule.  
**Workaround:** None.

### Blocker 2 — Theme editor renders blank in Claude's Chrome tab

**Blocking:** All theme editor and App embed saves (A, B, C, D).  
**Needs:** The theme editor (`Online Store → Themes → Customize` on the live theme) to render in the Claude in Chrome tab group. The storefront and Shopify admin pages load fine. Only the editor's embedded frame is white. George may need to open Chrome, check nothing is waiting on him, and open the editor once himself.  
**From:** George (Chrome on his computer)  
**Severity:** P1  
**Can work around it?:** Only with George's explicit approval.  
**Workaround:** Apply the same settings through the Shopify Admin API by writing `config/settings_data.json` and `sections/footer-group.json`. The brief does not allow this route: it says Theme editor only, no code edits. Not used.

### Blocker 3 — Tee dispatch time

**Blocking:** D.  
**Needs:** The number of working days from a tee order to dispatch.  
**From:** George  
**Severity:** P1 (a false shipping promise is on live tee pages now)  
**Can work around it?:** No. Inventing a number would be another false promise.  
**Workaround:** None.

## Waiting on George

**How to answer:** reply in this workstream's Cowork chat, or add `workstreams/theme-editor/ANSWERS.md` on this branch with one numbered answer per question. Then send the chat the word "answered". This session reads both places before making any change.

1. **Concurrent editing:** is anyone else editing the live theme ("CROOKSLDN — SEO round 2 (from live 16 Oct)") right now? No save happens until the answer is "no".
2. **Theme editor won't render:** Online Store → Themes → live theme → Customize loads as a blank white page in Claude's Chrome tab group. Answer (a) or (b):
   - (a) George opens the theme editor once in Chrome himself, clears any prompt or dialog waiting there, and confirms it loads; or
   - (b) George allows the fallback: the same settings written through the Shopify Admin API, which counts as a file write and is outside the brief's theme-editor-only rule.
3. **Tee dispatch time:** how many working days from a tee order to dispatch? A number, or a range such as "3–5".
4. **D approach:** approve both of these on the Default product template → Exhibit record section?
   - "Made-to-order delivery line" → `Printed to order. Dispatched within [N] working days.`
   - "Made-to-order tag" → `tee`

   This affects tee pages only. Other products keep "Order before 18:00 and it ships today". Yes, or give replacement wording.
5. **Judge.me core embed (task C):** off, or keep on? It shows shoppers nothing today: no floating tab, no trust badge, no stars, no medals. Review request emails keep working either way.
6. **Sitewide status bar:** it reads "FREE UK SHIPPING OVER £30 // ORDER BY 18:00 FOR SAME-DAY DISPATCH" on every page, tee pages included. Answer (a), (b) or (c):
   - (a) keep it as it is;
   - (b) replace it with George's wording; or
   - (c) leave it to the held theme work.

## Waiting on external systems

None yet. After B is live, Google needs to recrawl to pick up the new footer link.

## Next actions

1. **D**, once the dispatch time is known: removes a false same-day promise from every tee page. Biggest commercial risk.
2. **B**: a sitewide internal link to the new Outerwear collection.
3. **A**: removes a dead embed.
4. **C**, if George says off: removes about 34 KB of unused Judge.me settings and scripts from every page.
5. Hand the out-of-scope tee claims to their owners:
   - custody step 01 and the stock or low-stock labels → held code work
   - the status bar → George's wording
   - tee inventory tracking → products workstream

## Expected impact

**Commercial:** Medium. D stops promising same-day dispatch on print-on-demand tees, which drives "where's my order" contacts and complaints. B surfaces a new collection from every page.  
**SEO:** Low–Medium. B adds a sitewide internal link to `/collections/outerwear`. A and C are small page-weight gains.  
**GEO:** Low–Medium. AI shopping answers quote on-page shipping text, so the tee dispatch wording needs to be true.  
**Confidence:** Medium. The findings are high confidence; the size of the effect is not measured.

## Notes for the orchestrator

- The repo was empty when this branch was created: no `main`, no other workstream branches. This branch is an orphan root, so `main` was never committed to.
- The repo is **public**. This branch leaves out admin URLs and exact stock counts. Everything else in it, including the theme name and ID, the app embeds and the on-page wording, can already be seen from the storefront's page source.
- `CHANGES.md` is empty because nothing has been changed live.
- The brief's files `09-performance.md`, `01-collections-internal-linking.md` and `03-merchant-feed-handoff.md` section D were never available to this session.
- Results file: the brief asked for `/mnt/project-files/seo/cowork-results/03-theme-editor.md`, which this session can't reach. It is kept in this branch at `artifacts/03-theme-editor.md`.
