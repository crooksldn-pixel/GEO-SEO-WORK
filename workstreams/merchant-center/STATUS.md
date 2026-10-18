# Workstream: Merchant Center

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md) and override the open questions and George-blockers below. Anything not answered there is parked and blocks nothing. Project files are on `cowork/project-files-import`. Re-read live values before any write: some approved changes were applied on 18 Oct (change-log C-009 onward).

**Branch:** cowork/merchant-center  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 17:20 BST  
**Priority:** P1  
**Overall status:** READY TO IMPLEMENT

## Objective

Get the CROOKSLDN Google Merchant Center account (5860086407) clean enough for George to decide by 1 Nov whether to stay opted in to Google's automatic product additions (due 2 Nov). The feed comes from Shopify's Google & YouTube channel. This session is the only one allowed to change Merchant Center. It changes nothing in Shopify, and nothing is saved without George's "yes".

## Current state

Audit done. Nothing has been changed in Merchant Center.

All 25 Shopify products are approved for the UK. In the UK, the only disapproved item is the Cream Cap: it has no image, and product-data item A (unpublish it from Google & YouTube) hasn't been done yet. Every other disapproval comes from either:
- 10 duplicate products someone added by hand in Merchant Center under feed label `CROOKSRELEASESEPT`, or
- markets CROOKSLDN barely sells to: Liechtenstein, Bulgaria, Croatia, Malta and South Korea.

The brief's invalid-GTIN fix (task B) can't be done the way it was written, and it doesn't look needed right now (FINDINGS 2).

## Completed

- **Exported:** Products > All products, 16 Oct (18,553 offers across 77 feed labels). Summarised in [artifacts/baseline-2026-10-16.md](artifacts/baseline-2026-10-16.md).
- **Exported:** Needs attention > all issues, 18 Oct (1,484 issue rows, 4 issue types). Summarised in the same file.
- **Audited:** data sources. There are 76 "Shopify App API" sources (Merchant API), one per feed label, plus one "Added in Merchant Center" source with 10 products.
- **Audited:** Attribute rules availability. Shopify's sources have no Attribute rules tab.
- **Audited:** account-level shipping for the UK (4 policies), the shipping countries Merchant Center says are missing, and account issues (business name; no Google Ads link).
- **Audited:** item-level shipping that Shopify sends on every GB offer.
- **Compared:** shipping against the shipping policy page, the tee product page and the `cowork/live-site-checks` checkout findings.
- **Prepared:** proposals that need George's yes. See [artifacts/04-merchant-center.md](artifacts/04-merchant-center.md).
- **Scheduled:** a reminder in this chat for the 29 Oct re-check (task E), 09:00 GMT.
- **Live:** nothing.

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — Every Merchant Center change needs George's yes

**Blocking:** removing the 10 `CROOKSRELEASESEPT` duplicates; the business-name fix  
**Needs:** George's answers to Q1 and Q2 in QUESTIONS.md  
**From:** George  
**Severity:** P1  
**Can work around it?:** No  
**Workaround:** —

### Blocker 2 — Tee handling time has no number yet

**Blocking:** task D (tee handling time and shipping_label)  
**Needs:** Q3 in QUESTIONS.md, the tee print-on-demand time in working days  
**From:** George  
**Severity:** P2  
**Can work around it?:** No  
**Workaround:** —

### Blocker 3 — The `seo` project folder isn't reachable

**Blocking:** comparing against the 11 findings in `workstreams/03-merchant-feed.md` and the handoff "corrections" (sections A–E); saving the export to `measurements/`  
**Needs:** Q5 in QUESTIONS.md: those two files committed to this repo, or the `seo` folder connected  
**From:** George  
**Severity:** P2  
**Can work around it?:** Partly  
**Workaround:** findings are taken straight from Merchant Center. The results file the brief asked for sits on this branch at `artifacts/04-merchant-center.md`.

## Waiting on George

All questions, with options and answer lines, are in [QUESTIONS.md](QUESTIONS.md). When George says "answered", this session reads that file and carries on.

1. Q1: delete the 10 `CROOKSRELEASESEPT` duplicates?
2. Q2: business name "Crooks LDN"?
3. Q3: tee print-on-demand time, in working days.
4. Q4: auto-add stance for 1 Nov.
5. Q5: the `03-merchant-feed` files.
6. Q6 and Q7 are optional.

## Waiting on external systems

- Merchant Center reprocessing after product-data's Shopify writes land (Cream Cap, gender, age group, colour). Usually 1–3 days.
- The 29 Oct export, for the opt-in call.

## Next actions

1. On George's yes, delete the 10 `CROOKSRELEASESEPT` products. They're live in the UK as unbranded all-caps duplicates of Shopify listings, and disapproved in 33 other countries. Deleting them clears every currency issue and 10 of the 254 missing-shipping issues.
2. On George's yes, change the business name, so Shopping shows the brand instead of "crooksldn.com".
3. When the tee time arrives, check whether a supplemental source can carry handling time and a shipping_label onto the Shopify API sources. Then show George the exact setup before saving.
4. 29 Oct: re-export, compare with the baseline, and give the stay-in or opt-out call.
5. Optional and low value: Liechtenstein, Bulgaria, Croatia, Malta and South Korea gaps (FINDINGS 5). Leave alone unless George sells there.

## Expected impact

**Commercial:** Medium  
**SEO:** Low  
**GEO:** Medium  
**Confidence:** Medium

The UK feed is already eligible, so the main commercial risk is the opt-in decision, not lost listings. Removing the duplicates and fixing the seller name protects how the brand shows in Shopping and in AI shopping answers, which take Merchant Center data. Confidence is medium because Shopify regenerates its sources and policies, and Merchant Center may undo edits made on top of them.
