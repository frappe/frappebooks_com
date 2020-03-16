---
base_template_path: templates/doc.html
title: Bills
intro: A bill that your supplier sends you for products or services you have purchased.
---

### Creating Bills

When you have expenses that you don’t have to pay right away, record them by
creating a Bill in Frappe Books. Your supplier may accept the payment later,
after shipping, or you may have some other arrangement.

To access the Bill list, go to:

> Purchases > Bills

1. Click on the blue plus button. A New Bill form will open up.
1. Select the Supplier or create one from the dropdown.
1. Select the Item and enter the Rate and Quantity. The default Tax for that
   Item will be fetched, you can change it here if you want.
1. Click on Save. Ledger entries will be created to increase the amount in
   Accounts Payable.

### Recording payments against Bills

When it's time to record the payment, you can open the relevant Bill from
Purchases > Bills then follow these steps.

1. Click on Menu > Make Payment.
1. Enter the Payment Method, Date and click on Save. This will now reduce the
   amount from Accounts Payable and the amount from your Bank Account will be
   updated.

### Recording Expenses

When you have expenses that you pay at the time of purchase, you can record an
Expense directly using Journal Entry.

1. Go to Purchases > Journal Entry and click on the blue plus button. A Journal
   Entry form will open.
1. Here you will have to make at least two entries, one for Debit and one for
   Credit. Let’s say you incur an expense of ₹5,000 for traveling to a client
   site, and you paid it directly from your Bank Account, then you must do the
   following entries:

| Account         | Debit  | Credit |
| --------------- | ------ | ------ |
| Bank Account    |        | ₹5,000 |
| Travel Expenses | ₹5,000 |        |

When you are making a Journal Entry, you must ensure that the total amount in
the Debit column should equal the total amount in the Credit column.

After you Save and Submit the Journal Entry, Frappe Books will do the necessary
ledger entries. You can check the entries from Menu > Ledger Entries.
