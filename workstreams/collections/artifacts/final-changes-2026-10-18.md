# Final changes for George's "go", 18 Oct 2026

Built from George's answers (`../ANSWERS.md`, owner decisions 11, 13, 15, 21, 27 and 28) and the source files on `cowork/project-files-import`. Every target value was re-read live at 19:15–19:30 BST on 18 Oct.

**State: PREPARED.** Nothing here is live until George types "go" in the collections chat.

How the live theme handles lengths (`snippets/meta-tags.liquid`):
- It adds ` | CROOKSLDN` to a title only if the result stays within 56 characters. Longer titles show without the brand and are not cut mid-word.
- It trims meta descriptions over 160 characters.

---

## 1. /collections/denim (admin UI, collection 688184099159): Q1 + Q2

Remove the origin clause (Q2) and append the outfit line (Q1). Nothing else changes.

```html
<p>CROOKSLDN denim comes in three cuts. Yard Jeans are 14oz denim in an OG straight cut with a mid rise: structured, not baggy, in blue or grey wash, with an embroidered handcuff graphic on the back pockets. Yard Jorts are baggy 14oz denim shorts that finish below the knee, with the Convict embroidery on the back pockets, also in blue or grey wash. OG Jeans are heavyweight denim with a baggy, stacked fit and a white handcuff graphic on the back pockets. Wash the Yard pieces cold, inside out, and hang dry. Sizes XS to XL, with measurements in each size guide.</p><p>Wear them with the <a href="/collections/sweats">Convict Hoodie</a> or a <a href="/collections/tees">graphic tee</a>.</p>
```

## 2. /collections/sweats (admin UI, collection 688184131927): task A + C + Q9

- **H1:** stays `Sweats`. There is no Search Console evidence for changing it.
- **SEO title:** `Heavyweight Hoodies & Joggers | Baggy Fleece Sweats` (51 characters, so it renders without the brand suffix)
- **Meta** (157 characters): `Convict hoodies and joggers in 550gsm brushed fleece, baggy fit, in matching colours. 450gsm Cellblock crewneck and shorts. XS–XL. Free UK shipping over £30.`
- **Description:**

```html
<p>CROOKSLDN sweats are heavyweight brushed fleece cut baggy. The Convict Hoodie and the Convict Sweats, our joggers, are 550gsm, 100% cotton and come in Black with white contrast piping, Grey with the embroidered handcuff logo, or Pink with white piping and handcuff embroidery, with the sweats cuffed at the hem. Each piece is £60; wear hoodie and sweats together as a tracksuit from the <a href="/collections/tracksuits">Tracksuits</a> collection.</p><p>The Cellblock Crewneck (£50) and Cellblock Shorts (£45) are a lighter 450gsm brushed fleece in a relaxed cut with 3D embroidery, and come together as a matching co-ord, the <a href="/products/cellblock-set">Cellblock Set</a>.</p><p>Sizes run XS to XL and are true to size. Every product page lists the garment's own measurements: the Convict Hoodie's chest runs from 116.8cm in XS to 132.1cm in XL. Pair them with <a href="/collections/denim">Yard Jorts</a> when it's warm.</p><p>Not sure on size? See <a href="/blogs/news/convict-vs-cellblock-fit">how the Convict and Cellblock fits compare</a>.</p>
```

- **Rule (Q9):** change from "all conditions: Type = Sweats" to "any condition: Type = Sweats, OR Title = CELLBLOCK SET". The collection goes from 8 products to 9.

What differs from the copy approved on 16 Oct (workstream 01):
- The confirmed weights are added: 550gsm and 100% cotton for Convict, 450gsm for Cellblock.
- Prices are the live ones (£50, £45, £60).
- The C fit-guide sentence is added.
- "our joggers" is added to the intro, and the meta says "hoodies and joggers" instead of "hoodies and sweats". Search Console shows "joggers" is the largest product query cluster, and almost all of it lands on the homepage (search-console report, row 2).

## 3. /collections/tracksuits (Admin API, collection 687058518359): Q3

Append as the last paragraph. The existing two paragraphs stay unchanged.

```html
<p>Not sure on size? See <a href="/blogs/news/convict-vs-cellblock-fit">how the Convict and Cellblock fits compare</a>.</p>
```

## 4. Fit article (Admin API, Article 676342530391): Q4

Replace the existing gsm section with:

```html
<h2>Is 550gsm heavy?</h2>
<p>Yes. gsm is grams per square metre of fabric, and the Convict Hoodie and Convict Sweats are 550gsm, 100% cotton fleece: a heavy fabric, which is what gives them their structured hang. The Cellblock Crewneck and Shorts are 450gsm, so the Convict fabric is about 22% heavier, and the Cellblock is the one for layering or warmer days.</p>
```

The rest of the article is unchanged.

## 5. Reactive guide: new article /blogs/news/reactive-outerwear (Admin API, blog News): Q5

- **Title:** `Reactive outerwear: how the HydroCuff and Double-Agent Puffa work`
- **SEO description** (metafield `global.description_tag`): `What water-reactive and heat-reactive jackets do, how CROOKSLDN's HydroCuff and Double-Agent Puffa react, and how to look after them.`
- **Author:** CROOKSLDN (same as the fit guide)
- **Tags:** reactive, outerwear, care
- **Summary:** `<p>What the water-reactive HydroCuff Windbreaker and heat-reactive Double-Agent Puffa do, and how to look after them.</p>`
- **Published:** yes

What the owner decisions changed from draft section 4 (decisions 11 and 15):
- The durability line stays.
- The Puffa turns white with heat and goes back to black as it cools.
- The Puffa care line is only "avoid washing where possible".
- One added FAQ: "Does the Double-Agent Puffa change back?"

```html
<p>We make two reactive jackets: one reacts to water, one to heat. Here's what each does and how to look after it.</p>
<h2>What "reactive" means here</h2>
<p>A reactive garment changes how it looks when something in its surroundings changes. The HydroCuff reacts to water, and the Double-Agent Puffa reacts to heat.</p>
<h2>HydroCuff Windbreaker: water-reactive</h2>
<p>When the HydroCuff gets wet from rain or water, a cuff pattern comes through on the fabric. When it dries, it goes back to its normal state, so the pattern only shows when it's wet. It's made to react wear after wear.</p>
<p>It's a hooded windbreaker with zipped front pockets and contrast stitching. £85, XS–XL. <a href="/products/hydrocuff-windbreaker">Shop the HydroCuff</a></p>
<h2>Double-Agent Puffa: heat-reactive</h2>
<p>The Double-Agent Puffa is black, turns white with heat and goes back to black as it cools. It's a padded puffer with Crooks handcuff embroidery on the chest and hood and concealed hand pockets. £140, XS–XL. <a href="/products/double-agent-puffa">Shop the Double-Agent Puffa</a></p>
<h2>Looking after them</h2>
<table>
<thead><tr><th></th><th>HydroCuff Windbreaker</th><th>Double-Agent Puffa</th></tr></thead>
<tbody>
<tr><td>Reacts to</td><td>Rain and water</td><td>Heat</td></tr>
<tr><td>Goes back to normal</td><td>Yes, once dry</td><td>Yes, back to black as it cools</td></tr>
<tr><td>Washing</td><td>Wash cold</td><td>Avoid washing where possible</td></tr>
<tr><td>Ironing</td><td>Do not iron</td><td>—</td></tr>
</tbody>
</table>
<h2>Questions</h2>
<p><strong>Does the HydroCuff pattern stay on after it dries?</strong> No. It shows when the jacket is wet and goes back once it's dry.</p>
<p><strong>Does the Double-Agent Puffa change back?</strong> Yes. It turns white with heat and returns to black as it cools.</p>
<p><strong>Can I wash the Double-Agent Puffa?</strong> We recommend avoiding washing it where possible.</p>
<p><strong>Where can I see both?</strong> In <a href="/collections/outerwear">Outerwear</a>.</p>
<p>Questions about either jacket? Email <a href="mailto:team@crooksldn.com">team@crooksldn.com</a>.</p>
```

## 6. /collections/outerwear (Admin API, collection 698784121175): Q5, draft section 3

Apply this after the guide is live, so the link never points to a 404.

- **SEO title:** unchanged (`Water-Reactive & Heat-Reactive Jackets`)
- **Meta** (from draft section 3, 135 characters): `Reactive outerwear from CROOKSLDN: the HydroCuff windbreaker reacts to rain, the Double-Agent Puffa to heat. Free UK shipping over £30.`
- **Description:**

```html
<p>CROOKSLDN outerwear reacts to the weather. The <a href="/products/hydrocuff-windbreaker">HydroCuff Windbreaker</a> (£85) shows a cuff pattern in the rain and goes back to normal once it dries. The <a href="/products/double-agent-puffa">Double-Agent Puffa</a> (£140) is a padded, heat-reactive puffer that turns white with heat and back to black as it cools, with Crooks handcuff embroidery on the chest and hood.</p><p>See <a href="/blogs/news/reactive-outerwear">how the HydroCuff and Double-Agent Puffa work</a>, and how to look after them.</p>
```

## 7. URL redirects (Admin API): Q6 + decision 21

Every source returned 404 when checked live on 18 Oct, and none has a redirect yet. Search Console shows none of them with real traffic: the most any has is 1 click (`white-tesco-tshirt`) over 16 months.

| Path | Target |
|---|---|
| `/products/og-crook-tee` | `/collections/tees` |
| `/products/3-clives-tee` | `/collections/tees` |
| `/products/broadcast-tee` | `/collections/tees` |
| `/products/evil-clive-tee` | `/collections/tees` |
| `/products/large-duffle-bag` | `/collections/accessories` |
| `/products/white-tesco-tshirt` | `/products/crooks-express-t-shirt` |
| `/products/black-tesco-tshirt` | `/products/crooks-express-t-shirt` |

## 8. /collections/frontpage (Admin API, collection 678766281047): Q6c

Set metafield `seo.hidden` = `1` (`number_integer`). This removes the page from the sitemap and adds noindex. It is not unpublished and not deleted. Search Console: 76 impressions and 0 clicks over 28 days, as a brand sitelink.

## Not doing

- **Contact page "run out of London" (decision 13).** The text isn't page content. It's the `about_body` setting of the `crooks-contact` section in the live theme's `templates/page.contact.json`, and this session's brief bars theme edits. The theme-editor session was changing the live theme at 18:37–18:58 BST on 18 Oct. Handed to theme-editor with the exact text: `<p>CROOKSLDN is an independent British streetwear brand. Short runs, made properly, packed by hand.</p>`. The second paragraph stays.
- **/collections/sets:** left as is (Q8).
- **CB1/CB2 redirects:** left as is (Q7, decision 27).
- **Sweats H1:** stays "Sweats".
