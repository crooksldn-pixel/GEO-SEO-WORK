# Next

## Do next

1. **B, B2, C, D**: if George has said yes in chat, apply them exactly as in `artifacts/proposed-changes.md`.
   - Denim (B, B2): use the Shopify admin UI, collection 688184099159, description HTML view. The Admin API can't see it.
   - Tracksuits (C) and the fit article (D): use the Admin API.
   - Re-read each value first. If it no longer matches the baseline, stop and show George the new before.
   - After saving, read the change back on the live page and log it in `CHANGES.md`.
2. **A**: when `workstreams/01-collections-internal-linking.md` is available, build the final Sweats text:
   - the "Sweats" section from that file
   - "550gsm, 100% cotton" for the Convict pieces and "450gsm" for Cellblock
   - the C fit-article sentence
   Show George the final text, then apply it in the admin UI (collection 688184131927). Keep the H1 as "Sweats".
3. **F**: when `cowork-results/05-search-console.md` lands, check clicks and impressions for the URLs in `artifacts/index-hygiene-audit.md`. Propose the redirects and the frontpage `seo.hidden` change to George, and create them on his yes.
4. **CB1/CB2**: once George confirms the washes, edit the two wrong redirect targets.
5. **E**: once George approves `05-reactive-drafts.md` sections 3 and 4, publish `/blogs/news/reactive-outerwear`, link it from Outerwear, and link it to both jackets.
6. Copy `artifacts/proposed-changes.md`, with the approval and read-back fields filled in, to `/mnt/project-files/seo/cowork-results/02-collections.md` when that folder is reachable.

## Do not do yet

- Changing the Sweats H1 to "Heavyweight Sweats". It waits on Search Console data.
- Publishing the reactive guide. It waits on George's approval of the drafts.
- Redirecting `/collections/sets`. Don't do it at all (Finding 2).
- Deleting any collection, including the `-1` duplicates, which already redirect.
- Touching products, the theme, Merchant Center or outreach. Other sessions own those.

## Decisions still required

- Yes or no on B, B2, C and D.
- Which wash CB1 and CB2 were.
- Approval of the E drafts.
- Optional, not in the brief: whether the Cellblock Set should also appear in Sweats. It would need the Sweats smart rule changed to "Type = Sweats OR Title = CELLBLOCK SET". Today the Cellblock Set is only browsable through Sets and ALL.

## Data still required

- The five project files listed in STATUS.md, Blocker 2
- `cowork-results/05-search-console.md`

## Recommended follow-up date

Nothing is live yet, so there's no measurement date. Once a change goes live, check Search Console for that URL 28 days later.
