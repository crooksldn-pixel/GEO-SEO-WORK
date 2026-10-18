# Proposal — CROOKSLDN international markets and local pricing

18 Oct 2026. Nothing below is live. Decisions are in [../QUESTIONS.md](../QUESTIONS.md).

## Fix first: let international visitors see their own currency

Every international visitor browses in £ and only meets their currency at checkout, together with shipping (and for the US, duties on delivery). Checkout completion: UK 51%, EU ~14%, US 10%. Turn on Horizon's country/region selector in header and footer. The Grow plan has no automatic market detection; a geolocation popup app is optional.

## Recommended CROOKSLDN Markets

### Tier 1

- **United States** — biggest non-UK audience and rising (2,497 sessions, 108 checkout starts in 90 days), 10% checkout completion. Own single-country market, fixed USD price list, fixed USD shipping, duties collected at checkout (Q3).
- **Eurozone** — most overseas orders (6 paid of 9), ~3,000 sessions, ~14% checkout completion. Fixed EUR price list on the existing European Union market (non-euro states see it converted to their currency), fixed EUR shipping in a Eurozone-only zone.
- **Channel Islands** — second-biggest market (63 orders, £3,700, UK-like conversion). Already GBP; shipping parity with UK (Q6).

### Tier 2 — automatic FX + Shopify rounding, no adjustment

Australia & New Zealand, Japan, Canada, non-euro EU (PL, DK, SE, CZ, HU, RO).

- No adjustment because auto prices already include Shopify's 2% fee; the remaining gap (~1% international card surcharge) is worth about £3 a year at current volume.
- Japan stays automatic: one order in 12 months, and Shopify's ¥100 rounding already lands on Japanese-style prices (¥12,900). Move it to a fixed JPY list when it passes ~5 orders a quarter.

### Tier 3 — automatic, unchanged

Everything else, Indonesia included (23 sessions, no add-to-cart, no orders in 12 months). Shopify already rounds IDR to Rp1,000.

## Recommended price matrix

Rule: GBP × mid-market rate × 1.03 (Shopify's 2% conversion fee plus ~1% international card premium), then the next deliberate point up. Points: $/€5 steps from 30 to 100, $/€10 steps above (plus 175 and 195); under 30 the low-ticket points 9, 12, 15, 18, 20, 22, 25, 28. One exception: if the next point up lifts net more than 10% above UK and the point below is within 3%, take the point below and flag it.

| Product | GBP | US now | US proposed | EU now | EU proposed | Japan now → stays auto | Australia now → stays auto |
|---|---:|---:|---:|---:|---:|---:|---:|
| MotionTec socks, 1 pair | £6 | $9 | **$9** | €7.95 | **€8** | ¥1,300 | A$12 |
| MotionTec socks, 3 pack | £15 | $21 | **$22** | €18.95 | **€20** | ¥3,300 | A$30 |
| Tee: Crooks Express, CRX GARMS | £20 | $28 | **$28** | €24.95 | **€25** | ¥4,300 | A$40 |
| Tee: CRXST★RZ; socks 6 pack | £25 | $34 | **$35** | €30.95 | **€30** ⚑ | ¥5,400 | A$49 |
| Major League Cap (Cream) | £32 | $44 | **$45** | €38.95 | **€40** | ¥6,900 | A$63 |
| Cellblock Shorts; socks 12 pack | £45 | $62 | **$65** | €54.95 | **€55** | ¥9,700 | A$89 |
| Cellblock Crewneck; Yard Jorts | £50 | $68 | **$70** | €60.95 | **€65** | ¥10,800 | A$98 |
| Convict Hoodie, Convict Sweats, Yard and OG Jeans | £60 | $82 | **$85** | €72.95 | **€75** | ¥12,900 | A$118 |
| Cellblock Set; HydroCuff Windbreaker | £85 | $116 | **$120** | €102.95 | **€110** | ¥18,300 | A$167 |
| Convict Set (black, grey, pink) | £110 | $150 | **$160** | €133.95 | **€140** | ¥23,700 | A$216 |
| Double-Agent Puffa | £140 | $191 | **$195** | €169.95 | **€175** | ¥30,100 | A$275 |

"Now" is Shopify's live converted price on 18 Oct; automatic prices keep moving with FX. ⚑ €30 sits 1.9% below UK net; €35 would be 14.6% above.

- **Net vs UK per unit** (after FX, 2% conversion, 2.7% international card; UK at 1.7% + 25p): USD +1.2% to +9.4%; EUR −1.9% to +9.4%. Socks carry the biggest % uplift because of the fixed 25p card fee. Full workings: [price-matrix.md](price-matrix.md).
- **Ladder holds:** hoodie + sweats $170 vs Convict Set $160 (UK £120 vs £110); €150 vs €140. Cellblock Crewneck + Shorts $135 vs Cellblock Set $120; €120 vs €110. Tees keep two tiers: $28/$35, €25/€30.
- **US duty on top (Q3, option A):** an $85 hoodie ≈ $31 at checkout (~36%; HydroCuff ~48%). Including duty in the price instead would need a ~$140 hoodie to match UK net.
- **EU VAT:** these EUR prices assume the buyer pays VAT at import, as now. If VAT is ever collected at checkout and shown inclusive (Q8), the EUR list needs rebuilding about 20% higher.
- Fixed lists don't follow FX: re-check quarterly or after a ~5% move from 1.334 (USD) / 1.186 (EUR).

## Recommended shipping matrix

Weight bands need product weights fixed first (11 live products are at 0g, including every Set). Cost basis is Royal Mail's published online price, October 2026 — not CROOKS's account rate (Q4).

| Market | Current | Proposed | Net vs Royal Mail cost | Why |
|---|---:|---:|---:|---|
| United States (own zone, fixed USD) | $26 flat | $25 up to 1kg · $30 up to 2kg · $50 above | −£0.17 · +£0.73 · +£2.80 | Clean, at cost; single items cheaper than now |
| Eurozone (own zone, fixed EUR) | €15.95 flat | €20 up to 1kg · €25 above | −£0.28 to +£0.92 · +£1.64 to +£3.74 | Ends a £2.33–£5.63 loss per parcel |
| Rest of Europe (GBP, auto-converted) | £12.99 | £16.99 · £18.99 | about break-even | Same Royal Mail cost band |
| World Zone 1 — Japan, Canada, Indonesia, rest of world | £18.99 (¥4,100, C$37) | £25.99 · £31.99 (¥5,600 · ¥6,900; C$50 · C$62) | +£0.70 · +£1.34 | Ends a £6–£11 loss per parcel |
| World Zone 2 — Australia & NZ | £18.99 (A$38) | £29.99 · £39.99 (A$59 · A$79) | +£1.35 · +£1.62 | Ends a £9–£19 loss per parcel |
| Channel Islands | £3.99 T48 / £7 T24, no free threshold | Tracked 48 free from £30, as UK | inland cost, as UK | Second-biggest market; 7 abandoned checkouts since 12 Sep carried the charge |
| Isle of Man | £12.99 (Europe zone) | Into the Channel Islands zone | inland cost | Royal Mail prices it as UK |

- Fixed local-currency shipping works because the US zone holds one country and the Eurozone zone holds one currency.
- **International free shipping: none for now.** US at $250 would cost £20.70–£32.90 a parcel (11–18% of order value) and EU at €150 about 13–15%, against roughly 12% for the UK at £30. Needs unit costs to judge (Q7).

## Shopify changes required

### Can safely implement (nothing a customer pays changes)

1. Country/region selector in header and footer (theme workstream).
2. Delete the draft duplicate "United Kingdom" market.
3. Strip GB, GG, JE, US, CA, AU, NZ and the EU states out of "all world". Required before fixed prices: overlapping catalogs that aren't nested show the lower price.
4. Product data (product-data workstream): HS codes on 17 products, origin CN on China-made products, weights on 11, HydroCuff HS to 6201.40.

### Requires George's approval

5. Single-country "United States" market; "United States and Canada" becomes "Canada". USD catalog with the fixed list (CSV import).
6. EUR catalog with the fixed list on the European Union market; optionally add MC, AD, SM, VA, ME, XK.
7. Shipping zones and rates as above.
8. Channel Islands free Tracked 48 from £30.
9. US duty collection at checkout (line item) and Royal Mail PDDP for US parcels. Shopify charges 0.5% on orders where it calculates duties (temporary rate).
10. Any international free-shipping threshold; any EU VAT change (accountant).

## ROI

Scenarios, not forecasts — the programme's evidence rule applies.

- **Revenue affected so far:** overseas 1.5% of 12-month net sales (14 orders, £877); Channel Islands 6.4% (63 orders, £3,700).
- **Where the upside is:** the checkout drop-off. Last 12 months, US + EU had 269 checkout starts and 33 completions (12%). At 25% — half the UK rate — that's about 34 more orders, roughly £3.4k a year at a £100 order. On the current US run-rate (108 starts in 90 days, ~430 a year) 25% completion alone would mean ~100 US orders a year.
- **Likely conversion effect:** cleaner prices on their own are a small lever. The selector (local price from the first page), clean shipping and an upfront US duty line address where buyers actually leave.
- **Margin:** product prices land 1–9% above UK net per unit (one EUR line −1.9%). Shipping changes stop £2–£19 losses per overseas parcel. Duty collection removes the risk of CROOKS absorbing ~36% duty on Royal Mail US parcels.
- **Effort:** about 4–6 hours of admin once decided — Markets restructure 1h, two catalog CSVs 1h, shipping zones 1h, duty setup and test orders 1h — plus the product-data and theme items.
- **Measure:** checkout completion by country from F1 is the baseline; re-pull at 30 and 60 days after go-live.
