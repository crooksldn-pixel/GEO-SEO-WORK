# Next

Updated 18 Oct 2026, 20:30 BST. The live theme is "CROOKSLDN — live 18 Oct + evening fixes" (207475147095). FINDINGS 1–6 are the 16 Oct before state of the old live and no longer describe the current live. Use FINDINGS 7–8.

## Do next

1. **Password lock (P0).** George decides. Nothing else counts while shoppers get `/password`.
2. **Agree the next theme to publish.** Probably "live 18 Oct + colour photos" (207476752727), if its owner is finishing it. In that one theme, once its owner has stopped editing:
   1. Judge.me storefront embeds off. In Theme editor → App embeds, switch off "Judge.me" (core) and "Judge.me cart drawer widget". In `config/settings_data.json` these are blocks 14060646107696862457 and 13047258039897440615, set `disabled: true`. Leave Orderify, Mida, Partner Hub, Forms and Omnisend as they are.
   2. Tee stock lines and tee schema timings, as written in `artifacts/code-handoff-tee-stock-and-schema.md`. This is code, so a code-allowed session does it.
   3. Status bar m2, if George approves the wording.
   4. Preview-check:
      - a tee: no stock line; the 2–3 day line; JSON-LD handling 2–3 and transit 2–3
      - a hoodie: "IN STOCK"; same-day line; handling 0–2
      - the footer: OUTERWEAR
      - no `jdgm` scripts or styles in the page source
      - Orderify, Mida and Partner Hub still loading
   5. Duplicate the current live as a backup, then George clicks **Publish**.
3. **After publish:** repeat the checks on the live site (needs the password lock off for a public check). Log each change in CHANGES.md with the time and the check.
4. **If George would rather not wait for a copy:** he can flip the two Judge.me toggles on live in about a minute. Only do this if no copy-of-live is about to be published. Publishing a copy made before the flip would switch them back on.

## Do not do yet

- **Do not publish "CROOKSLDN — live + 18 Oct approved fixes" (207468855639).** It predates tonight's live and would wipe it. Everything useful in it is already live.
- Do not publish "Claude P1 fixes" (decision #7).
- Do not write to live or to any copy while another session is editing a copy of live.
- Do not switch off Orderify (decision #26), Mida or Partner Hub.
- Do not turn on Judge.me review display. Leave Judge.me backend review collection alone (decision #22).
- Do not touch the password setting, products, collections, menus or Merchant Center.

## Decisions still required

- Password lock: intentional, or off?
- Who owns "live 18 Oct + colour photos", and is it next to publish?
- Status bar m2 wording. Proposed: "IN-STOCK ORDERS BY 6PM DISPATCHED TODAY".
- Who makes the code changes in the handoff file.

## Data still required

None.

## Recommended follow-up date

- Same evening as the next publish: live checks as above.
- About 1 Nov 2026: Search Console internal links to `/collections/outerwear`, and Rich Results on a tee for the new handling time. Only meaningful once the password lock is off.
