# Workstream: Product data

**Branch:** cowork/product-data  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 20:30 BST  
**Priority:** P1  
**Overall status:** LIVE

## Objective

Make the Shopify product data for every live CROOKSLDN product match George's confirmed facts. That covers copy, SEO and Shopping titles, alt text, fabric attributes, tags, variant weights, inventory settings, category attributes (gender, age group, colour), channel publishing and the store description. The aim is that Google Shopping, product pages, product schema and AI answers describe the range correctly and make no false stock or composition claims.

This session is the only one allowed to change products, variants, inventory items, product media, product channel publishing and Settings > Store details.

## Current state

George answered on 18 Oct ([ANSWERS.md](ANSWERS.md); owner decisions 17:03 UTC, "go" 18:45 UTC, "answered" in this chat 20:07 BST). Every approved change that this session's tools can make is now live and read back ([CHANGES.md](CHANGES.md)).

The store changed a lot on 18 Oct before the writes. There are now 45 live products, not 25:
- 21 tees, including the 14 T-shirt Week tees and 4 reactivated older tees;
- 2 new caps.

The Cream Cap gained photos and copy. The 3 original tees were rewritten. The writes were adjusted to that live state; see CHANGES.md for what was skipped and why.

Two approved items need George's own hands, because the tools couldn't reach them:
- the store description (an embedded admin frame that won't take input);
- the old pre-order plan (needs a scope the connector lacks).

Three new questions came out of today's changes (QUESTIONS Part 4).

## Completed

- **Live 18 Oct:**
  - stock tracking off on all 630 tee variants. 540 by this session; 90 earlier by the project thread, C-009.
  - fabric cleanup C1–C9;
  - OG Jeans 14oz;
  - Crewneck and Puffa SEO and Shopping titles;
  - HydroCuff and Puffa descriptions;
  - age group "Adults" and gender "Unisex" on all 45 live products;
  - Puffa colour Black;
  - weights: Black and Grey Set 1,700g, Cellblock Set 1,450g, CRX Garms and CRXST★RZ 250g.
  
  All read back in Admin.
- **Audited** (16 Oct, 18 Oct): the full product-data audit in FINDINGS 1–15, cross-checked against the merchant-center, live-site-checks, geo-measurement, search-console, collections and programme-records branches.
- **Skipped on purpose:** Cream Cap off Google. It now has photos, so pulling it would undo a fix.

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — Store description can't be entered from this session

**Blocking:** owner decision #14 (store description)  
**Needs:** George pastes the approved text into Online Store → Preferences → Meta description and saves (QUESTIONS M1)  
**From:** George  
**Severity:** P2  
**Can work around it?:** No  
**Workaround:** None. The Admin API has no write for `shop.description`, and the admin frame didn't take browser input after 3 attempts.

### Blocker 2 — Old pre-order plan can't be removed by the connector

**Blocking:** owner decision #25 on 19 products  
**Needs:** George removes them from the plan in Notify Me! → PreOrder (QUESTIONS M2)  
**From:** George  
**Severity:** P3  
**Can work around it?:** No  
**Workaround:** None. The API needs a purchase-options scope this connector doesn't have.

## Waiting on George

1. M1: paste the store description (2 minutes).
2. M2: remove 19 products from the Notify Me! pre-order plan (5 minutes).
3. Q19: is the tee "200gsm" a confirmed fact, or should it come out of the 21 live tees?
4. Q20: 250g on the remaining 560 tee variants?
5. Q21: change the Puffa reacted-photo alt from "metallic silver" to "white"?

Parked by George (not asked again): Pink Set weight, other missing weights, jeans size charts, photos.

## Waiting on external systems

- Merchant Center reprocessing of today's titles, gender, age group, colour and material changes, typically 1–3 days. `cowork/merchant-center` re-exports on 29 Oct.
- Google recrawl of the HydroCuff, Puffa and OG Jeans pages. Note the store is currently password-protected (FINDINGS observation).

## Next actions

1. Once George answers Q19, either remove "200gsm" from the 21 tees and clear the 3 "220gsm cotton" fields, or make the fields match the confirmed fact.
2. Once he answers Q20 and Q21, set the tee weights and the Puffa alt.
3. After M1 and M2, read back `shop.description` and the `sellingPlanGroups` on the 19 products.
4. 2–3 days after today's writes, ask `cowork/merchant-center` for item issues on gender, age_group, colour, material and titles.

## Expected impact

**Commercial:** Medium  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** Medium

- **Commercial:** the clearest wins are 630 tee variants no longer counting down to false "[n] LEFT" or negative stock during the T-shirt Week launch, and real weights on the three heaviest sets.
- **SEO and GEO:** unconfirmed composition is out of copy and Google's material attribute; two all-caps or unbranded Shopping titles are fixed; the reactive jackets now describe their effect plainly. Any ranking or GEO gain is recorded only against the next measurement, not assumed.
