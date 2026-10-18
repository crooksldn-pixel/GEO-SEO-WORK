<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 09 · Core Web Vitals and technical performance

Status: audit done, read-only; user decisions on popup and apps received 16 Oct 15:33, spec below (section "Update 16 Oct"). Nothing changed in Shopify or the theme.
Implementer: workstream 01 thread (owns the master queue and all store/theme writes).
Sources: Shopify Admin API reads of the live theme "CROOKSLDN — SEO round 2 (from live 16 Oct)" (gid 207329132887): `layout/theme.liquid`, `snippets/scripts.liquid`, `stylesheets.liquid`, `fonts.liquid`, `meta-tags.liquid`, `crack-the-cuffs.liquid`, `crooks-schema-product.liquid`, `assets/crooks.css`, `config/settings_data.json` (app embeds), `templates/index.json`, `product.json`, homepage/PDP/collection sections; products, redirects and markets via Admin API; live reads of robots.txt, all sitemaps, /collections/tracksuits and /blogs/news.

## Evidence limits (read this first)
- **No field or lab metrics were captured.** The keyless PageSpeed Insights API returned `429 Queries per day exceeded` (shared quota); CrUX needs an API key; curl and Playwright to crooksldn.com are blocked by this environment's proxy; treo.sh renders client-side. So there is no LCP / INP / CLS number in this file, and nothing below claims the site is fast or slow.
- Findings are therefore from theme code and configuration. Each one says what it would affect; none should be implemented for score alone.
- To get real numbers: Search Console → Core Web Vitals report (workstream 04/10 have the access question), or a free PSI/CrUX API key added to the environment. A small store may have no CrUX origin data at all; if so, GSC will say "not enough data" and lab tests are the only signal.

## Current state (verified in code)
Someone has already done careful performance work on this theme (comments in the code record measured fixes), so the basics are in place:
- Hero/product/collection images: first image `loading=eager` + `fetchpriority=high`, the rest lazy; `image_tag` with `sizes` gives responsive srcset from Shopify's CDN (WebP/AVIF served automatically). Width/height attributes come from `image_tag`, so no image-driven CLS. (`sections/crooks-exhibit-record.liquid:159-180`, `crooks-exhibit-log.liquid:434-463`, `crooks-sightings.liquid:174-189`)
- Homepage hero is text (board canvas is off: `templates/index.json` `show_board: false`), so homepage LCP is text or the first Sightings image, which is already eager/high.
- Fonts: VT323 preload URL fixed to match the CSS request (comment in `layout/theme.liquid` records a 28px buy-panel reflow it cured); CRX Mono uses `font-display: swap`.
- Header height is computed inline before paint to prevent layout shift.
- Horizon's search modal, predictive-search.js and dialog were removed from every page; the 166 KB Base44 game is no longer loaded on PDPs or cart and only loads after a click on RUN IT.
- All theme JS is `defer` or `type=module` with `fetchpriority=low`; no render-blocking theme script.
- Crawl: robots.txt is Shopify's default (blocks cart/checkout/account, `sort_by`, `+` tag-combination URLs and multi-filter URLs; no AI crawlers blocked; no crawl-delay). Canonical is Shopify's `canonical_url`, which drops filter/sort/variant parameters. Search and cart are `noindex, follow`. Single domain with no market subfolders, so no hreflang to manage. Redirects exist for old product handles and the stale `-1` collections.
- Sitemaps: 21 products, 8 collections, 6 pages, 1 blog; the four "Set" products are deliberately `seo.hidden` (they are a buying mechanism; tracksuit intent is served by /collections/tracksuits, which lists the six real pieces).

## Ranked opportunities

| Rank | Class | Action | Commercial ROI | SEO | GEO | Effort | Confidence | Dependencies | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | P1 | **Get a CWV baseline before any perf work**: GSC Core Web Vitals report (mobile + desktop, URL groups) and one PSI run each for home, a PDP (/products/v1-hoodie), a collection (/collections/sweats) | Enables everything below; prevents wasted theme work | Real page-experience status | None directly | 15 min with access | High | GSC access (WS04/WS10) or a PSI API key | Blocked on access |
| 2 | P2 | **Audit and trim third-party app embeds** loaded on every page: Orderify (preorders now come from the CROOKS Operations app block on `product.json`, so Orderify may be unused), Judge.me core + Judge.me cart-drawer widget (cart drawer is never rendered; reviews are not shown anywhere), Mida session-replay recorder | Medium: less main-thread work on mobile PDPs = better INP and add-to-cart responsiveness | INP/LCP on mobile | None | 30 min to verify each app, minutes to toggle | Medium (app weights unmeasured) | User: is Orderify still used? Is Mida still being watched? WS02 rank 6 wants Judge.me reviews shown instead | Proposed |
| 3 | P3 | Homepage "Getaway" popup: full-screen overlay 3 s after load on first visit, mobile included. Google treats full-screen mobile interstitials on search landing pages as a negative page-experience signal, and the homepage takes most branded search traffic | Unknown: it's a discount capture, so removing it could cost signups | Small ranking risk on the brand's strongest page | None | 30 min theme | Medium | **Business call**: keep as is / show as a bottom banner on mobile / show from the second pageview | Proposed |
| 4 | P3 | Render-blocking CSS: `base.css` (104 KB raw, Horizon) + `crooks.css` (101 KB raw, about a third of it comments) load before first paint on every page. Much of Horizon's base.css styles components the Crooks sections replaced | Low-med | FCP/LCP on slow mobile | None | 3–6 h (needs careful coverage testing) | Low until PSI shows CSS on the critical path | Rank 1 | Hold for data |
| 5 | P3 | Trim `snippets/scripts.liquid`: about 25 Horizon module scripts load on every template, including ones unused here (quick-add with quick add off, slideshow/layered-slideshow, volume pricing, comparison/sticky ATC on non-PDP pages; `fly-to-cart.js` is loaded twice on PDPs) | Low | Small INP/TBT gain | None | 2 h + regression test | Low-med | Rank 1; theme lock (WS01) | Hold for data |
| 6 | P3 | Archived products with no redirect now 404: `og-crook-tee`, `3-clives-tee`, `broadcast-tee`, `evil-clive-tee`, `large-duffle-bag` | Low unless they still get clicks or links | Recover any link equity / impressions | Low | 10 min (redirect tees → /collections/tees) | Medium | Check GSC for impressions/links first (WS04) | Proposed |
| 7 | P4 | `/collections/frontpage` is in the sitemap and indexable; it duplicates the homepage product set | Low | Thin duplicate URL | None | 5 min (hide from Online Store channel or unpublish) | Medium | Confirm nothing links to it | Proposed |
| 8 | P4 | New blog article "Convict 550gsm vs Cellblock 450gsm: how they fit" is live at /blogs/news but not yet in `sitemap_blogs_1.xml` | Low | Discovery speed only | Low | none, or request indexing in GSC | Medium (likely sitemap lag) | GSC | Recheck 17 Oct |

Nothing found qualifies as P0: no `noindex` on money pages, no blocked resources, no canonical errors, no render-blocking third-party script in the theme code.

## Hand-offs to other workstreams
- **WS02 / WS03 (schema and feed parity):** `crooks-schema-product.liquid` emits `priceCurrency` from `cart.currency`, and the store has six active markets (UK, EU, US/Canada, ANZ, Channel Islands, all world) on one domain. If Googlebot (crawling from the US) is shown USD, the PDP schema says USD while Merchant Center is GBP. The theme already guards shippingDetails with `if GBP`, which suggests non-GBP renders happen. Worth checking with the Rich Results Test / URL Inspection rendered HTML. Not verified from here.
- **WS02:** the schema comment says "no reviews app is installed", but Judge.me is installed and embedded sitewide. That's consistent with WS02's rank 6 finding; whichever way it goes (show reviews or disable the embed), rank 2 above follows it.
- **WS02:** `crxst-rz-t-shirt` shows total inventory −2 (oversold), matching WS02's P0 on zero-stock tees.

## Recommended implementation order
1. Get the baseline (rank 1). Without it, ranks 4–5 are guesses and should not be done.
2. Rank 2 is the only change worth doing without numbers, because it removes work rather than reshaping the page, and each app can be switched back on in the theme editor. It needs the user's answer on Orderify and Mida, and WS02's decision on Judge.me.
3. Rank 3 is a business decision; it goes to the user with the master queue, not before.
4. Ranks 6–8 are quick crawl hygiene for the WS01 thread to batch with other store edits.

## Metrics to monitor
GSC Core Web Vitals (mobile "Good URLs" share, LCP/INP/CLS per URL group); GSC Page indexing (404s, "Duplicate without user-selected canonical"); Shopify Analytics mobile add-to-cart rate before/after rank 2. Do not record an improvement from a deploy alone.

---

## Update 16 Oct 2026 15:50 UTC · user decisions on ranks 2 and 3

User (15:33): popup "keep the offer, but delay and soften it… trigger after meaningful engagement/time/scroll and ensure it is easy to dismiss on mobile". Apps: "audit both before removal… if nobody is actively reviewing Mida recordings or using its insights, disable/remove it. Also identify any other installed scripts/apps with no measurable operational or conversion value."
Implementer: the Crooks GEO and SEO programme thread (workstream 01). Everything below is a spec; nothing has been changed.

### A. App and script audit (evidence)

Method: app embeds in `config/settings_data.json` and app blocks in templates (live theme); shop, product and order data via Admin API. The API denies `appInstallations` and `scriptTags`, so apps that inject through ScriptTags or web pixels (Settings → Customer events) can't be seen from here; check those two admin screens by hand.

| App / script | Loads on | Evidence of use | Verdict | Action | Reversible? |
|---|---|---|---|---|---|
| **Orderify** (app embed `orderify/script_js`) | Every page | (Withdrawn 18:45: used for customer cancel/edit, see correction) None found. No Orderify metafields on the shop or any of the 25 active products; no selling plan groups; no line-item properties, tags or attributes on the last [n] orders (7–16 Oct, CROOKS-[order] to 2197). Pre-orders now run through the CROOKS Operations app block on `templates/product.json`. | No measurable value | Turn the embed off in Theme editor → App embeds. Uninstall after the user opens the Orderify admin and confirms there are no active pre-order campaigns | Yes (toggle) |
| **Mida replay/heatmaps** (`mida_recorder`) | Every page, records every session | Can't be seen through the API. Only the user can say whether anyone watches the recordings. | Disable unless someone names a current use | Turn the embed off. If nobody has missed it within 30 days, uninstall it, which also ends its data processing | Yes |
| **Judge.me cart-drawer widget** (`judgeme/cart_drawer_widget`) | Every page | The cart drawer is never rendered (`layout/theme.liquid` comment; Crooks header links straight to /cart) | No value | Turn the embed off | Yes |
| **Judge.me core** (`judgeme_core`) | Every page | Collecting reviews (product review data updated as late as 13 Oct; 37 reviews per WS02), but no Judge.me widget or stars are rendered in the Crooks sections | Keep, but it's paying a sitewide cost for nothing visible | Follow WS02 rank 6: show reviews (and add `aggregateRating`) and the cost is justified. Review request emails run server-side and don't need the embed | n/a |
| **Crooks Partner Hub** (`creator-gift`) | Every page | Custom app; what it does can't be read from here | Unknown | User: what does it do on the storefront? If it only serves creator gift links, limit it to the pages that need it | — |
| Shopify Forms (`forms` embed) | Every page | Used: inline form block on the homepage (`templates/index.json`) | Keep | — | — |
| Omnisend (`app-embed`) | Every page | Email/SMS marketing and tracking | Keep | — | — |
| Notify Me | Already disabled | — | — | Uninstall if not coming back | — |
| Horizon module scripts (`snippets/scripts.liquid`) | Every page | About 25 modules, several unused (quick-add while quick add is off, slideshows, volume pricing; `fly-to-cart.js` loaded twice on PDPs) | Low value | Still rank 5: wait for a baseline | Yes |

Order of work: Orderify, Judge.me cart widget and Mida (if confirmed) are three theme-editor toggles with no code change. Before/after, record Shopify Analytics mobile conversion rate and add-to-cart rate (7 days each side), and a PSI mobile run of `/products/v1-hoodie` if a key exists by then.

### B. Homepage popup ("The Getaway"), delayed and softer spec

Current behaviour (`snippets/crack-the-cuffs.liquid`): homepage only. Opens 3 s after DOMContentLoaded (`DELAY = 3000`) for anyone not snoozed or won. It covers the full screen on phones (`.ctc-sheet` 100% height under 750px), dims and blurs the page, locks scroll (`documentElement.style.overflow = 'hidden'`) and sets `aria-hidden` on the rest of the page. A bare close spends nothing, so it comes back on the next homepage view.

Keep: the offer copy, RUN IT → game iframe (user-initiated, so full screen is fine at that point), NOT NOW = 14-day snooze, a win suppresses for good, the consent-banner and drawer waits, `?ctc=1` force-open for testing, and the focus and Escape handling.

Change:
1. **Trigger (all devices):** don't open on a timer from load. Open on the first of these:
   - the visitor has scrolled at least 50% of the homepage **and** spent 10 s or more on it;
   - it is their 2nd or later page view this session and they are back on the homepage (count page views in `sessionStorage`);
   - desktop only: exit intent (pointer leaves through the top of the viewport) after 10 s or more on the page.
   Never sooner than 10 s after load. Never while a consent banner, drawer or dialog is open (existing `whenClear`).
2. **Mobile (< 750px), before RUN IT: bottom sheet, not a full-screen overlay.**
   - Sheet anchored to the bottom and at most 40% of the viewport height. No backdrop dim or blur, no scroll lock, no `aria-hidden` on the page.
   - Non-modal: `role="dialog"` with `aria-modal="false"` and an `aria-labelledby` title. Move focus to the sheet's heading once. No focus trap, because the page behind stays usable.
   - Close: a 44×44px "×" inside the sheet, top-right. Escape also closes it, and so does tapping the page behind on mobile.
   - Content: the title in one smaller line (24–28px), the one-line offer, then RUN IT and NOT NOW side by side.
   - On RUN IT, expand to the current full-screen sheet with the game. Full screen is fine here because the visitor asked for it; keep scroll lock and the focus trap for this state only.
3. **Desktop (≥ 750px):** keep the centred modal with the new trigger only.
4. **Dismissal memory:** a bare close (× or Escape) suppresses it for the rest of the session (`sessionStorage`). NOT NOW stays 14 days. A win stays permanent.
5. **Measurement:** publish custom events through `Shopify.analytics.publish` for `ctc_shown`, `ctc_run`, `ctc_not_now`, `ctc_close` and `ctc_win`. Compare popup signups per 1,000 homepage sessions for 14 days after the change against the 14 days before (Omnisend/Forms signups). If signups fall a lot, the next lever is the trigger, not a return to the full screen.
6. **Performance guard:** no new resources. Keep the preconnect deferred until the sheet opens, and keep the iframe loading only on RUN IT. The sheet is `position: fixed` so it adds no CLS. Test that it doesn't become the LCP element (it opens after 10 s, well after LCP).

Acceptance checks for the implementer: on a 390px-wide phone the header, hero and first product row stay visible and scrollable with the sheet open; × is reachable with one thumb; nothing appears in the first 10 s or without scrolling; `?ctc=1` still forces it; keyboard Tab and Escape work on desktop; the game still opens and the `getaway:*` postMessage contract still works.

Metric to monitor: popup signup rate (above); homepage bounce rate and mobile conversion rate in Shopify Analytics; GSC page experience for the homepage once there's data. Don't claim a ranking effect from this change.

## Owner decisions, 16 Oct 2026 18:30 UTC (override earlier recommendations in this file)
- Theme copy "Claude P1 fixes" (schema and popup): **HOLD**, do not publish.
- Product-data batch 2: **APPROVED**, except that barcodes must not be removed or remapped (item bags use them).
- Google Shopping gender: **MIXED.** Crooks sells men's and women's products, so assign gender per product, never one catalogue-wide value.
- Tracksuits: **YES**, list the three Convict Sets.
- Judge.me reviews on product pages: **NO** for now.
- Mida: **KEEP** (in use). Crooks Partner Hub: **KEEP.** Orderify: no live campaigns, so turn the embed off and prepare removal once no other dependency is found. **(Superseded 18:45: Orderify is used for customer cancel/edit; keep it on. See correction at the end.)**
- About page: **not approved yet**; keep it drafted. "Designed in-house" = true; "free size swaps" = true.
- Official profiles for sameAs: https://crooksldn.com, Instagram @crooksldn, TikTok @crooksldn **only**. Not crooksldn.uk, X, YouTube, Pinterest or Depop.
- Tier-1 creator samples: **declined for now**.

---

## Update 16 Oct 2026 18:40 UTC · user decisions (18:29)

Decisions: Claude P1 fixes theme on HOLD (don't publish); Judge.me reviews NOT shown on PDPs for now; **Mida KEEP** (in use); **Orderify: no live campaigns, prepare for removal if there's no other dependency**; **Crooks Partner Hub creator gift: KEEP**.

Resulting app plan (supersedes table A above):
| App | Decision | Dependency check | Next step |
|---|---|---|---|
| Orderify | ~~Remove~~ HOLD, see correction below | ~~No other dependency found~~ (withdrawn: used for customer cancel/edit): no shop, product or variant metafields (checked all 25 active products and the first 50 variants), no selling plans, no order properties or tags on the last [n] orders, no theme code or app block referencing it; the only trace is the app embed in `settings_data.json`. Pre-orders run on CROOKS Operations. | 1) Switch off the Orderify app embed (Theme editor → App embeds). 2) After 7 days with no pre-order or checkout issues, uninstall it in Settings → Apps. Uninstalling is the one irreversible step and is already approved, conditional on this check. |
| Judge.me cart-drawer widget | Off | Cart drawer never renders | Switch off the app embed |
| Judge.me core | Keep installed; consider switching off its storefront embed | Reviews stay hidden by decision, so the embed loads on every page with nothing (or only Judge.me's own floating widgets) shown. Review collection emails run server-side and don't need the embed. | Optional. Switch it off only if Judge.me's popup or trust badge isn't wanted on the site either. Check the live site for a floating reviews tab first |
| Mida | Keep | — | No action. Consider limiting recording to key templates in Mida's settings to reduce cost on every page |
| Crooks Partner Hub | Keep | — | No action |

How these get done: app-embed toggles live in the live theme's `settings_data.json`, which the Shopify connector can't write (writes go to unpublished themes only, and the P1 theme is on hold). So the two "off" toggles are about one minute each for the user in Theme editor → App embeds on the live theme. That has no effect on the held theme work.

Popup spec (B): stays parked with the held theme. Build it on the unpublished theme now if the programme thread wants it ready, but it goes live only with the theme release.

---

## Correction 16 Oct 2026 18:45 UTC · Orderify is NOT safe to remove

The programme thread found Orderify **is used** for customer self-service order cancel/edit: [n] orders, most recent 26 Sep 2026. My dependency check (metafields, selling plans, order tags/attributes on the last [n] orders) missed this because those edits don't leave the traces I checked, and 26 Sep falls outside the 40-order window. Everything above that says Orderify has "no measurable value", "no other dependency found" or "Remove" is withdrawn.

Current status: **keep Orderify installed and its app embed on** until the user decides whether to keep self-service cancel/edit (the programme thread has asked). If they drop the feature, the removal steps above apply (embed off, then uninstall after 7 days). If they keep it, Orderify stays and nothing changes.

Unchanged: Judge.me cart-drawer widget off (cart drawer never renders); Judge.me core embed optional off; Mida and Partner Hub kept.
