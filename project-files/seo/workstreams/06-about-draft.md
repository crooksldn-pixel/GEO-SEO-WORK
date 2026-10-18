<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# CROOKSLDN brand definition + About page draft (v1, 16 Oct 2026)

Status: **draft, needs owner approval of the copy before anything goes live.** Builder: the Crooks GEO and SEO programme thread (sole writer to Shopify/theme). Facts used come only from the owner's answers of 16 Oct 2026 and the live site; nothing below is inferred.

## 1. Canonical brand definition

**Full (site, schema, press notes):**
> CROOKSLDN is an independent British streetwear brand making heavyweight fleece, baggy denim, graphic tees and reactive outerwear, cut in oversized, street-led silhouettes and released in drops.

**Short (Instagram / TikTok bio, Trustpilot "about", directory listings, ≤150 chars):**
> Independent British streetwear. Heavyweight fleece, baggy denim, graphic tees and reactive outerwear. Released in drops.

Naming rule everywhere: **CROOKSLDN** first, then "Crooks LDN" or "Crooks London" as the alternates. Never "Crooks" on its own in a description.

Where to set it:
- Shopify › Online Store › Preferences › homepage meta description stays as is; **Settings › Store details / shop description** = full definition. The Organization schema already reads `shop.description`, so this one field fixes the schema description.
- Trustpilot business name → "CROOKSLDN"; about → short version. (Owner action in Trustpilot Business.)
- Instagram display name "CrooksLdn" → "CROOKSLDN" is optional; bio → short version. (Owner action.)

## 2. About page

- **URL:** /pages/about (title "About CROOKSLDN"). Conventional path users and crawlers expect.
- **Design:** the existing evidence-file/terminal style, same type and colours as the homepage; not a text wall. Each section is a short block.
- **Links in:** footer (next to QUESTIONS / TERMS), and the main menu.
- **SEO title:** About CROOKSLDN | Independent British Streetwear (47 chars)
- **Meta description:** CROOKSLDN (Crooks LDN) is an independent British streetwear brand: heavyweight fleece, baggy denim, graphic tees and reactive outerwear, released in drops. (154 chars)

### Copy

**H1: CROOKSLDN**

CROOKSLDN, also known as Crooks LDN and Crooks London, is an independent British streetwear brand. We make heavyweight fleece, baggy denim, graphic tees and reactive outerwear, cut oversized and released in drops.

**Founded by George Hinxman**
CROOKSLDN was started by George Hinxman and is still run independently. Every piece is designed in-house and sold direct from crooksldn.com.

**What we make**
- [Sweats](/collections/sweats): heavyweight Convict fleece hoodies, joggers and sets.
- [Denim](/collections/denim): baggy Yard denim.
- [Tees](/collections/tees): graphic T-shirts.
- [Outerwear](/collections/outerwear): the HydroCuff Windbreaker and the Double-Agent Puffa, reactive pieces that change when they meet water or heat.
- [Accessories](/collections/accessories): including MotionTec socks.

**How we drop**
New pieces go live to the list first. Orders are sealed, tagged and numbered before they leave us. Free UK shipping over £30, free size swaps and easy returns.

**Find us**
Instagram [@crooksldn](https://instagram.com/crooksldn) · TikTok [@crooksldn](https://tiktok.com/@crooksldn) · Reviews on [Trustpilot](https://uk.trustpilot.com/review/crooksldn.com) · team@crooksldn.com

<small>CROOKSLDN is a trading name of Crooks Clothing Company Ltd (company no. 16606021). CROOKSLDN is not affiliated with Crooks & Castles.</small>

### Copy notes for the owner
- "Every piece is designed in-house" and "still run independently": **please confirm both**; I took "independent" from your definition, but "designed in-house" is my wording.
- "reactive pieces that change when they meet water or heat" is the only reactive wording, and it describes the product names, not how the fabric works. Technical claims wait for the supplier data (your answer 21).
- **No 550gsm, 14oz, country of manufacture, age, revenue, founding year or location claims** (answers 11, 13, 15, 20, 22). Add each when evidenced.
- The company line sits in the footer-size small print only; no [town redacted] address and no reference to CROOKSLDN LTD (answer 14). Owner may remove it entirely; the schema `identifier` carries the company number anyway.
- The Crooks & Castles line appears **only here** (answer 18), because "Crooks London" searches currently return Crooks & Castles.

## 3. Schema changes (for the builder)

File: `snippets/crooks-schema-site.liquid` (Organization / Brand / WebSite).
1. `alternateName` → `["Crooks LDN", "Crooks London", "Crooks"]` on Organization, Brand and WebSite.
2. Add to Organization:
   ```json
   "founder": { "@type": "Person", "name": "George Hinxman" },
   "identifier": { "@type": "PropertyValue", "propertyID": "Companies House", "value": "16606021" },
   "address": { "@type": "PostalAddress", "addressCountry": "GB" }
   ```
   No `foundingDate`, `foundingLocation` or street address until evidenced/approved. MRCROOKS stays off the schema (answer 12).
3. `description` needs no code change once `shop.description` is set (section 1).
4. `sameAs` unchanged (Instagram, TikTok via footer). Add others only after the owner confirms them (section 4).

New on /pages/about only (a section or `templates/page.about.json` with a JSON-LD block):
```json
{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "@id": "https://crooksldn.com/pages/about#webpage",
  "url": "https://crooksldn.com/pages/about",
  "name": "About CROOKSLDN",
  "isPartOf": { "@id": "https://crooksldn.com#website" },
  "mainEntity": { "@id": "https://crooksldn.com#organization" }
}
```
(Build the URLs from `shop.url` as the existing snippet does.)

Validate: Rich Results Test / Schema Markup Validator on / and /pages/about; check Organization shows founder, identifier, alternateName.

## 4. Profiles: verified vs not

| Profile | Status |
|---|---|
| instagram.com/crooksldn | Linked from site footer: official |
| tiktok.com/@crooksldn | Linked from site footer: official |
| TikTok Shop | A "crooksldn joggers" TikTok Shop search page exists; seller not readable from here. Owner to confirm |
| YouTube, Pinterest, Depop | Nothing found |
| x.com/crooksuk ("C R O O K S") | Found in search; can't tell if it's yours. Owner to confirm or disown |
| crooksldn.uk (a WordPress-style "Home - Full Screen Slider" page) | Found in search; not readable from here. **Owner to confirm whether you own this domain.** If not, it is a lookalike of your brand name and worth knowing about |

## 5. Change-register entry (to be filed by the builder at implementation)
- Baseline: no About page; shop description blank; alternateName lacks "Crooks LDN"; no founder/identifier in schema; "Crooks London" searches surface Crooks & Castles.
- Target intent: Crooks LDN, Crooks London, Crooks LDN reviews, "what is CROOKSLDN", British streetwear brands.
- Expected result: /pages/about indexed; AI assistants describe CROOKSLDN as a British streetwear brand with the right product lines and founder; fewer Crooks & Castles confusions.
- Metrics: GEO rows Crooks LDN / Crooks London / Crooks LDN reviews (description accuracy, confusion); GSC impressions/clicks for /pages/about and brand queries.

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
