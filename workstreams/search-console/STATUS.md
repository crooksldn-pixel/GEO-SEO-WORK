# Workstream: Search Console analysis

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md), copied onto each question in [QUESTIONS.md](QUESTIONS.md). Q1, Q3 and Q4 are answered; Q2 is parked.

**Branch:** cowork/search-console  
**Owner:** Cowork session  
**Last updated:** Sat 24 Oct 2026, 10:45 BST  
**Priority:** P1  
**Overall status:** WAITING ON EXTERNAL

## Objective

Use Google Search Console to find commercial queries where an existing crooksldn.com URL can rank better, preferring URLs with momentum over new pages. Record a baseline, index hygiene, Core Web Vitals, sitemap status and Product structured-data currency, then measure what the other workstreams' changes do.

This workstream changes nothing on the store, the theme, Merchant Center or Search Console.

## Current state

The 20 Oct and 24 Oct scheduled checks ran together on 24 Oct; the 20 Oct one arrived four days late.

- **Store lock resolved.** The store was password-locked from about 18:15 BST on 18 Oct to about 17:00 BST on 19 Oct (FINDINGS 13, timed from Crawl stats). It has been open since; checked 24 Oct 10:01 BST.
- **Index baseline in.** Indexing > Pages has processed: 43 pages indexed, 800 not indexed. 639 of the 800 are parameter copies of product pages, nothing important is blocked, and the stale entries will drop on recrawl (FINDINGS 14).
- **First week read (15–22 Oct), with no clean SEO read possible** (FINDINGS 15). Only 16–17 Oct are clean post-deploy days; 18–19 Oct are lock days and 19–25 Oct is T-shirt Week. Recorded signals: "550gsm hoodie" got the first non-branded click to /collections/sweats; "water reactive windbreaker" had 7 impressions on HydroCuff; "joggers" searches still click through to the homepage.
- **Not done yet by collections:** the Tesco tee redirects (both URLs still 404) and hiding /collections/frontpage (still indexed and a brand sitelink). Four of the five archived tees came back live with T-shirt Week, so they no longer need redirects (FINDINGS 8).
- **Google:** /collections/outerwear is still "Discovered – currently not indexed". The fit article is now in `sitemap_articles_1.xml` (sitemap read 23 Oct, 54 pages) but is still unknown to Google.

## Completed

- **Measured:** UK Performance for 21 Jan – 22 Jul 2026, 15–16 Oct and 15–22 Oct 2026, with day labels; first-half vs second-half comparison; query → page breakdowns. `artifacts/gsc-exports/`
- **Measured:** branded vs non-branded. Jan–Jul UK: 14,312 clicks; branded 12,303; genuinely non-branded 1 click and 187 impressions. 15–22 Oct UK: 650 clicks, 1,520 impressions; genuinely non-branded commercial 1 click and 17 impressions.
- **Audited:** Indexing > Pages baseline, reasons and the indexed list (report dated 16 Oct). URL Inspection on 13 URLs (16 and 18 Oct) and 4 URLs (24 Oct). Sitemaps, Core Web Vitals, HTTPS, Shopping and Crawl stats reports.
- **Measured:** password-lock window from Crawl stats (FINDINGS 13).
- **Tested:** live URL test on /products/convict-hoodie-1: priceCurrency GBP, 5 valid merchant items.
- **Researched:** ranked opportunity list, 14 rows with owners. `artifacts/opportunities.csv`
- **Written:** full report `artifacts/search-console-report.md` and `FINDINGS.md` (15 findings).
- **Scheduled and run:** 20 Oct and 24 Oct checks (run together on 24 Oct). 14 Nov is still scheduled.

## Currently working on

Nothing currently running. Next scheduled run: 14 Nov 2026, 10:00 GMT.

## Blockers

None. The store lock (18–19 Oct) and the Indexing report processing are both resolved.

## Waiting on George

1. Request indexing for /collections/outerwear and /blogs/news/convict-vs-cellblock-fit: yes or no? Asked in chat on 18 Oct and not answered yet. Both pages are live, in the sitemap and not indexed. This workstream was briefed never to request indexing, so it waits for a plain yes.

## Waiting on external systems

- Collections: the approved redirects (both Tesco tee URLs → /products/crooks-express-t-shirt; large-duffle-bag, joggas-1 and the 2005-drop pink CRSDR URLs) and `seo.hidden` on /collections/frontpage.
- Google: indexing of /collections/outerwear and the fit article; recrawl dropping /cart, /search, the -1 collections and black-set from the index.
- Search Console data for a clean window: 26 Oct – 1 Nov (after T-shirt Week), readable around 3 Nov.
- Fresh CrUX data for Core Web Vitals.

## Next actions

1. **14 Nov (scheduled):** 28-day read, 16 Oct – 12 Nov, with lock and T-shirt Week days labelled; Indexing > Pages again; 4-week figures for each live change in the programme change log.
2. When collections reports the redirects and the frontpage change live: check them on the live site and in URL Inspection.
3. Recommended, not scheduled: a clean 7-day read of 26 Oct – 1 Nov around 3 Nov. It needs George's or the orchestrator's OK to add a fourth scheduled run.

## Expected impact

**Commercial:** High  
**SEO:** High  
**GEO:** Low  
**Confidence:** Medium

Search drives almost all brand traffic. "crooks" alone carries a third of impressions, and the brand+product clusters still land on the homepage instead of a collection. Fixing both uses existing URLs. The first non-branded clicks are landing on the right URLs (sweats for 550gsm, HydroCuff for water-reactive), but volumes are still tiny.
