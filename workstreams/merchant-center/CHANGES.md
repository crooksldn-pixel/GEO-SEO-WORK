# Changes

## 18 Oct 2026, 20:12 BST — Business name changed to "Crooks LDN"

**State:** LIVE

**Affected:**
- Merchant Center 5860086407 > Settings > Business info > Business details > Business name

**Before:**  
"CROOKSLDN". Google rejected it as an invalid business name and showed the seller as "crooksldn.com" instead.

**After:**  
"Crooks LDN". Only the Business name section was saved; the address and customer service fields weren't touched.

**Reason:**  
Owner decision #9 / Q2 (ANSWERS.md); George's "answered" in this chat at 20:08 BST.

**Target:**  
Seller name shown on Shopping and free listings (FINDINGS 4).

**Validation:**  
Read back on the Business info page at 20:12 BST: "Crooks LDN". The account switcher shows "Crooks LDN". By 20:13 the "Setup and policy issues" count had dropped from 2 to 1, though which issue cleared wasn't checked. Google's re-review of the name can take a few days.

**Expected metric:**  
"Invalid business name" stays cleared, and listings show "Crooks LDN" as the seller once the store's password lock is off.

---

## Not done: the two approved writes this session's permission check refused

Both are approved by George (ANSWERS.md, Q1 and Q3), but this session's permission check refused them because the approval sits in a repo file, not in the chat. Each needs George to type the yes directly in this Cowork chat.

1. **Archive the 10 `CROOKSRELEASESEPT` products** (IDs `G-65230983` to `G-65230992`, added 28 Sep). The products were filtered to "Data source: Merchant Center" and all 10 selected, then the Archive button was refused. Nothing was archived. Merchant Center offers **Archive**, which is reversible, on this list. This session won't hard-delete; if George wants them gone for good, he can delete them from the archive himself.
2. **Tee handling time:** add a supplemental product source carrying [artifacts/gmc-supplemental-tee-handling-GB.tsv](artifacts/gmc-supplemental-tee-handling-GB.tsv), linked to the **GB** "Shopify App API" source only. Nothing was created.

---

## Read-only actions

- Downloads from Merchant Center:
  - products, 16 Oct and 18 Oct 20:22 BST
  - issues, 18 Oct 16:35 and 20:13 BST
  
  A download changes nothing.
- The UK £3 shipping policy's edit wizard was opened to read its values, then left with Cancel.
- Filter, select and expand actions in product lists. "Add all products found", "Add now", "Remind me later", opt-out and delete controls were left alone.
