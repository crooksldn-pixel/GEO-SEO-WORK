# Workstream: Collections, navigation, redirects and blog articles

**Branch:** cowork/collections  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 17:20 BST  
**Priority:** P1  
**Overall status:** READY TO IMPLEMENT

## Objective

Give each search intent one URL, and link the pages so visitors move between them:

- heavyweight / 550gsm hoodies and joggers → `/collections/sweats`
- tracksuits → `/collections/tracksuits`
- baggy jeans → `/collections/denim` and `/products/og-jeans`
- reactive jackets → `/collections/outerwear`
- fit and sizing → `/blogs/news/convict-vs-cellblock-fit`

This is the only session allowed to change Shopify collections, menus, URL redirects and blog articles. It does not touch products, the theme, Merchant Center or outreach.

## Current state

This workstream has changed nothing in Shopify yet.

- Live baselines for every target were captured on 16 Oct and re-checked on 18 Oct; nothing had changed.
- Exact copy for B (Denim links), B2 (Denim "made in Portugal" removal), C (Tracksuits fit link) and D (fit-article gsm section) is drafted and waiting on George's yes in chat.
- A (Sweats copy) and E (reactive guide) can't start, because their source files aren't reachable from this session.
- F is audited from the live site and the redirect list is ready, but it waits for Search Console evidence.
- G is answered: leave `/collections/sets` alone, because it's already noindexed.

This repo is public, so these files leave out anything about manufacturing origin and name no internal-only collections.

## Completed

- Audited: live H1, SEO title, meta and description for Sweats, Denim, Tracksuits, Sets and Outerwear (`artifacts/baselines-2026-10-18.md`).
- Audited: the fit article (published 16 Oct 13:10Z, unedited since).
- Audited: every F candidate's live status, `sitemap_collections_1.xml`, the 9 existing URL redirects and the archived products (`artifacts/index-hygiene-audit.md`).
- Prepared: exact before/after HTML for B, B2, C and D (`artifacts/proposed-changes.md`).
- Researched: G. The recommendation is no redirect (FINDINGS, Finding 2).
- Live: nothing.

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — Write approvals

**Blocking:** B, B2, C, D  
**Needs:** answers to QUESTIONS.md Q1 to Q4, then George's typed "go" in the Cowork chat. The C-003 pre-approval written in the brief isn't accepted on its own: the session's permission check blocked the Denim save on 16 Oct at 20:40.  
**From:** George  
**Severity:** P1  
**Can work around it?:** No  
**Workaround:** —

### Blocker 2 — Project files not reachable

**Blocking:** A (Sweats copy), E (reactive guide), writing `cowork-results/02-collections.md`  
**Needs:** the Sweats section of `01-collections-internal-linking.md` and sections 3 and 4 of `05-reactive-drafts.md`, copied into `inputs/` (QUESTIONS.md, Q10 and Q11). The other project files are useful context but not required.  
**From:** George  
**Severity:** P1  
**Can work around it?:** No  
**Workaround:** — (The Sweats copy is pre-approved text, and rewriting it here would bypass that approval.) The same path problem affects other sessions too: see `cowork/programme-records` FINDINGS. That branch also has C-003 down as not live, which matches this record.

### Blocker 3 — Search Console evidence

**Blocking:** F  
**Needs:** `cowork-results/05-search-console.md`, or the per-URL figures in QUESTIONS.md Q12  
**From:** another workstream (search console)  
**Severity:** P2  
**Can work around it?:** Partly  
**Workaround:** The redirect and noindex list is already prepared from live checks, so only the go/no-go decision waits on the data.

## Waiting on George

Every open question is in **`QUESTIONS.md`** (Q1 to Q12), with an answer line under each one. Source text goes in `inputs/`. When the answers are committed to this branch, George tells the collections chat "answered".

1. Approvals for the live edits: Q1 to Q6 and Q9. A typed "go" from George in the collections chat is still needed before any save.
2. Facts: Q7 (which wash CB1 and CB2 were)
3. Decisions: Q8 (leave Sets alone) and Q9 (optional Cellblock Set in Sweats)
4. Source files: Q10 (Sweats copy), Q11 (reactive drafts) and Q12 (Search Console data)

## Waiting on external systems

- Search console workstream output (`05-search-console.md`)
- Google recrawl of each page once changes go live

## Next actions

1. Apply whichever of B, B2, C and D are approved in QUESTIONS.md, once George types "go" in chat. Verify each one on the live page and log it in CHANGES.md.
2. Apply A once the 01 file arrives: confirmed weights plus the fit link, which also removes "made in Portugal" from Sweats.
3. After Search Console: redirect the 5 archived 404s (4 tees → `/collections/tees`, the duffle → `/collections/accessories`) and set `seo.hidden` on `/collections/frontpage`.
4. Fix whichever CB1/CB2 redirect pair Q7 shows is wrong.
5. Publish E once approved.

## Expected impact

**Commercial:** Medium  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** Medium

Single-intent collection pages, and a fit article that answers "is 550gsm heavy", target the store's highest-intent queries. Removing the Portugal claims takes a false fact off two indexed pages before AI answers repeat it. A small catalogue and low current traffic limit how big the near-term effect can be.
