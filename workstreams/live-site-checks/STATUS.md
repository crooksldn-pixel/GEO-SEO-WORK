# Workstream: Live site checks — CWV baseline, rendered schema, shipping-promise parity, tee stock messaging, mobile popup

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md) and override the open questions and George-blockers below. Anything not answered there is parked and blocks nothing. Project files are on `cowork/project-files-import`. Re-read live values before any write: some approved changes were applied on 18 Oct (change-log C-009 onward).

**Branch:** cowork/live-site-checks  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 17:16 BST  
**Priority:** P1  
**Overall status:** READY TO IMPLEMENT

## Objective

A research-only baseline of the live site, theme "CROOKSLDN — SEO round 2 (from live 16 Oct)". It covers:
- Core Web Vitals
- rendered structured data
- every shipping promise and where they conflict
- what tee pages tell shoppers about stock and dispatch
- the mobile popup's timing and coverage

The brief excluded Shopify, theme, app and Merchant Center edits.

## Current state

The audit ran on 16 Oct. Key facts were re-checked on 18 Oct:
- the live theme hasn't been edited since 16 Oct 13:33 UTC
- tee inventory setup, UK rates and policies are unchanged
- checkout still pre-ticks marketing consent

There are 10 findings with evidence in `FINDINGS.md`; two are P1 (tees showing false stock and dispatch; the pre-ticked consent box). The full 18-item register with owners is in [`artifacts/live-site-checks-report-2026-10-16.md`](artifacts/live-site-checks-report-2026-10-16.md).

**Nothing has been fixed.** One item, the mobile popup, already has a fix built and staged in the held, unpublished "Claude P1 fixes" theme by the 09-performance workstream. No other finding is staged anywhere.

The tee fix belongs to `cowork/product-data`: its item D2, turning off tee inventory tracking, already waits on George's yes. This workstream adds two asks to it: the `made-to-order` tag, and the 14 draft tees.

The held theme is a full copy of live as of 16 Oct, so publishing it after any live theme edit would revert that edit. Theme-side fixes therefore wait on a decision about how to ship (see `NEXT.md`). Policy and product-data fixes don't, and can go ahead now.

## Completed

- **Measured:** PageSpeed Insights mobile and desktop on home, `/products/convict-hoodie-1`, `/collections/sweats`, `/collections/tracksuits` and `/collections/outerwear` (16 Oct 20:28 BST). Covers CrUX field data, lab score, LCP element, TBT, top opportunities and third-party weight.
- **Tested:** Google Rich Results Test and validator.schema.org on home, the Convict hoodie PDP, a tee PDP, the Black Set PDP and `/collections/outerwear`. Rendered JSON-LD was parsed in the browser.
- **Audited:** 14 places that make a shipping promise, against Shopify delivery settings and a live checkout taken to the shipping-method step (no payment).
- **Audited:** tee PDP stock and dispatch lines against Admin API inventory. Screenshotted.
- **Measured:** homepage popup timing and coverage at 390 × 844.
- **Re-verified (18 Oct):** live theme, tee inventory, UK rates, policies and the checkout marketing box.
- **Compared:** the held "Claude P1 fixes" theme to live by checksum across all 499 files. Only `snippets/crack-the-cuffs.liquid` (popup) and `snippets/crooks-schema-site.liquid` (Organization) differ.
- **Not done:** anything prepared, coded, staged or deployed by this workstream.

## Currently working on

Nothing currently running. Waiting for George's answers in `QUESTIONS.md`; he'll say "answered" in this session's chat.

## Blockers

### Blocker 1 — Tee print-on-demand lead time unknown

**Blocking:** the final shipping wording for tees, the tee "made-to-order" line on the PDP, and the tee schema `handlingTime`  
**Needs:** the real order-to-dispatch time for print-on-demand tees  
**From:** George  
**Severity:** P1  
**Can work around it?:** Yes, partly  
**Workaround:** tag the tees `made-to-order` and stop tracking their inventory now. That alone removes "IN STOCK", "leaves tomorrow" and "1 LEFT". The made-to-order line can say "Printed to order" with no number until the lead time is confirmed. Don't use the theme default "9–16 days".

## Waiting on George

All nine questions, with context, options and answer slots, are in [`QUESTIONS.md`](QUESTIONS.md). Proposed wording for Q6 and Q7 is in [`artifacts/proposed-copy.md`](artifacts/proposed-copy.md).

1. Q1 — Tee print-on-demand lead time (order to dispatch).
2. Q2 — Confirm UK delivery times: Tracked 48 2–3 working days, Tracked 24 1–2 (as checkout states).
3. Q3 — Untick "Preselect the sign-up option" in Settings → Checkout → Marketing options (George's action).
4. Q4 — Mida: embed off, keep, or uninstall. It has no sampling or page exclusion.
5. Q5 — Any Shopify Forms popups besides the homepage/password signup (form 923202)?
6. Q6 — Approve the pre-order cancellation policy (draft in `artifacts/proposed-copy.md` §B).
7. Q7 — Approve the shipping and delivery wording (`artifacts/proposed-copy.md` §A).
8. Q8 — Lift the hold and publish "Claude P1 fixes", or keep holding.
9. Q9 — OK to run one tee-only test cart (confirmed in chat before running).

Already asked elsewhere, not repeated here: George's yes on turning off tee inventory tracking (`cowork/product-data`, item D2).

## Waiting on external systems

- CrUX 28-day window: any homepage INP fix takes about 28 days to show in field data.
- Google recrawl after any schema change (transit time, tee handling time, set `size` key).

## Next actions

1. Tag all 17 tees (3 live, 14 draft) `made-to-order` and untrack POD inventory, before the T-shirt week drafts publish. Owner: `cowork/product-data` (extends its D2). George's yes on D2 is already requested there.
2. Turn off checkout marketing preselect (George, Shopify settings).
3. Align UK delivery time to Tracked 48 = 2–3 working days and Tracked 24 = 1–2, across policies, FAQ, Terms, the PDP custody block and schema `transitTime` (theme editor, Shopify policies, theme code).
4. Mida embed off if George agrees (Q4). If there are no Forms popups (Q5), test the Shopify Forms app embed off on a copy theme. Re-measure homepage INP 28 days later.
5. Publish the staged popup fix when the hold lifts; compare `ctc_*` events and signups against this baseline (09-performance).
6. Add the pre-order cancellation policy once approved (Q6; draft ready in `artifacts/proposed-copy.md` §B).
7. Theme code: no low-stock line on `continue` variants; tee `handlingTime` from the POD lead time; set products print `size` once; set-panel shipping line reworded.
8. Performance headroom: critical CSS, `font-display: swap`, hero `fetchpriority` (theme/performance).

## Expected impact

**Commercial:** High  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** High

- **Commercial:** every live POD tee promises stock and next-day dispatch it can't meet, and 14 more tees are about to launch the same way. Checkout consent is non-compliant. Pre-order shoppers are asked to agree to a missing policy.
- **SEO:** the homepage fails mobile INP and shows a full-screen mobile interstitial.
- **GEO:** merchant-listing and FAQ delivery facts are wrong for most orders, and answer engines quote shipping and delivery facts verbatim.
- **Confidence:** findings come from direct measurement and API reads. The impact sizes are judgement.
