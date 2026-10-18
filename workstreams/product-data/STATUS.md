# Workstream: Product data

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md) and override the open questions and George-blockers below. Anything not answered there is parked and blocks nothing. Project files are on `cowork/project-files-import`. Re-read live values before any write: some approved changes were applied on 18 Oct (change-log C-009 onward).

**Branch:** cowork/product-data  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 17:35 BST  
**Priority:** P1  
**Overall status:** READY TO IMPLEMENT

## Objective

Make the Shopify product data for every CROOKSLDN product match George's confirmed facts of 16 Oct 2026. That covers copy, SEO and Shopping titles, alt text, fabric attributes, tags, variant weights, inventory settings, channel publishing and the store description. The aim is that Google Shopping, product pages, product schema and AI answers describe the range correctly and make no false stock or composition claims.

This session is the only one allowed to change products, variants, inventory items, product media, product channel publishing and Settings > Store details. Collections, theme, Merchant Center and outreach belong to other workstreams.

## Current state

The audit is finished and was re-checked live on 18 Oct. This session hasn't written anything to Shopify.

Every question for George is in **[QUESTIONS.md](QUESTIONS.md)**, with an answer line under each. When George says "answered" in the product-data chat, this session will:
1. read the file;
2. take each YES as approval for exactly that change;
3. make the writes, reading each product live first and back afterwards.

Several other workstreams have reported, and that changed this plan:
- **`cowork/live-site-checks`:** the tee fix now also covers the `made-to-order` tag and the 14 draft T-shirt week tees.
- **`cowork/merchant-center`:** all 25 products are already approved for the UK apart from the Cream Cap. So gender, age group and colour are completeness work, not a disapproval fix, and they moved down the order. Its two title proposals were added as Q6.

## Completed

- **Audited** (16 Oct 20:31 BST, re-checked 18 Oct 16:30 BST): title, description, SEO title and description, every image alt, `crooks.fabric` and `shopify.fabric` on all 25 active products, against the confirmed facts. 6 products carry cotton claims outside hoodies and joggers, and OG Jeans lacks 14oz. See FINDINGS 1–2.
- **Audited:**
  - size charts: the three jeans charts are copies of the sweats chart (FINDINGS 3);
  - channel publishing, variant weights, tee tracking and stock, and selling plans;
  - gender, age group and colour coverage, and the store description (FINDINGS 4–9).
- **Audited** (18 Oct): all 17 tees, 3 live and 14 draft. None is tagged `made-to-order`, and all track inventory. The tag `cotton` isn't used by any collection rule.
- **Cross-checked** against `cowork/merchant-center`, `cowork/live-site-checks`, `cowork/geo-measurement`, `cowork/search-console`, `cowork/collections` and `cowork/programme-records` (18 Oct). Overlaps are recorded in FINDINGS 4, 6, 7, 8 and 11.
- **Prepared:**
  - exact before/after for every proposed write ([artifacts/c-fabric-claim-fixes.md](artifacts/c-fabric-claim-fixes.md), [artifacts/01-product-data.md](artifacts/01-product-data.md));
  - George's answer sheet ([QUESTIONS.md](QUESTIONS.md)).
- **Live:** nothing yet.

## Currently working on

Nothing currently running. Waiting for "answered".

## Blockers

### Blocker 1 — Every Shopify write needs George's yes

**Blocking:** every write  
**Needs:** YES or NO on QUESTIONS Q1–Q9, then "answered" in the product-data chat  
**From:** George  
**Severity:** P1  
**Can work around it?:** No  
**Workaround:** None. The connector refuses writes whose approval exists only in the brief.

### Blocker 2 — SEO project files and photos not in reach

**Blocking:** G (HydroCuff and Puffa descriptions), J (photos)  
**Needs:** the files listed in QUESTIONS Q16 and the photos in Q17  
**From:** George  
**Severity:** P2  
**Can work around it?:** Partly  
**Workaround:** the brief's results file is kept on this branch at `artifacts/01-product-data.md`, where `cowork/programme-records` can read it. GitHub issue #1 tracks the Project-files import for all workstreams.

## Waiting on George

Everything is in [QUESTIONS.md](QUESTIONS.md):
- **Q1–Q9:** yes/no approvals.
- **Q10–Q14:** gender per product, Puffa colour, weights, the 17 Oct weight changes, jeans measurements.
- **Q15–Q18:** reactive-copy wording calls, Project files, product photos, bag-label photos.

## Waiting on external systems

- Merchant Center reprocesses after the Shopify writes, typically 1–3 days. `cowork/merchant-center` re-exports on 29 Oct for the auto-add call.

## Next actions

Once answered, in this order:

1. **A:** Cream Cap off Google & YouTube. Clears the only UK disapproval.
2. **Tees:** untrack all 450 tee variants and tag all 17 tees `made-to-order` (Q5). Removes the false "IN STOCK", "leaves tomorrow" and "1 LEFT" claims before the T-shirt week drafts publish.
3. **C1–C8 and the `cotton` tag:** removes unconfirmed composition from copy, attributes and the three tee Shopping titles.
4. **Q6:** Crewneck and Puffa SEO and Shopping titles.
5. **H:** shipping weights. Sets and two tees first, the rest as George gives them.
6. **D1, E, F:** age group, gender per product, Puffa colour.
7. **I:** remove the ReStock plan in the app.
8. **B:** store description, via the browser.
9. The jeans size charts, once the measurements arrive.
10. G, J and K, once the files and photos arrive.

## Expected impact

**Commercial:** Medium  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** Medium

- **Commercial:** the biggest concrete wins are stopping false dispatch and stock claims on tees across 17 products, fixing copied size charts, and putting real weights on the sets.
- **SEO and GEO:** the copy is mostly sound. The fixes take unconfirmed claims out of what Shopping, search snippets and AI answers quote, and fix two all-caps Shopping titles.
- **Gender, age group and colour:** these don't affect eligibility today, so their effect on Shopping-pack inclusion is uncertain. That's measured by the next geo-measurement run, not assumed.
