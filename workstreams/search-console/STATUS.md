# Workstream: Search Console analysis

> **18 Oct 2026, 17:03 UTC — George answered the consolidated decision pack.** His answers for this workstream are in [ANSWERS.md](ANSWERS.md), copied onto each question in [QUESTIONS.md](QUESTIONS.md). Q1, Q3 and Q4 are answered; Q2 is parked. Project files are on `cowork/project-files-import`.

**Branch:** cowork/search-console  
**Owner:** Cowork session  
**Last updated:** 18 Oct 2026, 20:20 BST  
**Priority:** P1  
**Overall status:** WAITING ON EXTERNAL

## Objective

Use Google Search Console to find commercial queries where an existing crooksldn.com URL can rank better, preferring URLs with momentum over new pages. Record a baseline, index hygiene, Core Web Vitals, sitemap status and Product structured-data currency, then measure what the other workstreams' changes do.

This workstream changes nothing on the store, the theme, Merchant Center or Search Console.

## Current state

The research is done and recorded, George's answers are applied, and the three follow-up reads are scheduled.

**New, 18 Oct evening: the whole store is password-locked** (FINDINGS 13). Since some time after 17:05 BST, every URL redirects to /password, Googlebot included, and /sitemap.xml returns 404. It's probably the T-shirt Week launch, but nothing in the programme records says so. While it lasts, Google can't crawl the new pages or the approved redirects, and brand searches land on a password page.

Other limits on the data:
1. Search Console has no data for 23 Jul – 14 Oct 2026 (FINDINGS 1). Jan–Jul is pre-relaunch reference data; the post-deploy anchor is 15–16 Oct.
2. Indexing > Pages is still processing (property re-added 16 Oct). In-scope URLs were checked one by one with URL Inspection instead.
3. T-shirt Week (Mon–Sun, presumed 19–25 Oct) and the lock both fall inside the first 7-day window, so that window can't be read as an SEO before/after.

The ranked actions are for other workstreams (FINDINGS 12). Collections now has approval for the redirects (Tesco tees → /products/crooks-express-t-shirt, plus the others) and for hiding /collections/frontpage (owner decision #21).

## Completed

- **Measured:** UK Performance (queries, pages, daily) for 21 Jan – 22 Jul 2026 and 15–16 Oct 2026; first-half vs second-half comparison; query → page breakdowns for every product cluster. `artifacts/gsc-exports/`
- **Measured:** branded vs non-branded baseline. Jan–Jul UK: 14,312 clicks, 35,948 impressions; branded 12,303 clicks; genuinely non-branded 1 click and 187 impressions. Anchor 15–16 Oct UK: 86 clicks, 295 impressions, CTR 29.2%, position 4.6.
- **Researched:** ranked opportunity list, 14 rows with owners. `artifacts/opportunities.csv` (row 3 updated with George's Tesco tee answer).
- **Audited:** URL Inspection (indexed view) on 13 URLs, 15 inspections across 16 and 18 Oct; live status and redirects of every in-scope URL; Sitemaps, Core Web Vitals, HTTPS, Shopping and Crawl stats reports.
- **Tested:** live URL test on /products/convict-hoodie-1. Rendered Product JSON-LD shows priceCurrency GBP, and the 5 merchant items are valid.
- **Audited (18 Oct, 20:09–20:11 BST):** store-wide password lock (FINDINGS 13).
- **Written:** full report `artifacts/search-console-report.md` and `FINDINGS.md` (13 findings).
- **Scheduled:** read-only checks for 20 Oct, 24 Oct and 14 Nov (NEXT.md).

## Currently working on

Nothing currently running. Next scheduled run: 20 Oct 2026, 10:00 BST.

## Blockers

### Blocker 1 — Store password-locked

**Blocking:** URL Inspection and live tests of the new and redirected URLs, Google's crawling of them, the sitemap fetch, and any clean post-deploy measurement window  
**Needs:** the store to reopen, and the lock dates so they can be labelled  
**From:** George  
**Severity:** P1  
**Can work around it?:** Partly  
**Workaround:** Keep reading Search Console data, and label lock days so they're left out of comparisons.

### Blocker 2 — Indexing > Pages report still processing

**Blocking:** The site-wide list of reasons pages aren't indexed (task 6)  
**Needs:** Google to finish processing the newly added property  
**From:** Google  
**Severity:** P3  
**Can work around it?:** Yes  
**Workaround:** URL Inspection on each in-scope URL (done; see FINDINGS 6–8).

## Waiting on George

1. Is the store's password lock (from the evening of 18 Oct) intentional, and when does it reopen? (FINDINGS 13)
2. Once it reopens: OK to click **Request indexing** in Search Console for /collections/outerwear and /blogs/news/convict-vs-cellblock-fit? Both are live pages Google hasn't indexed. Asked in chat, because this workstream was briefed never to request indexing.

## Waiting on external systems

- Store reopening (see Blocker 1).
- Collections creating the approved redirects and hiding /collections/frontpage.
- Search Console data accumulation, and Indexing > Pages processing.
- Google recrawl: /collections/outerwear ("Discovered – currently not indexed"), the fit article (unknown to Google), /collections/tees-1 (indexed, now a 301), /products/convict-hoodie-1 (indexed copy from 7 Oct shows missing variant images; live page passes).
- Fresh CrUX data for Core Web Vitals (Search Console's copy stops at 23 Jul).

## Next actions

1. **20 Oct (scheduled):** lock status; Indexing > Pages; URL Inspection on outerwear, the fit article, /collections/frontpage and a Tesco tee URL.
2. **24 Oct (scheduled):** first read from 15 Oct onward, with lock and T-shirt Week days labelled and left out of the comparison with the 15 Oct anchor.
3. After the store reopens and collections has made its changes: verify the redirects and the frontpage noindex on the live site and in URL Inspection.
4. **14 Nov (scheduled):** 28-day read, plus 4-week Search Console figures for each live change in `project-files/seo/change-log.md`.

## Expected impact

**Commercial:** High  
**SEO:** High  
**GEO:** Low  
**Confidence:** Medium

Search drives almost all brand traffic. "crooks" alone carries a third of impressions and lost 1,076 clicks in a quarter, and the brand+product clusters (joggers, jeans, jorts, tees) all land on the homepage instead of a collection. Fixing both uses existing URLs. Confidence is medium because the reference data predates the relaunch, and the first post-deploy week is distorted by the lock and T-shirt Week.
