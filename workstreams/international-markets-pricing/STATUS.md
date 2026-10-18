# Workstream: International markets & local pricing

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md). Re-read live values before any write: some approved changes were applied on 18 Oct by the project thread (change-log C-009 onward).
>
> **18 Oct 2026, 18:56 BST — George answered this branch's open questions** (recorded in [QUESTIONS.md](QUESTIONS.md)): go on USD prices; YES to US duty at checkout; Eurozone split YES; shipping bands YES "for now"; Channel Islands ship Royal Mail YES; tee blanks are Gildan.

**Branch:** cowork/international-markets-pricing  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 19:35 BST  
**Priority:** P2  
**Overall status:** LIVE EXCEPT THE FIXED PRICES — USD and EUR catalogs are built and in draft; loading the prices is refused by this session's permission check even after George's "go"

## Objective

International customers see deliberate local prices and clean shipping in a currency they recognise, from first page to checkout, without giving away margin.

## Live now (all read back — [CHANGES.md](CHANGES.md))

1. **Markets:** UK, Channel Island, United States (USD), Eurozone (EUR: 21 euro states + MC, AD, SM, VA, ME, XK), European Union (non-euro: CZ, DK, HU, PL, RO, SE), Canada, Australia and New Zealand, all world (rest of world). No overlaps. Product prices unchanged everywhere (still automatic conversion).
2. **Shipping on real costs:** US $25 under $100 / $30 from $100 (fixed USD); Eurozone €15 under €90 / €18 from €90 (fixed EUR); AU/NZ £20.99 / £26.99 at £75; rest of world £22.99 / £30.99 at £75; rest of Europe £12.99; Channel Islands Tracked 48 free from £30. Tested with Shopify's order calculator: every band fires as intended ([tests](artifacts/tests/2026-10-18-tier1.md)).
3. **Customs data:** HS codes on every non-tee product (17 added, HydroCuff corrected to 6201.40); origin CN on all non-tee products.
4. **Catalogs in draft:** "United States — USD fixed prices" and "Eurozone — EUR fixed prices", each with an all-products publication and a 0% price list. No effect until prices load and they're set Active.

## Blocked / waiting

### Blocker 1 — Fixed prices (USD and EUR)

The write that loads the prices was refused twice by this session's permission check (before and after George's "go"). Not worked around. George picks:

- **Import:** Markets → Catalogs → Import → Adjust prices → Import CSV with [catalog-prices-USD.csv](artifacts/catalog-prices-USD.csv) and [catalog-prices-EUR.csv](artifacts/catalog-prices-EUR.csv); set the 8 sock packs by hand ($9/$22/$35/$65, €8/€20/€30/€55); set both catalogs Active. Or
- **Explicit instruction** in the chat naming the action (e.g. "load the USD and EUR fixed prices into the US and Eurozone catalogs and activate them"); I retry once and stop if refused again.

### Blocker 2 — US duty collection needs George in admin

Shopify only switches it on in Settings → Taxes and duties → Duties and import taxes → Set up, ending in **Agree and activate** (terms acceptance — George's click). Choose: United States only, add duties at checkout, postal duty rates (US parcels go Royal Mail). HS codes are in except the 21 tees.

### Blocker 3 — Tee origin (Gildan)

Gildan sews in Honduras, Nicaragua and Bangladesh; the neck or care label says which. George reads one label per blank style → I write HS 6109.10 + that origin on all 21 tees in one pass.

### Blocker 4 — Channel Islands routing (CLIVE Shipping)

CLIVE Shipping holds "international orders only" and pulled Guernsey order CROOKS-2202 in, where Parcel2Go only offers Parcelforce (£16.71). The service code isn't in GitHub (the CLIVE repo only has its client), so the fix is George's: treat GG, JE and IM as domestic so they go Royal Mail Tracked 48 with UK orders.

### Blocker 5 — Country selector (theme workstream)

Without it, visitors only meet local prices at checkout.

## Next actions

See [NEXT.md](NEXT.md).

## Expected impact

**Commercial:** Medium (US/EU checkout completion; overseas shipping now covers real cost on every quoted lane except light FR/IT parcels at £0.25–£1; US duty recovered at checkout once switched on)  
**SEO:** Low  
**GEO:** Low–Medium  
**Confidence:** Medium — no improvement claimed until the 30/60-day re-pull.
