# Workstream: Merchant Center

**Branch:** cowork/merchant-center  
**Owner:** Cowork session  
**Last updated:** 29 Oct 2026, 09:15 GMT  
**Priority:** P2  
**Overall status:** WAITING ON EXTERNAL

## Objective

Get the CROOKSLDN Google Merchant Center account (5860086407) clean enough for George to decide by 1 Nov whether to stay opted in to Google's automatic product additions (due 2 Nov). The feed comes from Shopify's Google & YouTube channel. This session is the only one allowed to change Merchant Center, and it changes nothing in Shopify.

## Current state

**29 Oct opt-in call: stay opted in** (George's Q4 rule). The UK feed is clean:
- all 306 GB offers have links, gender, age group, colour and description
- the only UK disapproval is one sock pack's price
- the password lock that emptied Shopping on 18 Oct is gone
- "Invalid business name" has cleared since the change to "Crooks LDN"

See [artifacts/04-merchant-center.md](artifacts/04-merchant-center.md), section "Task E".

Still open:
- The 10 `CROOKSRELEASESEPT` duplicates and the tee handling-time supplemental both wait on George's yes typed in this chat. Both are approved in ANSWERS.md.
- The UK shipping sent by Shopify (free Tracked 48; Tracked 24 free from £50) no longer matches the shipping policy page (FINDINGS 10).
- Outside the UK, 76 variants per label are sent without links, so 4.4K offers are not approved. That's for international-markets-pricing.

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
- **Done, 29 Oct (task E):** re-exported, compared and made the call: stay opted in. See [artifacts/check-2026-10-29.md](artifacts/check-2026-10-29.md).

## Currently working on

Nothing currently running. Waiting on George.

## Blockers

### Blocker 1 — Two approved writes need George's yes in this chat

**Blocking:** archiving the 10 duplicates (Q1); tee handling time (Q3, task D)  
**Needs:** George types, in this Cowork chat: "yes, archive the 10 CROOKSRELEASESEPT products and add the GB tee handling-time supplemental source"  
**From:** George  
**Severity:** P2  
**Can work around it?:** No  
**Workaround:** —

## Waiting on George

1. A typed yes in this chat for the two Merchant Center writes (Blocker 1).
2. Is the free UK Tracked 48 / Tracked 24 free-from-£50 offer deliberate? If yes, update the shipping policy page; if no, restore the Shopify rates (FINDINGS 10).

## Waiting on external systems

- Google's auto-add on 2 Nov.

## Next actions

1. **3 Nov:** list what auto-add brought in, flag any duplicates of Shopify items, and confirm UK disapprovals are still about 0.
2. **On George's typed yes:** archive the 10 duplicates, and add the GB tee handling-time supplemental. Rebuild the file from a fresh export first. Re-check the variant IDs (tees are back to £25). Also copy the UK shipping prices Shopify is sending at the time: the file still carries £3 Tracked 48, and on 29 Oct the feed sends £0.00.
3. **When the 14 T-shirt Week tees appear in the GB feed:** add them to the supplemental file.

## Expected impact

**Commercial:** Medium. The UK listings are live again; the remaining gains are the international links and accurate tee handling.  
**SEO:** Low  
**GEO:** Medium  
**Confidence:** High
