# Findings — International markets & local pricing

Pulled 18 Oct 2026 from Shopify (analytics, Markets, delivery profile, catalogue, orders, abandoned checkouts), the live storefront and CROOKS's Parcel2Go account. Shopify's order history starts inside the last 12 months, so lifetime = last 12 months. Revenue is net sales in GBP by shipping country. F1–F7 are the audit before any change; F8–F11 were added after George's answers.

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

## F2. Markets configuration before changes (audit, 18 Oct)

Changed since — see F11 and [CHANGES.md](CHANGES.md).

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
- No catalogs existed, so there were no fixed prices and no percentage adjustments anywhere.
- One domain (crooksldn.com); no market subfolders or domains.
- Duties: not collected (storefront reports `duties_collected: false`).
- Tax: Shopify records £0 tax on every order, UK included. George has confirmed CROOKS is VAT-registered — see F9.
- Payments: Shopify Payments (rounding only works with it). Plan: Grow. Shopify's theme docs say automatic country detection is Plus-only.

## F3. Why international prices look converted

1. Every price is GBP × live rate × 1.02 (Shopify adds its 2% conversion fee into the price), then rounded up by Shopify's fixed rule: USD, CAD, AUD to whole units; EUR to .95; JPY to ¥100; IDR to Rp1,000. Today £60 → $82, €72.95, A$118, C$116, ¥12,900, Rp1,471,000. Endings are tidy; the numbers aren't deliberate and drift (the July US order paid $82 for sweats, the September one $76).
2. Shopify's rounding can't be customised, so automatic conversion can never produce an $85 / €75 ladder.
3. Shipping was converted and rounded the same way: £18.99 → $26–27, ¥4,100–4,200, A$37–38; £12.99 → €15.95. **Fixed since 18 Oct (IMP-7): US and Eurozone shipping are now set in USD and EUR.**
4. **No country/currency selector, no auto-detection.** Shopify identified our test visitor as US (confidence 1.0, suggesting USD), yet the collection and product pages showed £60.00. Currency only changes at checkout: product £60 → cart £60 → checkout $82 + $26 shipping. That is the mismatch the brief rules out.
5. `?country=JP` and `?currency=USD` on storefront URLs changed nothing.
6. International visitors only see UK promises ("FREE UK SHIPPING OVER £30", "Free UK Tracked 24 included", "ships today") and nothing about international shipping or duties.

## F4. Storefront tests (18 Oct 2026, before changes)

Method: pages fetched from a US IP, confirmed as US by Shopify's `browsing_context_suggestions` endpoint. Checkout amounts come from real orders and abandoned checkouts — no addresses were typed into the live checkout. Post-change tests: [artifacts/tests/2026-10-18-tier1.md](artifacts/tests/2026-10-18-tier1.md).

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

## F5. Duties and taxes — what buyers face

**United States.** De minimis is suspended for every country (since 29 Aug 2025), so every US parcel is dutiable. Duty follows country of origin (China), not where it ships from. For China-origin goods today: MFN + Section 301 (7.5% on apparel) + the Section 301 forced-labour tariff at 12.5% (from 24 Jul 2026). IEEPA tariffs ended 24 Feb 2026; the Section 122 surcharge expired 24 Jul 2026. Estimate: ~36% on fleece, denim and tees; ~48% on the HydroCuff (synthetic outerwear). An $85 hoodie carries about $31.

- Royal Mail International Tracked to the US is a Postal Delivery Duties Paid service: Royal Mail pays US duty and invoices the sender (+50p handling per item). Parcel2Go sells it as duty pre-paid by the sender (F8). Until duty is collected at checkout, CROOKS pays ~36% of the item value out of margin on those parcels: ~£23 on an $85 hoodie, ~£44 on a $160 Convict Set.
- George approved collecting US duty at checkout (18 Oct). Shopify only switches it on in admin with George's "Agree and activate".
- Tees on Gildan blanks (Honduras, Nicaragua or Bangladesh, not China) carry MFN only (~16.5%), not the China surcharges.

**EU.** No VAT is collected at checkout (no IOSS), so EU buyers pay import VAT (19–27%), a flat €3 customs duty per item line under €150 (since 1 Jul 2026) and a carrier handling fee on delivery. France has added a small-parcel tax since 1 Mar 2026. Two of the nine EU orders were refunded (DK, NL); cause not recorded.

**Australia.** Orders under A$1,000 from an unregistered overseas seller normally arrive with nothing to pay; CROOKS is far below Australia's A$75k GST registration threshold.

**Japan, Canada, Indonesia.** Nothing collected at checkout; any charges fall on the buyer at delivery.

**Product customs data — updated 18 Oct 19:20 BST (45 active products):**

| Products | HS code | Origin |
|---|---|---|
| Black, Grey, Pink Convict Hoodie; Charcoal Cellblock Crewneck | 6110.20 (existing) | CN |
| Black, Grey Convict Sweats; Pink CRSDR Joggers; Charcoal Cellblock Shorts | 6103.42 | CN |
| Cellblock, Grey, Pink, Black Sets | 6103.22 (knitted cotton ensembles) | CN |
| OG, Grey Wash and Blue Wash Yard Jeans; Blue and Grey Wash Yard Jorts | 6203.42 | CN |
| HydroCuff Windbreaker; Double-Agent Puffa | 6201.40 (HydroCuff corrected from HS 2017 620193) | CN |
| Major League caps (Cream, Blue, Brown) | 6505.00 | CN |
| MotionTec socks (both) | 6115.95 | CN |
| 21 tees | 6109.10 — **not written yet** | Gildan blank — **label country needed** |

- Assumptions to confirm: Puffa shell and fill synthetic; socks majority cotton.
- Tees are printed in-house (George, Q10) on Gildan blanks. Customs origin is where the blank was sewn, not where it was printed, so it isn't GB. Gildan sews in Honduras, Nicaragua and Bangladesh.
- Weight 0 on 31 products (20 of the 21 tees, the four sets, three caps, the Puffa, both Yard Jorts, White/Red socks). Shipping now bands by order value, so this only matters for Swiss duties or a later move to weight bands.

## F6. Shipping configuration and cost (before changes)

One General profile, shipping from GB:

| Zone | Countries | Rates |
|---|---|---|
| United Kingdom | GB | Tracked 48 £3.00, free from £30; Tracked 24 £4.99, free from £80 |
| Channel Islands | GG, JE | Tracked 48 £3.99; Tracked 24 £7.00; no free threshold |
| "EU (European Union)" | EU 27 plus NO, CH, IS, UA, RU, BY, the Balkans, IM, GI, MC, AD… (50) | Standard international £12.99 flat |
| International | everything else incl. US, CA, AU, NZ, JP, ID (164) | Standard international £18.99 flat |

Replaced on 18 Oct — see F11. The first cost check used Royal Mail's published online prices; F8 replaces it with CROOKS's own Parcel2Go rates.

## F7. Passed to other workstreams (not acted on)

- **live-site-checks:** the product page says "Free UK Tracked 24 included" on a £60 item; checkout only makes Tracked 24 free from £80.
- **product-data / T-shirt week:** all tees are now £20, and 21 tees are active. The price lists cover £20 and £25.
- **CLIVE:** CLIVE Shipping takes Channel Islands orders as international (F10).

## F8. Real carrier costs (CROOKS's Parcel2Go account)

Parcel2Go quotes in George's account, 18 Oct 2026, ex VAT, drop-off. 1kg parcel = 35×25×8 cm; 2kg = 40×30×12 cm. Easyship (the other half of CROOKS Shipping) needs a login I can't enter, so its rates aren't here; if Easyship is cheaper on a lane, these margins are conservative.

| Destination | Service costed | ≤1kg | ≤2kg | Other services seen |
|---|---|---:|---:|---|
| United States | Royal Mail International Tracked (duty pre-paid by sender) | £17.53 | £20.20 | Evri £19.09 (1kg) |
| Germany | Royal Mail International Tracked | £11.10 | £11.10 | Evri £8.79 / £8.89; DPD Drop Off Europe DDP £9.37 |
| Italy | Royal Mail International Tracked | £13.05 | £14.15 | Evri £11.39 / £12.39 |
| France | Royal Mail International Tracked | £12.30 | not quoted | Evri £9.59; DPD DDP £9.98 |
| Japan | Royal Mail International Tracked | £21.45 | £29.10 | — |
| Australia | Royal Mail International Tracked | £19.40 | £25.10 | — |
| Canada | Royal Mail International Tracked | £20.27 | £24.52 | Evri £24.49 (2kg) |
| Guernsey | Parcelforce Channel Islands (Parcel2Go has no Royal Mail service to GG) | £12.96 | — | see F10 |

What CROOKS kept per parcel before 18 Oct (charge less 2% conversion and 2.7% international card fee):

| Lane | Charge | Net | ≤1kg | ≤2kg |
|---|---:|---:|---:|---:|
| US | $26 | £18.57 | +£1.04 | −£1.63 |
| Germany | €15.95 | £12.82 | +£1.72 | +£1.72 |
| Italy | €15.95 | £12.82 | −£0.23 | −£1.33 |
| France | €15.95 | £12.82 | +£0.52 | — |
| Japan | £18.99 (¥4,100) | £18.46 | −£2.99 | −£10.64 |
| Australia | £18.99 (A$38) | £18.46 | −£0.94 | −£6.64 |
| Canada | £18.99 (C$37) | £18.46 | −£1.81 | −£6.06 |

Rates live since 18 Oct (IMP-7), banded by order value because 31 of 45 products have no weight:

| Lane | Rate | ≤1kg result | ≤2kg result |
|---|---|---:|---:|
| US (fixed USD zone) | $25 under $100 / $30 from $100 | +£0.33 | +£1.23 |
| Eurozone (fixed EUR zone) | €15 under €90 / €18 from €90 | DE +£0.95, FR −£0.25, IT −£1.00 | DE +£3.36, IT +£0.31 |
| Japan, Canada, rest of world | £22.99 under £75 / £30.99 from £75 | JP +£0.90, CA +£2.08 | JP +£1.02, CA +£5.60 |
| Australia / New Zealand | £20.99 under £75 / £26.99 from £75 | +£1.00 | +£1.14 |
| Rest of Europe | £12.99 unchanged | no quotes yet | |

- The thresholds stand in for weight: one fleece piece or pair of jeans (0.65–0.9kg) stays under; a set or two pieces goes over.
- Orders over 2kg (three or more fleece pieces) have no quote and may lose money in the top band.
- US duty sits on top of the US shipping cost whenever Royal Mail pre-pays it (F5).

## F9. VAT — CROOKS is VAT-registered (George, Q9)

- UK prices include 20% VAT. A £60 hoodie sold in the UK nets £48.73 after VAT and the UK card fee.
- Goods sent outside the UK are zero-rated exports, given proof of export (tracking). So international sales keep the VAT-equivalent: $85 nets £60.47 (+24% on the UK sale); €75 nets £60.02 (+23%). Across the ladder the approved lists sit +18% to +33% above UK ex-VAT net. The Channel Islands are outside the UK VAT area too, so a £60 Guernsey order would net £58.73 if treated as an export.
- Yet Shopify records £0 tax on every order, UK included — UK VAT isn't set up in Shopify's tax settings. **For the accountant (nothing changed):**
  1. How UK VAT is calculated today, given Shopify reports none.
  2. Whether international and Channel Islands orders are treated as zero-rated exports. If all Shopify sales are treated as VAT-inclusive UK sales, VAT is being overpaid on them.
  3. Whether to set up UK VAT in Shopify so reports and invoices show it.
- EU: still no IOSS, so EU buyers pay import VAT, the €3 duty and handling on delivery (F5).

## F10. Channel Islands routing

- CLIVE Shipping (George's international shipping service, the CROOKS Operations app) quoted Guernsey order CROOKS-2202 as Parcelforce £16.71. Parcel2Go only offers Parcelforce to Guernsey (£12.96).
- The CLIVE repo's client describes the service as holding "international orders only", so GG/JE orders are being picked up as international. The service code itself isn't in GitHub.
- Earlier Channel Islands orders shipped Royal Mail Tracked 48 (VU…GB tracking numbers), priced as UK inland.
- Free Tracked 48 from £30 (live, IMP-4) only pays on Royal Mail. On Parcelforce at £16.71, each free order costs ~£17 — roughly £1,000 a year at last year's 63 Channel Islands orders, against ~£250 a year on Royal Mail.
- George confirmed Royal Mail Tracked 48 for the Channel Islands (Q14). Fix: the service treats GG, JE and IM as domestic.

## F11. Markets and shipping zones now (18 Oct 2026, 19:30 BST)

| Market | Countries | Base currency | Catalog | Shipping zone |
|---|---|---|---|---|
| UK | GB | GBP | none | United Kingdom (unchanged) |
| Channel Island | GG, JE | GBP | none | Channel Islands: Tracked 48 £3.99 / free from £30; Tracked 24 £7 |
| United States | US | USD | "United States — USD fixed prices" — DRAFT, prices not loaded | United States: $25 / $30 from $100 |
| Eurozone | 21 euro states + MC, AD, SM, VA, ME, XK | EUR | "Eurozone — EUR fixed prices" — DRAFT, prices not loaded | Eurozone: €15 / €18 from €90 |
| European Union (non-euro) | CZ, DK, HU, PL, RO, SE | GBP (local currencies) | none | Rest of Europe £12.99 |
| Canada | CA | GBP (local currency) | none | Rest of world £22.99 / £30.99 from £75 |
| Australia and New Zealand | AU, NZ | GBP (local currencies) | none | Australia and New Zealand £20.99 / £26.99 from £75 |
| all world | rest of world | GBP (local currencies) | none | Rest of world, or Rest of Europe for NO, CH, IS, IM, GI, the Balkans etc. |
| United Kingdom | GB | — | — | draft duplicate, left alone |

No market overlaps another. Product prices are still Shopify's automatic conversion everywhere ([tests](artifacts/tests/2026-10-18-tier1.md)) until the fixed prices load.
