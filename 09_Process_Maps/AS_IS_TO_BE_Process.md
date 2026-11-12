# BUSINESS PROCESS ANALYSIS

## 1. AS-IS Process – Existing Workflow

The following AS-IS workflow is an assumed representation of the existing process at the hypothetical organization.

1. Warehouse staff maintain raw material quantities using manual records.
2. Stock records are updated periodically.
3. Procurement identifies material shortages after stock levels become insufficient.
4. Purchase requests are communicated manually to the procurement team.
5. Purchase orders are created and tracked separately.
6. Received materials are manually recorded in inventory records.

### 1.1 Identified Process Bottlenecks

- **Delayed stock visibility:** Periodic updates may not reflect current inventory levels.
- **Inventory discrepancies:** Manual recordkeeping can result in differences between recorded and actual stock.
- **Reactive procurement:** Purchasing activities begin after shortages are identified.
- **Limited purchase order tracking:** Procurement information is maintained separately.
- **Production risk:** Delayed replenishment can affect raw material availability for production.

## 2. TO-BE Process – Proposed Odoo Workflow

The proposed workflow uses Odoo Inventory and Purchase to connect stock monitoring, replenishment and procurement activities.

1. Create and maintain raw material product records in Odoo Inventory.
2. Configure minimum and maximum stock levels through reordering rules.
3. Monitor product availability using inventory records.
4. Identify products requiring replenishment through the replenishment screen.
5. Review the replenishment quantity and generate a Request for Quotation (RFQ).
6. Confirm the RFQ to create a Purchase Order (PO).
7. Receive purchased materials through warehouse receipt operations.
8. Validate the goods receipt to update inventory quantities.

### 2.1 TO-BE Process Flow

```text
Product Configuration
        |
        v
Reordering Rule Configuration
        |
        v
Stock Monitoring
        |
        v
Replenishment Requirement Identified
        |
        v
Review Replenishment Proposal
        |
        v
Generate RFQ
        |
        v
Confirm Purchase Order
        |
        v
Receive Materials
        |
        v
Validate Goods Receipt
        |
        v
Inventory Quantity Updated
```

**Process Note:** The demonstrated reordering rule uses a Manual trigger. Therefore, the replenishment proposal is reviewed and ordered by the user; the system does not automatically create and confirm a purchase order.

## 3. Demonstrated Business Scenario – Steel Sheets

The following scenario was executed in the local Odoo environment using sample transaction data.

| Parameter | Quantity |
|---|---:|
| Initial inventory | 100 units |
| Minimum stock level | 20 units |
| Maximum stock level | 100 units |
| Simulated consumption | 85 units |
| Remaining stock | 15 units |
| Replenishment proposal | 85 units |
| Confirmed purchase quantity | 85 units |
| Final inventory | 100 units |

### 3.1 Scenario Execution

1. An initial purchase of 100 Steel Sheets was received and validated.
2. A reordering rule was configured with a minimum quantity of 20 and maximum quantity of 100.
3. An inventory adjustment simulated consumption of 85 units, reducing stock from 100 to 15.
4. Odoo identified the product for replenishment because available stock was below the minimum threshold.
5. A replenishment proposal for 85 units was generated.
6. The proposal was used to create an RFQ, which was confirmed as a Purchase Order.
7. The receipt of 85 units was validated.
8. The final inventory quantity was verified as 100 units.

## 4. AS-IS vs TO-BE Process Comparison

| Process Area | AS-IS – Assumed | TO-BE – Odoo |
|---|---|---|
| Stock records | Manual records | Centralized product and stock records |
| Stock monitoring | Periodic checking | Inventory visibility in Odoo |
| Replenishment | Reactive identification | Replenishment proposal based on configured thresholds |
| Purchase requests | Manual communication | RFQ creation through Purchase |
| Purchase tracking | Separate records | Centralized RFQ and PO records |
| Goods receipt | Manual recording | Validated warehouse receipt |
| Stock updates | Manual updates | Inventory updated through receipt validation |

## 5. Process Outcome

The demonstrated Odoo workflow connects inventory replenishment with purchasing and goods receipt operations.

The Steel Sheets scenario verified that a replenishment requirement could be identified when stock fell below the configured minimum level, converted into an RFQ and Purchase Order, and completed through goods receipt validation.

This provides a structured approach to raw material replenishment and improves process traceability within the demonstrated scope.

**Limitations:** The AS-IS workflow is hypothetical, and no actual business performance improvement was measured. The Odoo execution demonstrates a sample workflow rather than a production deployment.
