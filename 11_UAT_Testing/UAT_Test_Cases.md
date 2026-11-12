\# USER ACCEPTANCE TESTING (UAT)



\## Test Environment

\- ERP: Odoo Community Edition

\- Modules: Inventory and Purchase

\- Test Product: Steel Sheets

\- Test Vendor: Metro Steel Suppliers



\## Test Scenarios



| Test ID | Test Scenario | Expected Result | Actual Result |

|---|---|---|---|

| TC-01 | Create raw material product | Product record created | Pass |

| TC-02 | Create vendor | Vendor record created | Pass |

| TC-03 | Receive initial purchase of 100 units | Stock becomes 100 | Pass |

| TC-04 | Configure reordering rule | Min 20, Max 100 saved | Pass |

| TC-05 | Adjust stock from 100 to 15 | Stock becomes 15 | Pass |

| TC-06 | Generate replenishment proposal | 85 units proposed | Pass |

| TC-07 | Confirm purchase order | RFQ converted to PO | Pass |

| TC-08 | Validate goods receipt | Stock becomes 100 | Pass |



\## Detailed Test Scenario: Replenishment



Precondition:

\- Current stock: 15 units

\- Minimum quantity: 20

\- Maximum quantity: 100



Execution:

1\. Open Inventory replenishment.

2\. Identify the Steel Sheets shortage.

3\. Execute replenishment.

4\. Verify the generated RFQ.

5\. Confirm the purchase order.

6\. Validate the incoming goods receipt.



Expected Result:

\- Replenishment quantity: 85 units.

\- Purchase order successfully confirmed.

\- Goods receipt successfully validated.

\- Final stock: 100 units.



\## Test Conclusion



The demonstrated end-to-end replenishment scenario passed validation using the sample Odoo database.



Note: Results apply to the demonstrated Steel Sheets scenario. Other products were created but not independently tested through the full procurement cycle.

