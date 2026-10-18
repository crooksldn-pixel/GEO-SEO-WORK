# Workstream: Live site checks — CWV baseline, rendered schema, shipping-promise parity, tee stock messaging, mobile popup

**Branch:** cowork/live-site-checks  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 16:42 BST  
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

Nothing currently running.

## Blockers

### Blocker 1 — Tee print-on-demand lead time unknown

**Blocking:** the final shipping wording for tees, the tee "made-to-order" line on the PDP, and the tee schema `handlingTime`  
**Needs:** the real order-to-dispatch time for print-on-demand tees  
**From:** George  
**Severity:** P1  
**Can work around it?:** Yes, partly  
**Workaround:** tag the tees `made-to-order` and stop tracking their inventory now. That alone removes "IN STOCK", "leaves tomorrow" and "1 LEFT". The made-to-order line can say "Printed to order" with no number until the lead time is confirmed. Don't use the theme default "9–16 days".

## Waiting on George

1. Tell us the tee print-on-demand lead time (order to dispatch).
2. Turn off the pre-ticked email box: Shopify admin → Settings → Checkout → Marketing options → stop preselecting the sign-up.
3. Decide on Mida recording: sample sessions or exclude the homepage. It's the heaviest script on every page.
4. Say whether Shopify Forms is used anywhere. If Omnisend owns signup, its app embed can go (262 KiB per page).
5. Approve a short pre-order cancellation policy. Checkout currently asks shoppers to agree to one that doesn't exist.
6. Decide when the hold on the "Claude P1 fixes" theme lifts. It holds the popup fix and the Organization schema update, and its timing decides whether theme fixes go on live directly or into both themes.

## Waiting on external systems

- CrUX 28-day window: any homepage INP fix takes about 28 days to show in field data.
- Google recrawl after any schema change (transit time, tee handling time, set `size` key).

## Next actions

1. Tag all 17 tees (3 live, 14 draft) `made-to-order` and untrack POD inventory, before the T-shirt week drafts publish. Owner: `cowork/product-data` (extends its D2). George's yes on D2 is already requested there.
2. Turn off checkout marketing preselect (George, Shopify settings).
3. Align UK delivery time to Tracked 48 = 2–3 working days and Tracked 24 = 1–2, across policies, FAQ, Terms, the PDP custody block and schema `transitTime` (theme editor, Shopify policies, theme code).
4. Cut Mida's load (sample or exclude the homepage) and scope the Shopify Forms embed; re-measure homepage INP in 28 days (apps).
5. Publish the staged popup fix when the hold lifts; compare `ctc_*` events and signups against this baseline (09-performance).
6. Add a pre-order cancellation policy (Shopify settings).
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
