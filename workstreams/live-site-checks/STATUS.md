# Workstream: Live site checks — CWV baseline, rendered schema, shipping-promise parity, tee stock messaging, mobile popup

**Branch:** cowork/live-site-checks  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 20:40 BST  
**Priority:** P1  
**Overall status:** READY TO IMPLEMENT

## Objective

Started as a research-only baseline of the live site: Core Web Vitals, rendered structured data, shipping-promise parity, tee stock and dispatch messaging, and the mobile popup.

Since George's 18 Oct answers ([ANSWERS.md](ANSWERS.md), owner decisions #1, #3, #4), this workstream also owns four **Shopify policy** edits: shipping, refund, contact, and a new cancellation policy. Theme files belong to `cowork/theme-editor`. Products belong to `cowork/product-data`.

## Current state

**George answered on 18 Oct at 17:03 UTC** ([ANSWERS.md](ANSWERS.md)):
- tees dispatch in 2–3 working days
- UK delivery aims are confirmed and must be worded as "not guaranteed"
- the cancellation policy and shipping wording are approved
- the held P1 theme stays held, with fixes going onto the live theme instead
- Mida stays on
- Forms popups and the tee test cart are parked or dropped

Since then the store has moved:
- **A new live theme**, "CROOKSLDN — live 18 Oct + evening fixes", went live at ~18:58 UTC. It fixes most of the tee problem, rebuilds the popup and ships the Organization schema (FINDINGS 12).
- **The storefront is behind its password page** as of ~20:10 BST (FINDINGS 11). Whether that's intended is unknown.

The four policy edits are **built and checked against the live text**. Each "before" matched exactly once. They are **not applied**. They wait for George to type **go** in this workstream's chat: a go recorded in a file by another session isn't treated as authorisation for live writes.

## Completed

- **Measured, 16 Oct:** PageSpeed mobile and desktop on 5 URLs; homepage popup at 390 px.
- **Tested, 16 Oct:** Rich Results Test and validator.schema.org on 5 URLs.
- **Audited, 16 Oct:** 14 shipping-promise places; tee PDP stock lines; checkout to the shipping step.
- **Re-verified, 18 Oct 16:35 BST:** theme, tees, rates, policies, checkout box.
- **Compared, 18 Oct:** the held P1 theme vs live, and the new live theme vs Friday's (FINDINGS 12).
- **Prepared, 18 Oct:**
  - final approved copy with the live status of each place ([artifacts/proposed-copy.md](artifacts/proposed-copy.md))
  - exact policy edits with before and after bodies and rollback ([artifacts/policy-edits-ready.md](artifacts/policy-edits-ready.md), `artifacts/policy-bodies/`)
- **Observed, 18 Oct ~20:10 BST:** storefront password page (FINDINGS 11).
- **Not done:** no policy, theme or product change has been made by this workstream.

## Currently working on

Nothing currently running. Waiting for George's typed **go** on the four policy edits.

## Blockers

### Blocker 1 — Live policy writes need George's go in this chat

**Blocking:** the shipping, refund, contact and cancellation policy edits  
**Needs:** George types **go** in this workstream's Cowork chat. `ANSWERS.md` says "answered" counts as his go. Under the Cowork rules this session acts only on approval given in its own chat, not on one relayed through a file.  
**From:** George  
**Severity:** P1  
**Can work around it?:** No  
**Workaround:** none. Everything is prepared, so applying them takes minutes.

## Waiting on George

1. Type **go** for the four policy edits in `artifacts/policy-edits-ready.md`, or name the ones to hold.
2. Is the storefront password page intended, and when does it come off? (FINDINGS 11)
3. Untick "Preselect the sign-up option" (Settings → Checkout → Marketing options). Your own action, still outstanding per `ANSWERS.md`.

## Waiting on external systems

- The storefront reopening (password off). PageSpeed, the Rich Results Test, Merchant Center and Google all see the password page until then.
- CrUX: 28 days after any homepage INP change.
- Google recrawl after the policy and schema changes.

## Next actions

1. Apply the four policy edits one at a time on George's go, reading each back.
2. theme-editor: FAQ (A6), Terms (A7) and set-panel line (A4). Copy is in `artifacts/proposed-copy.md`.
3. Theme code: no "IN STOCK" on `tee` products; schema `transitTime` 2–3 and tee `handlingTime` 2–3.
4. product-data: tracking off on the 4 tees published at 17:27 UTC, and on the 14 T-shirt Week tees before they publish.
5. When the password page comes off: re-run PageSpeed on home, the Rich Results Test on hoodie, tee and outerwear, and the popup at 390 px. Record them against the 16 Oct baseline.

## Expected impact

**Commercial:** High  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** High

- **Commercial:** the written policies still promise 1–2 day delivery and same-day dispatch with no tee exception, and pre-order shoppers are asked to agree to a policy that doesn't exist.
- **SEO and GEO:** policies, FAQ and schema are what Google and AI answers quote for delivery times.
- **Confidence:** every number comes from Shopify settings or George's 18 Oct answers.
