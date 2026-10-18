# Workstream: Search Console analysis

**Branch:** cowork/search-console  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 17:05 BST  
**Priority:** P1  
**Overall status:** WAITING ON EXTERNAL

## Objective

Use Google Search Console to find commercial queries where an existing crooksldn.com URL can rank better, preferring URLs with momentum over new pages. Record a baseline, index hygiene, Core Web Vitals, sitemap status and Product structured-data currency.

This is research only. It changes nothing on the store, the theme, Merchant Center or Search Console.

## Current state

The research is done and recorded. Two things limit it:

1. Search Console has no data for 23 Jul – 14 Oct 2026. Jan–Jul is pre-relaunch reference data, and the post-deploy anchor is 15–16 Oct 2026.
2. Indexing > Pages is still processing (property re-added 16 Oct), so its "why pages aren't indexed" list can't be read yet. In-scope URLs were checked one by one with URL Inspection instead.

The ranked actions are recommendations for other workstreams. None are implemented. This workstream next measures what they change once data builds up.

Overlaps (FINDINGS 12): collections was blocked waiting for this report, which is now on this branch at `artifacts/search-console-report.md`; FINDINGS 5–8 are its task F evidence. The structured-data items (FINDINGS 3 and 9) touch the same Organization snippet that live-site-checks' held theme changes, so they should ship through that theme route.

## Completed

- **Measured:** UK Performance (queries, pages, daily) for 21 Jan – 22 Jul 2026 and 15–16 Oct 2026; first-half vs second-half comparison; query → page breakdowns for every product cluster. `artifacts/gsc-exports/`
- **Measured:** branded vs non-branded baseline. Jan–Jul UK: 14,312 clicks, 35,948 impressions; branded 12,303 clicks; genuinely non-branded 1 click and 187 impressions. Anchor 15–16 Oct UK: 86 clicks, 295 impressions, CTR 29.2%, position 4.6.
- **Researched:** ranked opportunity list, 14 rows with suggested owner workstreams. `artifacts/opportunities.csv`
- **Audited:** URL Inspection (indexed view) on 14 URLs; live status and redirects of every in-scope URL; Sitemaps, Core Web Vitals, HTTPS, Shopping and Crawl stats reports.
- **Tested:** live URL test on /products/convict-hoodie-1. Rendered Product JSON-LD shows priceCurrency GBP, and the 5 merchant items are valid.
- **Written:** full report `artifacts/search-console-report.md` and `FINDINGS.md` (12 findings, including overlaps with collections, live-site-checks, product-data and geo-measurement).

## Currently working on

Nothing currently running.

## Blockers

### Blocker 1 — Indexing > Pages report still processing

**Blocking:** The site-wide list of reasons pages aren't indexed (task 6)  
**Needs:** Google to finish processing the newly added property  
**From:** Google  
**Severity:** P3  
**Can work around it?:** Yes  
**Workaround:** URL Inspection on each in-scope URL (done; see FINDINGS 6–8).

## Waiting on George

1. Is the Crooks Express tee the design people call the "Tesco tee"? This decides where the two 404 Tesco tee URLs redirect (FINDINGS 5).

## Waiting on external systems

- Search Console data accumulation: 7-day post-deploy window ready around 24 Oct, 28-day around 14 Nov.
- Indexing > Pages processing.
- Google recrawl: /collections/outerwear ("Discovered – currently not indexed"), /collections/tees-1 (indexed, now a 301), /products/convict-hoodie-1 (indexed copy from 7 Oct shows missing variant images; live page passes).
- Fresh CrUX data for Core Web Vitals (last update 23 Jul).

## Next actions

1. Read Indexing > Pages once it finishes processing (check from 20 Oct) and add the reasons to FINDINGS.
2. Orchestrator routing: FINDINGS 5–8 (redirects, frontpage `seo.hidden`, fit-article links, joggers/denim/tees anchor links) → collections; FINDINGS 3 and 9 (homepage brand line, `shippingDetails`, currency) → the theme route in live-site-checks' NEXT.md. The Tesco tee redirect waits on George's answer.
3. Around 24 Oct: first 7-day post-deploy read (16–22 Oct) against the 15 Oct anchor. Track "crooks" position, which URL wins each product cluster, sitelinks, and indexing of /collections/outerwear and the fit article.
4. Around 14 Nov: 28-day read.

## Expected impact

**Commercial:** High  
**SEO:** High  
**GEO:** Low  
**Confidence:** Medium

Search drives almost all brand traffic. "crooks" alone carries a third of impressions and lost 1,076 clicks in a quarter, and the brand+product clusters (joggers, jeans, jorts, tees) all land on the homepage instead of a collection. Fixing both uses existing URLs. Confidence is medium because the reference data predates the relaunch.
