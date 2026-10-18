# GEO panel: method

Use this method for every run so results stay comparable. It was first used on 16 Oct 2026. Do not cite the older "GEO 43→54" scores: they were made without a method.

## Queries (21)

The ★ core queries run on all four surfaces first. In a "core" run, only these 8 are run.

| Group | Queries |
|---|---|
| brand | Crooks LDN ★ · Crooks London · Crooks LDN reviews |
| product | 550gsm hoodie UK ★ · heavyweight hoodie UK ★ · baggy hoodie UK · baggy jeans UK ★ · heavyweight tracksuit UK |
| category | British streetwear brands · independent British streetwear · London streetwear brands · emerging UK streetwear brands · best UK streetwear brands ★ |
| competitor | brands like Corteiz ★ · Corteiz alternatives · brands like Carsicko · brands like Broken Planet |
| specialist | water reactive clothing · water reactive jacket ★ · heat reactive clothing · heat reactive puffer ★ |

Type each query exactly as written, with no follow-ups.

## Environment

- UK network, no VPN. Record the IP country in `meta.json`.
- Use a browser profile that is signed out of Google, with cookies cleared. On consent banners pick reject / necessary only. The 16 Oct run used the Claude desktop app's built-in browser, which has its own profile separate from George's Chrome.
- ChatGPT, Gemini and Perplexity: stay logged out. If a surface forces a login, use one dedicated panel account with memory and custom instructions off. Open a new chat for every run.
- Watch for **Crooks & Castles** (and Crooks and Candy, Crooks 1926, Crooks' Corner) being mistaken for Crooks.

## Google UK (1 load per query)

1. Open `https://www.google.co.uk/search?q=<query>&gl=uk&hl=en-GB&pws=0`.
2. Wait about 15 seconds. The AI Overview streams in, and an early capture can be half-finished.
3. Expand the AI Overview with "Show more".
4. Record:
   - the position of the first crooksldn.com result in the top 20;
   - that URL;
   - AI Overview Y/N, and whether it names Crooks;
   - the first 5 other domains;
   - whether a shopping or product pack appears (written as `shopping_pack=Y/N` at the start of `notes`);
   - the AI Overview's sources in `sources_cited`: the inline source chips plus the visible source cards. On the 16 and 18 Oct runs the "Show all" button was not opened. Keep it that way so runs stay comparable.
5. If crooksldn.com is not on page 1, check page 2 (`&start=10`) and screenshot it as `<name>_p2.png`.
6. Position counts every titled result block in order, including TikTok, Instagram, Reddit and video blocks. Pages 1–2 usually hold 16–20 of these.

## ChatGPT / Gemini / Perplexity (3 runs per query)

For each run, record:
- whether Crooks is named, and its list position;
- every brand named, in order (leave out the brand named in the query itself);
- cited sources in display order;
- sentiment towards Crooks;
- any Crooks product named.

Surface-specific notes:
- **Gemini** shows sources only as chip labels without URLs. Record the label exactly as shown.
- **Perplexity:** click "N sources" to reveal the full source list. Logged out, it allowed only about 5 answers before a "Sign up and repeat your request." wall.
- **Background tabs do not render.** ChatGPT and Gemini stall on "Searching the web" until their tab is brought to the front. Collect each answer with its tab in front.
- **Answers fade in after streaming.** Wait 2–3 seconds after the text stops changing before taking the screenshot.

## Recording rules

- Only record what is on screen. Never fill a cell from memory.
- If a run is blocked (captcha or login wall), leave `crooks_mentioned` blank and put the reason in `notes`, starting with `BLOCKED:`.
- If a query could not be run at all, write `NOT RUN:` and the reason in `notes`.
- Screenshots go in `shots/<surface>__<query-slug>__<run_n>.png`.

## Output per run (`runs/YYYY-MM-DD/`)

- `results.csv`: UTF-8, with this header:
  `run_date,surface,query_group,query,run_n,crooks_mentioned,crooks_position,crooks_url,ai_overview,crooks_in_ai_overview,competitors,sources_cited,sentiment,product_surfaced,screenshot,notes`
- `meta.json`: run_date, type, ip_country, browser, model and login state per surface, started, finished, problems.
- `summary.md`: mention rate by query group and surface, Google UK positions, and the sources the AI answers cite most.
- Never edit a past run. To fill a gap, make a new dated run folder. Set its `meta.json` type to say what it completes, as `runs/2026-10-18/` does (type "gap-fill (Google UK only)", `completes_run` 2026-10-16).
