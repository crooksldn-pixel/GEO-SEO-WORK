# Workstream: Merchant Center

**Branch:** cowork/merchant-center  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 20:45 BST  
**Priority:** P0 (store password lock has emptied Shopping) / P1 otherwise  
**Overall status:** BLOCKED

## Objective

Get the CROOKSLDN Google Merchant Center account (5860086407) clean enough for George to decide by 1 Nov whether to stay opted in to Google's automatic product additions (due 2 Nov). The feed comes from Shopify's Google & YouTube channel. This session is the only one allowed to change Merchant Center, and it changes nothing in Shopify.

## Current state

George's answers are in [ANSWERS.md](ANSWERS.md). One of the three approved Merchant Center writes is live: business name "Crooks LDN". The other two were refused by this session's own permission check, because the approval sits in a repo file. Each needs George's yes typed in this Cowork chat:
- archive the 10 `CROOKSRELEASESEPT` duplicates
- add the GB tee handling-time file

**The store is password-locked**, since about 17:05–20:00 BST on 18 Oct. Shopify's sync at about 20:05 BST arrived with no product links. By 20:24, 17.4K of 17.5K offers were "Not showing on Google" (FINDINGS 8). Nothing in Merchant Center can fix this. It clears after the store reopens and Shopify re-syncs.

Product-data's writes have landed in the feed: gender, age group, Puffa colour, titles, weights. The tees changed to 30 variants each at £20, and three caps are live with images (FINDINGS 9).

## Completed

- **Exported:** products 16 Oct and 18 Oct 20:22; issues 18 Oct 16:35 and 20:13. See [artifacts/baseline-2026-10-16.md](artifacts/baseline-2026-10-16.md).
- **Audited:** data sources, attribute-rule availability, UK shipping policies, item-level shipping and account issues (FINDINGS 1–7).
- **Compared:** against workstream 3's 11 findings. See [artifacts/findings-map-03.md](artifacts/findings-map-03.md). F3, F5, F6 and F7 are done; F2 needs no action; F8 waits on task D.
- **LIVE (18 Oct 20:12 BST):** Merchant Center business name "CROOKSLDN" → "Crooks LDN". Read back. See CHANGES.md.
- **Prepared:** [artifacts/gmc-supplemental-tee-handling-GB.tsv](artifacts/gmc-supplemental-tee-handling-GB.tsv) for 90 GB tee variants:
  - handling 2–3 working days
  - Tracked 48: £3.00, transit 2–3 days
  - Tracked 24: £4.99, transit 1–2 days
  - `shipping_label` = `print-on-demand`
  
  A copy is in George's Downloads folder for the upload.
- **Diagnosed:** the password lock is what emptied the feed (FINDINGS 8).
- **Scheduled:** 29 Oct 09:00 GMT re-check reminder in this chat.

## Currently working on

Nothing currently running. Waiting on George.

## Blockers

### Blocker 1 — Store password lock

**Blocking:** every Shopping and free listing; the meaning of the 29 Oct check  
**Needs:** the lock taken off when George is ready (Shopify > Online Store > Preferences)  
**From:** George  
**Severity:** P0  
**Can work around it?:** No  
**Workaround:** —

### Blocker 2 — Two approved writes need George's yes in this chat

**Blocking:** archiving the 10 duplicates (Q1); tee handling time (Q3, task D)  
**Needs:** George types, in this Cowork chat: "yes, archive the 10 CROOKSRELEASESEPT products and add the GB tee handling-time supplemental source"  
**From:** George  
**Severity:** P1  
**Can work around it?:** No  
**Workaround:** —

## Waiting on George

1. Is the password lock deliberate, and when does it come off?
2. A typed yes in this chat for the two Merchant Center writes in Blocker 2.

## Waiting on external systems

- Shopify re-sync with links after the store reopens.
- Google re-review of the business name, usually within a few days.

## Next actions

1. On George's typed yes: archive the 10 duplicates. Read back that "Data source: Merchant Center" shows 0 active.
2. On the same yes: add the supplemental source, link it to the GB Shopify source only, then verify on 2–3 tee items that handling shows 2–3 days and the label is set.
3. Within 24 hours of the store reopening: re-export and confirm `link` on all GB offers and disapprovals back to baseline.
4. 29 Oct: the opt-in call, by George's rule (Q4).
5. When the 14 T-shirt Week tees join the feed, add their GB variant IDs to the handling-time file.

## Expected impact

**Commercial:** Very high while the lock is on. Every listing is down.  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** High on the diagnosis; medium on how fast listings recover after reopening.
