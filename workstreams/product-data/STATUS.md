# Workstream: Product data

**Branch:** cowork/product-data  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 16:55 BST  
**Priority:** P1  
**Overall status:** READY TO IMPLEMENT

## Objective

Make the Shopify product data for every active CROOKSLDN product match George's confirmed facts of 16 Oct 2026. That covers copy, SEO fields, alt text, fabric attributes, variant weights, inventory settings, channel publishing and the store description. The aim is that Google Shopping, product schema and AI answers describe the range correctly and the items are eligible to show.

This session is the only one allowed to change products, variants, inventory items, product media, product channel publishing and Settings > Store details. Collections, theme, Merchant Center and outreach belong to other workstreams.

## Current state

The audit is finished and was re-checked against live Admin on 18 Oct. Nothing audited has changed since 16 Oct, apart from two variant weights set from outside this session (Finding 6).

This session hasn't written anything to Shopify. The one pre-approved change, taking the Cream Cap off Google & YouTube, was refused by the connector's permission check. The approval sits in the brief, not in the chat, so it needs George's "yes" there.

Every other change is prepared with exact before/after values. Each one is waiting on a George approval or a fact only he has.

## Completed

- **Audited** (16 Oct 20:31 BST, re-checked 18 Oct 16:30 BST): title, description, SEO title and description, every image alt, `crooks.fabric` and `shopify.fabric` on all 25 active products, against the confirmed facts. 6 products carry cotton claims outside hoodies and joggers. OG Jeans lacks 14oz. Nothing else conflicts. See FINDINGS 1 and 2.
- **Audited**: size charts. The three jeans charts are copies of the Convict Sweats chart (Finding 3).
- **Audited**: channel publishing on the Cream Cap, variant weights on all 25 products, tee inventory tracking and stock, and selling-plan groups. Also gender, age group and colour attribute coverage, and the store description. See FINDINGS 4–9.
- **Prepared**: exact before/after for A, B, C1–C8, D2, F and the derived H weights, a suggested gender list for E, and the list of weights still missing. See [artifacts/01-product-data.md](artifacts/01-product-data.md) and [artifacts/c-fabric-claim-fixes.md](artifacts/c-fabric-claim-fixes.md).
- **Live**: nothing yet.

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — Shopify writes need George's yes in this chat

**Blocking:** every write, starting with A (Cream Cap off Google & YouTube)  
**Needs:** George replies "yes" to each item, or to a batch, in this Cowork chat  
**From:** George  
**Severity:** P1  
**Can work around it?:** No  
**Workaround:** None. The connector refuses writes whose approval exists only in a file.

### Blocker 2 — SEO project files not reachable

**Blocking:** G (HydroCuff and Puffa descriptions), J (photo inbox)  
**Needs:** the `seo` folder connected to this session, or `workstreams/05-reactive-drafts.md`, `assets/README.md` and the incoming photos attached here or committed to this repo  
**From:** George  
**Severity:** P2  
**Can work around it?:** Partly  
**Workaround:** the results file the brief asked for is kept on this branch at `artifacts/01-product-data.md`, where `cowork/programme-records` can read it

## Waiting on George

1. Say yes to A: Cream Cap off Google & YouTube only.
2. Say yes to B: the store description, using the exact sentence from the brief.
3. Say yes to C: remove "cotton" from the tees, socks and Cellblock Shorts, and add 14oz to OG Jeans (exact strings in artifacts).
4. Age group "adult" on all 25 products: yes, or name the one to leave out.
5. Say yes to turning off inventory tracking on the 30 tee variants.
6. Correct the gender list: which items are women's, which are men's, which are unisex.
7. Puffa base colour, one word.
8. Say yes to the derived weights: sets as the sum of their parts, CRX Garms and CRXST★RZ at 250g.
9. Weights for the Yard jorts, Puffa, cap and each White/Red sock pack.
10. Is Pink Convict Sweats 700g right, or should it be 800g like the Black and Grey?
11. ReStock preorder plan: remove from the tees only, or from the Pink Convict Sweats too?
12. Real size charts for both Yard Jeans and the OG Jeans.
13. Connect the `seo` folder, or attach the reactive drafts and photos.
14. Bag-label photos, one per product, denim first.

## Waiting on external systems

- None until writes land. After A, D, E and F go live, Merchant Center needs to reprocess the feed, typically 1–3 days.

## Next actions

1. A: unpublish the Cream Cap from Google & YouTube. Stops a live disapproval and needs one word from George.
2. D1, E and F: age group, gender and Puffa colour. These attributes are required for UK apparel in Shopping, so they matter most for feed eligibility.
3. C1–C8: fabric fixes and 14oz. Removes unconfirmed claims from feed attributes and snippets.
4. D2 and I: tee tracking and the ReStock plan. Fixes negative stock, PreOrder schema and the checkout notice.
5. H: shipping weights. Correct shipping rates and labels.
6. B: store description, via the browser.
7. The jeans size charts, once George sends measurements.
8. G, J and K once the files and photos arrive.

## Expected impact

**Commercial:** High  
**SEO:** Medium  
**GEO:** Medium  
**Confidence:** Medium

Commercial is high because gender, age group and colour gate apparel eligibility in UK Shopping. Google UK showed a Shopping pack on all seven core product and specialist queries measured on 16 Oct, with no Crooks product in any of them (Finding 11). Wrong weights and copied size charts also cost money directly, through shipping charges and wrong-size swaps.

SEO and GEO are medium because the copy is mostly sound already. The fixes take unconfirmed claims out of what search engines and AI answers quote, rather than adding new ranking content.

Confidence is medium because results depend on Merchant Center reprocessing, and several items depend on facts George hasn't supplied yet.
