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

- Royal Mail International Tracked to the US is a Postal Delivery Duties Paid service: Royal Mail pays US duty and invoices the sender (+50p handling per item). Parcel2Go sells it as duty pre-paid by the sender (F8). If US orders go this way, CROOKS pays ~36% of the item value out of margin: ~£23 on an $85 hoodie, ~£44 on a $160 Convict Set.
- The September US order went FedEx; courier imports are normally billed to the buyer on delivery plus a brokerage fee.

**EU.** No VAT is collected at checkout (no IOSS), so EU buyers pay import VAT (19–27%), a flat €3 customs duty per item line under €150 (since 1 Jul 2026) and a carrier handling fee on delivery. France has added a small-parcel tax since 1 Mar 2026. Two of the nine EU orders were refunded (DK, NL); cause not recorded.

**Australia.** Orders under A$1,000 from an unregistered overseas seller normally arrive with nothing to pay; CROOKS is far below Australia's A$75k GST registration threshold.

**Japan, Canada, Indonesia.** Nothing collected at checkout; any charges fall on the buyer at delivery.

**Product customs data — refreshed 18 Oct 18:45 BST (45 active products, first variant of each):**

- HS code on 8 of 45: Black, Grey and Pink Convict Hoodie (61102091), Black Convict Sweats (6103420000), Grey Convict Sweats (610342), Charcoal Cellblock Crewneck (6110209900), Grey Wash Yard Jeans (62034231), HydroCuff (620193). Missing on the other 37, including all four sets, all 21 tees, all three caps, the Puffa and both socks.
- HydroCuff's 620193 is an HS 2017 code; HS 2022 moved anoraks and windcheaters to 6201.40.
- Origin CN on 22; missing on 23: all 21 tees and the Blue and Brown Major League caps (activated after origin was set on the other products).
- Tees are printed in-house (George, Q10), but customs origin is where the blank garment was made, not where it was printed, so it isn't GB. Left blank until the blank's origin is known (Q15).
- Weight 0 on 31: 20 of the 21 tees (only Crooks Express has 250g), the Black, Grey, Pink and Cellblock Sets, all three caps, the Double-Agent Puffa, both Yard Jorts, White/Red socks. Weight-based shipping and duty calculation both need these.

## F6. Shipping configuration and cost

One General profile, shipping from GB:

| Zone | Countries | Rates |
|---|---|---|
| United Kingdom | GB | Tracked 48 £3.00, free from £30; Tracked 24 £4.99, free from £80 |
| Channel Islands | GG, JE | Tracked 48 £3.99; Tracked 24 £7.00; no free threshold — **changed 18 Oct: Tracked 48 free from £30 (IMP-4)** |
| "EU (European Union)" | EU 27 plus NO, CH, IS, UA, RU, BY, the Balkans, IM, GI, MC, AD… | Standard international £12.99 flat |
| International | everything else, incl. US, CA, AU, NZ, JP, ID | Standard international £18.99 flat |

No international free-shipping threshold. Overseas parcels have gone Royal Mail, UPS and FedEx.

The first cost check used Royal Mail's published online prices; **F8 replaces it with CROOKS's own Parcel2Go rates.** Royal Mail prices the Channel Islands and Isle of Man as UK inland, but the Isle of Man sits in the £12.99 Europe zone.

## F7. Passed to other workstreams (not acted on)

- **live-site-checks:** the product page says "Free UK Tracked 24 included" on a £60 item; checkout only makes Tracked 24 free from £80.
- **product-data / T-shirt week:** all tees are now £20, and 21 tees are active (F5 counts). The price lists cover £20 and £25.

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

What CROOKS keeps per parcel today (charge less 2% conversion and 2.7% international card fee) against those costs:

| Lane | Charge now | Net | ≤1kg | ≤2kg |
|---|---:|---:|---:|---:|
| US | $26 | £18.57 | +£1.04 | −£1.63 |
| Germany | €15.95 | £12.82 | +£1.72 | +£1.72 |
| Italy | €15.95 | £12.82 | −£0.23 | −£1.33 |
| France | €15.95 | £12.82 | +£0.52 | — |
| Japan | £18.99 (¥4,100) | £18.46 | −£2.99 | −£10.64 |
| Australia | £18.99 (A$38) | £18.46 | −£0.94 | −£6.64 |
| Canada | £18.99 (C$37) | £18.46 | −£1.81 | −£6.06 |

Proposed rates (Q13), banded by order value because 31 of 45 products have no weight:

| Lane | Rate | ≤1kg result | ≤2kg result |
|---|---|---:|---:|
| US (fixed USD zone) | $25 under $100 / $30 from $100 | +£0.33 | +£1.23 |
| Eurozone (fixed EUR zone) | €15 under €90 / €18 from €90 | DE +£0.95, FR −£0.25, IT −£1.00 | DE +£3.36, IT +£0.31 |
| Japan, Canada, rest of world | £22.99 under £75 / £30.99 from £75 | JP +£0.90, CA +£2.08 | JP +£1.02, CA +£5.60 |
| Australia / New Zealand | £20.99 under £75 / £26.99 from £75 | +£1.00 | +£1.14 |
| Rest of Europe | £12.99 unchanged | no quotes yet | |

- The thresholds stand in for weight: one fleece piece or pair of jeans (0.65–0.9kg) stays under; a set or two pieces goes over.
- Orders over 2kg (three or more fleece pieces) have no quote and may lose money in the top band.
- US duty sits on top of the US shipping cost whenever Royal Mail pre-pays it (F5, Q3b).

## F9. VAT — CROOKS is VAT-registered (George, Q9)

- UK prices include 20% VAT. A £60 hoodie sold in the UK nets £48.73 after VAT and the UK card fee.
- Goods sent outside the UK are zero-rated exports, given proof of export (tracking). So international sales keep the VAT-equivalent: $85 nets £60.47 (+24% on the UK sale); €75 nets £60.02 (+23%). Across the ladder the approved lists sit +18% to +33% above UK ex-VAT net. The Channel Islands are outside the UK VAT area too, so a £60 Guernsey order would net £58.73 if treated as an export.
- Yet Shopify records £0 tax on every order, UK included — UK VAT isn't set up in Shopify's tax settings. **For the accountant (nothing changed):**
  1. How UK VAT is calculated today, given Shopify reports none.
  2. Whether international and Channel Islands orders are treated as zero-rated exports. If all Shopify sales are treated as VAT-inclusive UK sales, VAT is being overpaid on them.
  3. Whether to set up UK VAT in Shopify so reports and invoices show it.
- EU: still no IOSS, so EU buyers pay import VAT, the €3 duty and handling on delivery (F5).

## F10. Channel Islands routing

- CROOKS Shipping (CROOKS Operations app) quoted Guernsey order CROOKS-2202 as Parcelforce £16.71. Parcel2Go only offers Parcelforce to Guernsey (£12.96).
- Earlier Channel Islands orders shipped Royal Mail Tracked 48 (VU…GB tracking numbers), which Royal Mail prices as UK inland.
- Free Tracked 48 from £30 (live, IMP-4) only pays on Royal Mail. On Parcelforce at £16.71, each free order costs ~£17 — roughly £1,000 a year at last year's 63 Channel Islands orders, against ~£250 a year on Royal Mail (lost £3.99 charges).

## F11. Markets after the changes (18 Oct 2026, 18:45 BST)

| Market | Status | Countries | Base currency | Local currencies | Catalog |
|---|---|---|---|---|---|
| UK | Active | GB | GBP | Off | none |
| Channel Island | Active | GG, JE | GBP | Off | none |
| United States (new) | Active | US | USD | On | "United States — USD fixed prices": DRAFT, 0 fixed prices |
| Canada (was United States and Canada) | Active | CA | GBP | On | none |
| European Union | Active | 27 EU states | GBP | On | none |
| Australia and New Zealand | Active | AU, NZ | GBP | On | none |
| all world | Active | rest of world only | GBP | On | none |
| United Kingdom | Draft | GB | — | — | duplicate, left alone |

contextualPricing check after the changes (BLACK CONVICT SWEATS, XS, £60): US $82, CA C$116, DE €72.95, BG €72.95, HR €72.95, PL 318 zł, DK 543 kr, SE 809 kr, JP ¥12,900, AU A$118, GG £60, GB £60, IM £60, NO £60. Identical to the audit: the restructure moved no price.
