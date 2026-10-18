<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Workstream 6 · CROOKSLDN entity consistency and About architecture

Audited 16 Oct 2026 (read-only). Owner of implementation: workstream 1 thread (sole writer to Shopify/theme). Nothing here has been changed on the store.

## Current state (evidence)

| Surface | How the brand is described | Source |
|---|---|---|
| Shop record | name `CROOKSLDN`; **description blank**; email team@crooksldn.com; country UK | Admin API `shop` |
| Homepage title / meta | "Crooks London Streetwear \| Fleece, Denim & Tees" / "CROOKSLDN, the Crooks London streetwear label: 550gsm Convict fleece, 14oz Yard denim, graphic tees and MotionTec socks…" (theme fallback in snippets/meta-tags.liquid) | live theme 207329132887; WebFetch of crooksldn.com |
| Homepage copy | Tagline "OWN THE STREETS™"; no sentence saying what CROOKSLDN is, where it is from or who runs it | WebFetch |
| Footer | "EVIDENCE TERMINAL v0.2 // CROOKSLDN // OWN THE STREETS™ // © 2026 - BUILT BY MRCROOKS"; links to Instagram, TikTok, two base44 games | WebFetch |
| About page | **Does not exist.** Pages: contact, data-sharing-opt-out, tracking, terms, faq, returns, t-shirt-week (unpublished). No /pages/about redirect | Admin API `pages`, `urlRedirects` |
| Blog | "News", 1 article | Admin API |
| Organization JSON-LD | name CROOKSLDN; legalName "Crooks Clothing Company Ltd"; alternateName ["Crooks London","Crooks"]; Brand @id; MerchantReturnPolicy; description = hard-coded fallback (because shop description is blank); sameAs = footer social links on an allowlist (Instagram, TikTok); contactPoint email; **no address, foundingDate, founder, identifier, logo verified** | snippets/crooks-schema-site.liquid |
| WebSite JSON-LD | same name + alternateName, SearchAction | same file |
| Companies House | CROOKS CLOTHING COMPANY LTD, 16606021, active, incorporated 24 Jul 2025, registered office Unit M [town redacted], [town redacted], [town redacted], SIC 47710 | [Companies House](https://find-and-update.company-information.service.gov.uk/company/16606021) |
| Trustpilot | name "**Crooks ldn**"; about "Streetwear Brand"; address [town redacted] [town redacted]; claimed Feb 2026; **50 reviews, TrustScore 3.3 "Average"** | [Trustpilot](https://uk.trustpilot.com/review/crooksldn.com) |
| Instagram | display name "**CrooksLdn**" (@crooksldn) per search result title; bio not readable (robots block) | WebSearch |
| TikTok | @crooksldn; a TikTok Shop search page exists for "crooksldn joggers"; bio not readable | WebSearch |
| Web search for "Crooks London" / "CROOKSLDN Crooks LDN streetwear" | Results are **Crooks & Castles** (US brand) and Crooked Tongues; no CROOKSLDN result | WebSearch (US index, so indicative only) |

## Findings and ranked opportunities

Priority = expected commercial impact × likelihood of success × implementation speed.

### E1 · No About / entity page exists — **P1**
- **Evidence:** pages list above; homepage has no "what is CROOKSLDN" sentence.
- **Affected:** new /pages/about (handle choice: `about`, the conventional path, rather than `about-crooks`); footer and main menu links.
- **Opportunity:** one page that answers "What is CROOKSLDN?" for search engines and AI assistants: names (CROOKSLDN / Crooks LDN / Crooks London), what it makes (550gsm Convict fleece, 14oz Yard denim, tees, reactive outerwear), how it sells (drops, numbered/sealed), where it is based, who runs it, official profiles, reviews, contact.
- **Commercial impact:** medium; indirect via trust and branded/category queries. **SEO:** medium (brand SERP, sitelinks). **GEO:** high; assistants currently have no first-party description to cite and confuse "Crooks" with Crooks & Castles.
- **Effort:** low-medium (page + template section in brand style; copy needs facts from the owner). **Confidence:** high that it helps entity resolution; medium on measurable revenue.
- **Dependencies:** owner facts (questions below); workstream 1 for theme/template and menu edits.
- **Recommended implementation:** short, on-brand page (not an SEO wall): 1-line definition, 3-4 short sections, product-line links into collections, profile links, contact. Add `AboutPage` JSON-LD with `mainEntity` → `#organization`. Link from footer and the main menu.
- **Status:** proposed; blocked on owner facts.

### E2 · "Crooks LDN" missing from alternateName; naming varies across profiles — **P1 (quick)**
- **Evidence:** schema alternateName is ["Crooks London","Crooks"]; GEO query set tracks "Crooks LDN" and "Crooks LDN reviews"; Trustpilot says "Crooks ldn", Instagram says "CrooksLdn".
- **Affected:** snippets/crooks-schema-site.liquid (Organization, Brand, WebSite); Trustpilot business name; Instagram display name.
- **Recommended:** alternateName ["Crooks LDN","Crooks London","Crooks"] on Organization, Brand and WebSite. Owner sets Trustpilot display name to "CROOKSLDN" (or "Crooks LDN") and description to the same one-line definition used on site.
- **Impact:** SEO low-medium, GEO medium; effort minutes; confidence high. **Status:** proposed (theme part for workstream 1; profile part for owner).

### E3 · Shop description blank, so every entity description is a hard-coded fallback — **P2**
- **Evidence:** `shop.description` = ""; schema falls back to "CROOKSLDN (Crooks London) is a streetwear label making…". It never says British/UK or independent.
- **Recommended:** set Online Store › Preferences description to one approved definition sentence (owner wording) and reuse it verbatim on the About page, Trustpilot, Instagram/TikTok bios. One definition everywhere is the core of entity consistency.
- **Effort:** minutes once wording is approved. **Confidence:** high. **Dependency:** owner approval of the sentence. **Status:** proposed.

### E4 · Location signals conflict: "London" brand, [town redacted] ([town redacted]) registered office — **P1 decision, owner only**
- **Evidence:** brand name and copy say London; Companies House and Trustpilot list [town redacted] [town redacted]; schema states no address.
- **Why it matters:** "London streetwear brands" and "British streetwear brands" are target queries; assistants weigh stated location. Stating London without basis would be inventing a fact.
- **Recommended:** owner states the truthful framing (e.g. founded in / connected to London, operating from [town redacted]). Then add `foundingLocation` and/or `address` (`addressLocality`, `addressRegion`, `addressCountry: GB`) to Organization only as approved. Keep street address off the About page unless owner wants it.
- **Status:** needs owner answer.

### E5 · No founder, founding date or history anywhere — **P2**
- **Evidence:** footer "BUILT BY MRCROOKS" is the only founder signal; schema has no founder/foundingDate. Owner's message mentions a [age redacted] founder and £[redacted]+ revenue (not yet approved for publication). Company incorporated 24 Jul 2025, but the brand may predate it.
- **Recommended:** if owner approves, add founder (name or chosen public alias) and brand start year to About page and `founder` / `foundingDate` in schema. The founder story is also the main outreach angle for workstream 7, so the About page doubles as the press reference.
- **GEO:** medium-high (founder stories are what editorial and AI answers repeat). **Status:** needs owner answer.

### E6 · Weak sameAs graph — **P2**
- **Evidence:** sameAs = Instagram + TikTok only (footer-driven). Companies House record and Trustpilot are not linked.
- **Recommended:** add `identifier` {PropertyValue, propertyID "Companies House", value "16606021"} (verified fact); add any other official profiles the owner confirms (YouTube, X, Pinterest, Depop/Vinted shop, TikTok Shop) via footer social blocks so the allowlist picks them up. Do not put Trustpilot in sameAs (a review listing is not the organisation's profile); link it from the About page instead.
- **Effort:** low. **Confidence:** medium-high. **Status:** proposed; profile list needs owner.

### E7 · Disambiguation from Crooks & Castles — **P2 (addressed through E1–E3, E8)**
- **Evidence:** "Crooks London" searches return Crooks & Castles articles; bare alternateName "Crooks" is ambiguous.
- **Recommended:** keep "Crooks" as an alternate but always pair it with LDN/London and UK in descriptions; About page states plainly "CROOKSLDN is not affiliated with Crooks & Castles" only if owner agrees (useful for AI answers, harmless to users). Track GEO rows "Crooks LDN" / "Crooks London" for confusion.
- **Status:** proposed.

### E8 · Trustpilot reputation: 3.3 from 50 reviews — **P1 flag (contradicts project memory)**
- **Evidence:** live Trustpilot 3.3 "Average", 50 reviews. Project memory lists Trustpilot as a strength.
- **Why it matters:** AI assistants quote TrustScore when asked "Crooks LDN reviews" (a tracked GEO query). This is reputation, not markup, and is not fixable by schema.
- **Recommended:** a separate review/support investigation (what the low reviews say, reply to each, invite post-delivery reviews through Trustpilot's own invitation flow). No fake or incentivised reviews. Do not add AggregateRating from Trustpilot to on-site schema (Google ignores self-serving third-party ratings on Organization).
- **Status:** flagged for coordinator; needs owner awareness.

### E9 · Organization type, logo — **P3/P4**
- `OnlineStore` (Organization subtype) is slightly more precise than `Organization`: P4, cosmetic.
- Logo is emitted only if `settings.logo` is set; could not verify from cloud (scripts stripped). Workstream 1 should confirm with Rich Results Test: P3.
- Wikidata/Wikipedia entry: brand does not yet have independent coverage to meet notability; creating one would be self-promotion. P4, revisit after press (workstream 7).

## Recommended implementation order (for the coordinator queue)
1. Owner answers the questions below (unblocks E1, E3, E4, E5).
2. E2 alternateName fix + E6 identifier: one small edit to snippets/crooks-schema-site.liquid, batch with workstream 1's next theme port.
3. E3 shop description → reused in bios and Trustpilot (owner can do profiles in minutes).
4. E1 About page (template + copy + AboutPage JSON-LD + footer/menu link).
5. E8 runs separately as a reputation task.

Metrics to monitor: GEO rows "Crooks LDN", "Crooks London", "Crooks LDN reviews" (mentioned, description accuracy, confusion with Crooks & Castles); GSC impressions/clicks for /pages/about and brand queries; Rich Results Test showing Organization with new fields.

## Questions only the owner can answer
1. One-sentence definition you want used everywhere (or approve a draft).
2. Location framing: is the brand London-based, London-founded, or run from [town redacted]? What may be stated publicly?
3. Founder: publish a name, the alias "MRCROOKS", or nothing? Approve stating [age redacted]?
4. When did the brand start trading (before the Jul 2025 incorporation)?
5. Official profiles beyond Instagram and TikTok (YouTube, X, Pinterest, Depop, TikTok Shop, Snapchat)?
6. Where is the clothing made / where do the 550gsm fleece and 14oz denim come from (only if you want it public)?
7. Any real press, stockists or collaborations to cite?
8. Okay to state "not affiliated with Crooks & Castles"?
9. Revenue figure (£[redacted]+): for outreach only, or never public?

## Update 16 Oct 2026 (owner answers received)
Owner answered items 10-18. Draft definition, About copy, schema delta and profile check: [06-about-draft.md](06-about-draft.md). E2, E3, E5, E6 (schema part) are now unblocked; E1 copy awaits owner approval; E4 resolved as "British / UK", no London or [town redacted] claims.

## Owner decisions, 16 Oct 2026 18:30 UTC (override earlier recommendations in this file)
- Theme copy "Claude P1 fixes" (schema and popup): **HOLD**, do not publish.
- Product-data batch 2: **APPROVED**, except that barcodes must not be removed or remapped (item bags use them).
- Google Shopping gender: **MIXED.** Crooks sells men's and women's products, so assign gender per product, never one catalogue-wide value.
- Tracksuits: **YES**, list the three Convict Sets.
- Judge.me reviews on product pages: **NO** for now.
- Mida: **KEEP** (in use). Crooks Partner Hub: **KEEP.** Orderify: no live campaigns, so turn the embed off and prepare removal once no other dependency is found.
- About page: **not approved yet**; keep it drafted. "Designed in-house" = true; "free size swaps" = true.
- Official profiles for sameAs: https://crooksldn.com, Instagram @crooksldn, TikTok @crooksldn **only**. Not crooksldn.uk, X, YouTube, Pinterest or Depop.
- Tier-1 creator samples: **declined for now**.
