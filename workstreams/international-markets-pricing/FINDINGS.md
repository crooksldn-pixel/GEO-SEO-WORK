# Findings — International markets & local pricing

Pulled 18 Oct 2026 from Shopify (analytics, Markets, delivery profile, catalogue, orders, abandoned checkouts) and the live storefront. Shopify's order history starts inside the last 12 months, so lifetime = last 12 months. Revenue is net sales in GBP by shipping country.

## F1. Where CROOKS actually sells

| Country | Orders | Net revenue | AOV | Sessions (12m) | Checkout starts → completed | Session conv. | Currency now | Market now | Priority |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| United Kingdom | 1,127 | £53,160 | £47 | 36,239 | 1,476 → 759 (51%) | 2.09% | GBP | UK | Home |
| Guernsey | 54 | £3,338 | £62 | 1,969 | 121 → 47 (39%) | 2.39% | GBP | Channel Island | Tier 1 (GBP) |
| Jersey | 9 | £362 | £40 | 468 | 25 → 10 | 2.14% | GBP | Channel Island | Tier 1 (GBP) |
| United States | 2 shipped to US (+5 US-billed, UK-delivered) | £214 | £107 | 3,865 (2,497 in last 90 days) | 117 → 12 (10%) | 0.31% | USD | United States and Canada | Tier 1 |
| EU (IT 2, PL 2, BE 1, DE 1; DK 2 and NL 1 refunded) | 9 | £347 | £58 | ~3,550 (FR 645, NL 422, DE 347, IT 334, ES 328, PL 280…) | ~152 → 21 (14%) | ~0.6% | EUR (PLN, DKK…) | European Union | Tier 1 (EUR) |
| Australia | 2 | £185 | £92 | 2,691 (278 in last 90 days) | 31 → 2 (6%) | 0.07% | AUD | Australia and New Zealand | Tier 2 |
| Japan | 1 | £131 | £131 | 242 | 13 → 2 | 0.83% | JPY | all world | Tier 2 |
| Canada | 0 | £0 | — | 212 | 3 → 0 | 0% | CAD | United States and Canada | Tier 2 (auto) |
| Indonesia | 0 | £0 | — | 23 | no add-to-cart | 0% | IDR | all world | Tier 3 |
| Everything else | 0 | — | — | under 200 each | — | — | various | all world | Tier 3 |

- Overseas (outside the UK and Crown Dependencies): 14 orders, £877 net = 1.5% of £57.7k. Channel Islands: 63 orders, £3,700 = 6.4%.
- The signal is the checkout drop-off: UK 51%, Guernsey 39%, EU ~14%, US 10%, Australia 6%. Session country is IP location and the samples are small.
- US traffic is growing: 108 of its 117 checkout starts were in the last 90 days, yet only 2 orders have shipped to the US.
- Abandoned checkouts with an address since 20 Jul: Slovakia ×2, Germany ×2, Australia ×2 — e.g. a €27.86 tee + €15.95 shipping = €43.81; an A$98 crewneck + A$37 shipping. No US abandoned checkout had an address, so US buyers leave before entering one.
- Channel Islands: 7 abandoned checkouts since 12 Sep, each carrying the £3.99/£7 shipping UK customers don't pay over £30.

## F2. Current Markets configuration (read-only)

| Market | Status | Countries | Currency | Local currencies | Rounding | Catalog / fixed prices / adjustment | Duties / tax inclusion |
|---|---|---|---|---|---|---|---|
| all world | Active | 230+ regions — includes GB, GG, JE, US, CA, AU, NZ and every EU state, so it overlaps every other market | Local where supported; ~45 countries fall back to GBP (e.g. Norway, Türkiye, Brazil, Mexico, South Africa, Gulf states) | On | On | None | Not set |
| European Union | Active | 27 EU states | EUR, PLN, DKK, SEK, CZK, HUF, RON | On | On | None | Not set |
| United States and Canada | Active | US, CA | USD, CAD | On | On | None | Not set |
| Australia and New Zealand | Active | AU, NZ | AUD, NZD | On | On | None | Not set |
| Channel Island | Active | GG, JE | GBP | Off | On | None | Not set |
| UK | Active | GB | GBP | Off | On | None | Not set |
| United Kingdom | Draft | GB | — | — | — | — | Duplicate of UK |

- Exchange rates: automatic everywhere. Manual rates need Managed Markets.
- No catalogs exist, so there are no fixed prices and no percentage adjustments anywhere.
- One domain (crooksldn.com); no market subfolders or domains.
- Duties: not collected (storefront reports `duties_collected: false`).
- Tax: no tax collected on any order, UK included. Looks like CROOKS isn't VAT-registered (Q9).
- Payments: Shopify Payments (rounding only works with it). Plan: Grow. Shopify's help lists no plan restriction on catalogs or duty collection; Shopify's theme docs say automatic country detection is Plus-only.

## F3. Why international prices look converted

1. Every price is GBP × live rate × 1.02 (Shopify adds its 2% conversion fee into the price), then rounded up by Shopify's fixed rule: USD, CAD, AUD to whole units; EUR to .95; JPY to ¥100; IDR to Rp1,000. Today £60 → $82, €72.95, A$118, C$116, ¥12,900, Rp1,471,000. Endings are tidy; the numbers aren't deliberate and drift (the July US order paid $82 for sweats, the September one $76).
2. Shopify's rounding can't be customised, so automatic conversion can never produce an $85 / €75 ladder.
3. Shipping is converted and rounded the same way: £18.99 → $26–27, ¥4,100–4,200, A$37–38; £12.99 → €15.95. The unrounded "$14.68" from the brief isn't happening now.
4. **No country/currency selector, no auto-detection.** Shopify identified our test visitor as US (confidence 1.0, suggesting USD), yet the collection and product pages showed £60.00. Currency only changes at checkout: product £60 → cart £60 → checkout $82 + $26 shipping. That is the mismatch the brief rules out.
5. `?country=JP` and `?currency=USD` on storefront URLs changed nothing.
6. International visitors only see UK promises ("FREE UK SHIPPING OVER £30", "Free UK Tracked 24 included", "ships today") and nothing about international shipping or duties.

## F4. Storefront tests (18 Oct 2026)

Method: pages fetched from a US IP, confirmed as US by Shopify's `browsing_context_suggestions` endpoint. Checkout amounts come from real orders and abandoned checkouts — no addresses were typed into the live checkout. Japan and Indonesia can't be simulated by IP from here; with no selector they go through the same £ code path.

| Step | UK | US | Japan | Indonesia |
|---|---|---|---|---|
| Collection / homepage | £ ✓ | £ ✗ (should be $) | £ ✗ | £ ✗ |
| Product page | £60.00 ✓ | £60.00 ✗ | £60.00 ✗ (`?country=JP` tested) | £ ✗ |
| Cart | £ | £ | £ | £ |
| Checkout | £ | $ ($82 sweats on orders) | ¥ (order paid ¥) | Rp (no orders) |
| Shipping | £3 / free ≥ £30 | $26 | ¥4,100 | Rp466,000 |
| Tax | none | none | none | none |
| Duties | n/a | not collected | not collected | not collected |
| Country selector | none | none | none | none |

## F5. Duties and taxes — what buyers face now

**United States.** De minimis is suspended for every country (since 29 Aug 2025), so every US parcel is dutiable. Duty follows country of origin (China), not where it ships from. For China-origin goods today: MFN + Section 301 (7.5% on apparel) + the Section 301 forced-labour tariff at 12.5% (from 24 Jul 2026). IEEPA tariffs ended 24 Feb 2026; the Section 122 surcharge expired 24 Jul 2026. Estimate: ~36% on fleece, denim and tees; ~48% on the HydroCuff (synthetic outerwear). An $85 hoodie carries about $31.

- Royal Mail International Tracked to the US is a Postal Delivery Duties Paid service: Royal Mail pays US duty and invoices the sender (+50p handling per item). If US orders go Royal Mail, CROOKS is already paying ~36% of the item value out of margin.
- The September US order went FedEx; courier imports are normally billed to the buyer on delivery plus a brokerage fee.
- Which of these applies is Q4.

**EU.** No VAT is collected at checkout (no IOSS), so EU buyers pay import VAT (19–27%), a flat €3 customs duty per item line under €150 (since 1 Jul 2026) and a carrier handling fee on delivery. France has added a small-parcel tax since 1 Mar 2026. Two of the nine EU orders were refunded (DK, NL); cause not recorded.

**Australia.** Orders under A$1,000 from an unregistered overseas seller normally arrive with nothing to pay; CROOKS is far below Australia's A$75k GST registration threshold.

**Japan, Canada, Indonesia.** Nothing collected at checkout; any charges fall on the buyer at delivery.

**Product customs data (25 live products):**

- HS codes on 8: Black, Grey and Pink Convict Hoodie (61102091), Black Convict Sweats (6103420000), Grey Convict Sweats (610342), Charcoal Cellblock Crewneck (6110209900), Grey Wash Yard Jeans (62034231), HydroCuff (620193).
- Missing on 17: Black, Grey and Pink Set, Cellblock Set, Pink Convict Sweats, Charcoal Cellblock Shorts, Blue Wash Yard Jeans, OG Jeans, Blue and Grey Wash Yard Jorts, Double-Agent Puffa, the three live tees, Major League Cap (Cream), both MotionTec socks.
- HydroCuff's 620193 is an HS 2017 code; HS 2022 moved anoraks and windcheaters to 6201.40.
- Country of origin CN on 22 of 25. The three live tees have none — they're print on demand, so the blank's origin needs confirming (Q10).
- Weight 0 on 11: Black, Grey and Pink Set, Cellblock Set, both Yard Jorts, Double-Agent Puffa, Major League Cap (Cream), White/Red socks, CRX GARMS, CRXST★RZ. Weight-based shipping and duty calculation both need these.

## F6. Shipping configuration and cost

One General profile, shipping from GB:

| Zone | Countries | Rates |
|---|---|---|
| United Kingdom | GB | Tracked 48 £3.00, free from £30; Tracked 24 £4.99, free from £80 |
| Channel Islands | GG, JE | Tracked 48 £3.99; Tracked 24 £7.00; no free threshold |
| "EU (European Union)" | EU 27 plus NO, CH, IS, UA, RU, BY, the Balkans, IM, GI, MC, AD… | Standard international £12.99 flat |
| International | everything else, incl. US, CA, AU, NZ, JP, ID | Standard international £18.99 flat |

No international free-shipping threshold. Overseas parcels have gone Royal Mail, UPS and FedEx.

Result per parcel against Royal Mail's published online International Tracked prices (Oct 2026). "Net" is what CROOKS keeps after the 2% conversion and 2.7% international card fee:

| Destination | Royal Mail ≤1kg | Royal Mail ≤2kg | CROOKS charges | Net result ≤1kg | Net result ≤2kg |
|---|---:|---:|---:|---:|---:|
| US | £17.53 + £0.50 handling | £20.20 + £0.50 | $26 | +£0.54 | −£2.13 (before any US duty invoiced) |
| Europe Zone 1 / Zone 2 | £15.15 / £16.35 | £16.35 / £18.45 | €15.95 | −£2.33 / −£3.53 | −£3.53 / −£5.63 |
| World Zone 1 (JP, CA, ID…) | £24.65 | £29.90 | ¥4,100 | −£6.09 | −£11.34 |
| World Zone 2 (AU) | £27.90 | £37.55 | A$38 | −£9.06 | −£18.71 |

These are Royal Mail's public online prices, not CROOKS's account rates (Q4). A single fleece piece is 0.8–0.9kg (≤1kg band); a Convict Set is two of those (2kg band). Royal Mail prices the Channel Islands and Isle of Man as UK inland, but the Isle of Man sits in the £12.99 Europe zone.

## F7. Passed to other workstreams (not acted on)

- **live-site-checks:** the product page says "Free UK Tracked 24 included" on a £60 item; checkout only makes Tracked 24 free from £80.
- **product-data / T-shirt week:** CROOKS EXPRESS T-SHIRT and CRX GARMS T-SHIRT moved to £20 with 30 variants at 17:42–17:44 BST during this audit; CRXST★RZ is still £25. The matrix covers both price points.
