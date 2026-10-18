<!-- Copied from the claude.ai Project seo/ folder on 18 Oct 2026 and sanitised for this public repo (owner decision #16): sales figures, order counts, age, town/address and IP removed. -->
# Reactive outerwear copy: DRAFTS (not live)

Workstream 5 · master-queue Q37 · drafted 16 Oct 2026 · **status: draft, needs George's approval before any store change.**

**Facts used, and nothing else.** These are owner-confirmed on 16 Oct 18:26 UTC (see [[crooksldn-brand-facts]] in memory), plus what is already in Shopify product data:
- HydroCuff Windbreaker (£85, black, XS–XL): reacts to rain and water; returns to its normal state once dry; wash cold; do not iron; the reaction is "reasonably durable". Already in Shopify: water-activated cuff pattern, hooded, zipped front pockets, contrast stitching.
- Double-Agent Puffa (£140, XS–XL): heat-reactive; avoid washing where possible. Already in Shopify: changes appearance with temperature, handcuff embroidery on chest and hood, padded fit, concealed hand pockets.

**Still gated (not used anywhere below):** reaction time, number of cycles or lifetime, wash temperatures, how the effect works (ink or fabric type), what temperature triggers the Puffa, whether the Puffa returns to its normal state, fabric composition of either jacket. Origin is not mentioned (it isn't needed on the page).

**Two wording calls for George** (marked ⚑ below):
1. "Reasonably durable": the drafts say *"made to react wear after wear"*. If that overstates it, the fallback is to say nothing about durability.
2. Puffa: the drafts say it changes *"with heat"* and avoid saying it changes back. Confirm whether it returns to normal as it cools; if yes, the line "and back again as it cools" can be added.

---

## 1. HydroCuff Windbreaker: product description

Target intent: "water reactive jacket", "rain reactive jacket", "colour changing rain jacket". Primary URL: /products/hydrocuff-windbreaker.

> **HydroCuff Windbreaker.** Rain brings it out. When the jacket gets wet, a cuff pattern comes through on the fabric; once it dries, it goes back to plain black. ⚑ Made to react wear after wear.
>
> Hooded, with zipped front pockets and contrast stitching.
>
> **Care:** wash cold. Do not iron.

SEO title (unchanged, already good): `HydroCuff Windbreaker — Water-Reactive Jacket | CROOKSLDN`
Meta (optional refresh, 150 chars): `Water-reactive windbreaker: a cuff pattern comes through in the rain and fades back once dry. Hooded, zipped pockets. Wash cold, do not iron.`

Note: "goes back to plain black" assumes the dry state is solid black (the only colourway). Check against a dry photo before publishing.

## 2. Double-Agent Puffa: product description

Target intent: "heat reactive puffer", "heat reactive jacket", "colour changing puffer". Primary URL: /products/double-agent-puffa.

> **Double-Agent Puffa.** A heat-reactive puffer: it changes appearance with heat. ⚑
>
> Crooks handcuff embroidery on the chest and hood, a padded fit and concealed hand pockets.
>
> **Care:** avoid washing where possible. Spot clean if needed.

⚑ "Spot clean if needed" is a sensible addition but is not owner-confirmed. Delete it if George doesn't want it.
SEO title (current one lacks the brand): `Double-Agent Puffa — Heat-Reactive Puffer Jacket | CROOKSLDN`
Meta (unchanged): current meta is accurate.

## 3. Outerwear collection: intro line

This replaces the reactive sentences in workstream 1's Outerwear draft (01-collections-internal-linking.md, Outerwear section) so the collection and PDPs say the same thing. Workstream 1 owns the collection; this is the text only.

> CROOKSLDN outerwear reacts to the weather. The [HydroCuff Windbreaker](/products/hydrocuff-windbreaker) (£85) shows a cuff pattern in the rain and goes back to normal once it dries. The [Double-Agent Puffa](/products/double-agent-puffa) (£140) is a padded, heat-reactive puffer with Crooks handcuff embroidery on the chest and hood.

Meta: `Reactive outerwear from CROOKSLDN: the HydroCuff windbreaker reacts to rain, the Double-Agent Puffa to heat. Free UK shipping over £30.`

## 4. Reactive clothing guide (article draft)

- **Proposed URL:** /blogs/news/reactive-outerwear (blog "News", same as the fit guide).
- **Intent:** informational and comparison: "what is water reactive clothing", "how does a water reactive jacket work", "do heat reactive jackets change back", "how to wash a water reactive jacket". This doesn't cannibalise the PDPs, which target the buying queries; the guide links to both and to /collections/outerwear.
- **GEO purpose:** a plain, quotable page AI assistants can cite when asked for streetwear brands with reactive jackets.
- **Priority:** P3. /collections/outerwear is already live (created 16 Oct), so publishing waits only on the ⚑ calls above. It's short on purpose: we can't explain the mechanism yet, and padding it out would mean inventing facts.

**Title:** `Reactive outerwear: how the HydroCuff and Double-Agent Puffa work`
**Meta:** `What water-reactive and heat-reactive jackets do, how CROOKSLDN's HydroCuff and Double-Agent Puffa react, and how to look after them.`

> We make two reactive jackets: one reacts to water, one to heat. Here's what each does and how to look after it.
>
> ## What "reactive" means here
> A reactive garment changes how it looks when something in its surroundings changes. The HydroCuff reacts to water, and the Double-Agent Puffa reacts to heat.
>
> ## HydroCuff Windbreaker: water-reactive
> When the HydroCuff gets wet from rain or water, a cuff pattern comes through on the fabric. When it dries, it goes back to its normal state, so the pattern only shows when it's wet. ⚑ It's made to react wear after wear.
> It's a hooded windbreaker with zipped front pockets and contrast stitching. £85, XS–XL. [Shop the HydroCuff](/products/hydrocuff-windbreaker)
>
> ## Double-Agent Puffa: heat-reactive
> The Double-Agent Puffa changes appearance with heat. ⚑ It's a padded puffer with Crooks handcuff embroidery on the chest and hood and concealed hand pockets. £140, XS–XL. [Shop the Double-Agent Puffa](/products/double-agent-puffa)
>
> ## Looking after them
> | | HydroCuff Windbreaker | Double-Agent Puffa |
> |---|---|---|
> | Reacts to | Rain and water | Heat |
> | Goes back to normal | Yes, once dry | ⚑ (confirm) |
> | Washing | Wash cold | Avoid washing where possible |
> | Ironing | Do not iron | — |
>
> ## Questions
> **Does the HydroCuff pattern stay on after it dries?** No. It shows when the jacket is wet and goes back once it's dry.
> **Can I wash the Double-Agent Puffa?** We recommend avoiding washing it where possible.
> **Where can I see both?** In [Outerwear](/collections/outerwear).
>
> Questions about either jacket? Email [team@crooksldn.com](mailto:team@crooksldn.com).

If it's approved later: add FAQPage-style Q&A only if workstream 2's schema setup supports article FAQ markup (it's not required for the page to work). Add dry/wet HydroCuff photos and Puffa normal/reacted photos (workstream 8, Q12) to the guide.

## Validation before anything goes live
- George approves wording, including both ⚑ calls.
- Check the dry-state colour against a photo.
- Re-read the live PDPs immediately before editing, since other threads may have changed them.
- Log baseline, change and the metric to watch in /mnt/project-files/seo/change-log.md: impressions and clicks for "water reactive jacket" / "heat reactive puffer" on the PDPs (GSC), and the GEO query-set rows for the four Specialist queries.
