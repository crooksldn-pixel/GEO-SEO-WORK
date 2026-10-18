# Changes

**No changes have been made** to Shopify, any theme, any app, Merchant Center or any live URL by this workstream. The brief was research only.

Store reads were read-only Admin API queries. They covered:
- policies
- delivery profiles
- products and inventory
- theme lists and file checksums
- file contents of the live theme and the held "Claude P1 fixes" theme

The held theme was read as source only. It was never previewed or published.

## Test side effects (not site changes, recorded for completeness)

- **16 Oct ~21:00 BST — checkout session.** The existing test cart in George's built-in browser was used: 1 × PINK CONVICT SWEATS XL, pre-order, £51. It was taken to checkout's shipping-method step to read live rates. The brand's own published returns address (Bourne End Business Park, Bourne End, SL8 5AS) was typed to get rates. Address and city were cleared afterwards; the postcode may remain in that checkout session. No email or payment details were entered and nothing was submitted. The cart was not changed.
- **16 Oct ~21:03 BST — popup flag in that browser.** `crooksldn_ctc_seen` was removed from the built-in browser's localStorage to see the popup as a first-time visitor. The popup was closed with ×, then the flag was set back to `1`. This is per-browser and doesn't affect any customer.
- **18 Oct 16:35 BST — checkout re-read.** The same checkout session was reloaded to read the state of the marketing checkbox. Nothing was entered.
