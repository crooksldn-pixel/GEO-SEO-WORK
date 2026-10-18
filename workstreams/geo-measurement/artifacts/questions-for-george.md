# geo-measurement: questions for George

**Asked:** 18 Oct 2026, 17:15 UK  
**Branch:** `cowork/geo-measurement`

These are everything this workstream needs from George. Each question has its options and what happens with each answer.

**How to answer:**
1. Write the answer after **Answer:** under each question, in this file on this branch.
2. Commit with a message such as `answer geo-measurement questions`.
3. Tell the geo-measurement session "answered".

Answers pasted into that chat also work. None of these blocks the baseline, which is already measured.

---

## Q1 — Perplexity: sign in a panel account, or drop Perplexity?

**Why:** Logged out, Perplexity answered 5 runs and then showed "Sign up and repeat your request." 58 of 63 Perplexity runs are blank. See FINDINGS Finding 8.

**Options:**
- **A. Sign in.**
  1. Create a dedicated Perplexity account for the panel.
  2. Sign in yourself, in the Claude desktop app's built-in browser, in the Perplexity tab. I can't type passwords for you.
  3. Turn off memory and personalisation in its settings.
  4. **Sign up with email, not "Continue with Google".** A Google sign-in would also sign that browser into Google, and the Google UK and Gemini runs must stay signed out to remain comparable with the baseline.
- **B. Drop Perplexity.** The panel stays at Google UK, ChatGPT and Gemini, and the method is updated to match.

**What happens next:**
- **A:** I run Perplexity for all 21 queries × 3 into a new dated run folder ("Perplexity gap-fill"), with the login state recorded in `meta.json`.
- **B:** I record the decision in `panel-method.md` and `STATUS.md`, and close Blocker 1.

**Answer:**

---

## Q2 — Is Crooks London Limited (Companies House 16396366) your company?

**Why:**
- Perplexity (3 of 3 "Crooks LDN" runs) cites "Crooks London Limited, 16396366, incorporated 19 Apr 2025, Englefield Green" as the brand's company.
- ChatGPT ("Crooks London" run 2) also points to Crooks London Limited.
- The entity used for profiles is Crooks Clothing Company Ltd (16606021).

See FINDINGS Finding 6, and screenshot `artifacts/runs/2026-10-16/shots/perplexity__crooks-ldn__1.png`.

**Options:**
- **A. Not mine / unrelated.**
- **B. Mine or connected** (say how).
- **C. Don't know.**

**What happens next:**
- **A:** Finding 6 is updated to say the AI engines attach an unrelated company to the brand. That becomes a High-priority recommendation to the entity / About work to state Crooks Clothing Company Ltd (16606021) on the site and in Organization `legalName`.
- **B:** Finding 6 records it as a known second company. The recommendation becomes making sure the site names 16606021 as the trading entity.
- **C:** It stays open.

**Answer:**

---

## Q3 — This repo is public. Keep the measuring network's IP address in it?

**Why:** The run `meta.json` files record the IP address and network the panel ran from, plus a location footer from Gemini (removed 18 Oct per owner decision #16). The method only needs the country (GB).

**Options:**
- **A. Keep as is.**
- **B. Redact from now on.** New runs record only "GB, Three UK". The two existing run folders stay unchanged, under the never-edit-a-past-run rule.
- **C. Redact everywhere.** This edits the 16 and 18 Oct `meta.json` files, which is an explicit exception to never editing a past run. Even then, git history keeps the old values unless the history is rewritten, which needs a force-push. Say whether you want that too.

**What happens next:** I apply the chosen option and log it in `CHANGES.md`.

**Answer:**

---

## Q4 — Switch the GitHub default branch to `main`

**Why:** This branch is still the repo's default, because it was pushed before `main` existed. A new session that clones without naming a branch lands on this workstream's files. No session can change the default: "Repository settings writes are not permitted". `cowork/programme-records` raised the same thing (its Finding 2), and one action closes both.

**Action:** GitHub → the repo's Settings → default branch → `main`.

**Answer:** done / not done

---

## Q5 — Add "water reactive windbreaker" as an extra tracked query?

**Why:** `cowork/search-console` Finding 2 shows it as a real Search Console query for crooksldn.com. It is not in the panel's 21. Adding it to the 21 would break comparability with the baseline. Tracking it as a separately labelled extra query would not.

**Options:**
- **A. Yes,** as a labelled extra from the next run.
- **B. No.**

**Answer:**

---

## Q6 — Control re-run on Fri 13 Nov 2026 (evening)

**Why:** The panel runs in the built-in browser on your Mac, on your UK connection. The Mac has to be on, with the Claude desktop app open, for the whole run. On 16 Oct the run stopped when the Mac went offline.

The 16 Oct run of all 21 queries took about 1.5 hours. The core 8 should take roughly 40 minutes, though that is an estimate.

**Options:**
- **A. 13 Nov works.**
- **B. Use another date:** name it.

Also say whether you want this set up as a scheduled task that starts the run automatically. It would still need the Mac on.

**Answer:**

---

## Q7 — Is the GitHub branch enough as the record, or do you still want the run files in the Project folder?

**Why:** The original brief asked for the runs in the Project folder (`seo/measurements/geo-panel/runs/`). No Cowork session can reach that folder (see `cowork/programme-records` Finding 1 and issue #1). The two runs are complete on this branch. They were also sent to you in chat as `geo-panel-run-2026-10-16.zip` and `geo-panel-run-2026-10-18.zip`.

**Options:**
- **A. The branch is enough.**
- **B. I've uploaded the zips** to the Project folder.
- **C. I'll upload them later.**

**Answer:**
