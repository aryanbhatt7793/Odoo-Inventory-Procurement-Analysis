# INVENTORY & PROCUREMENT PROCESS IMPROVEMENT

## Odoo ERP Functional Analysis Case Study

**Client:** Apex Components Pvt. Ltd. (Hypothetical)  
**Industry:** Automotive Component Manufacturing  
**ERP Platform:** Odoo Community Edition  
**Modules:** Inventory and Purchase  
**Project Type:** Functional Analysis Case Study

---

## 1. Executive Summary

This project demonstrates how Odoo ERP can support improved inventory visibility and procurement coordination for a hypothetical automotive component manufacturer.

The case study involved analyzing an assumed manual inventory and procurement process, identifying functional gaps, and configuring standard Odoo Inventory and Purchase workflows to support stock monitoring, replenishment, purchasing and goods receipt.

A complete sample replenishment cycle was executed for Steel Sheets to validate the proposed workflow.

## 2. Business Challenge

The assumed existing business process relied on manual stock tracking and reactive procurement activities.

The key business challenges identified were:

- Inconsistent inventory records.
- Delayed identification of raw material shortages.
- Reactive purchasing activities.
- Limited visibility into purchase order status.
- Manual inventory updates following goods receipt.

These challenges formed the basis for the proposed ERP workflow.

## 3. Implemented Solution

The following activities were completed using Odoo Community Edition:

- Created raw material product records for Steel Sheets, Aluminium Rods and Copper Wire.
- Created sample supplier records.
- Configured minimum and maximum inventory thresholds for Steel Sheets.
- Simulated stock consumption through an inventory adjustment.
- Identified replenishment requirements through the Odoo Replenishment screen.
- Generated an RFQ from the replenishment proposal.
- Confirmed the RFQ as a Purchase Order.
- Validated the incoming warehouse goods receipt.
- Verified the updated inventory quantity.

**Implementation Note:** The reordering rule used a Manual trigger. The replenishment proposal required user review and action before generating the RFQ.

## 4. Demonstrated Results

The following results were verified during the Steel Sheets replenishment scenario.

| Metric | Demonstrated Result |
|---|---:|
| Initial stock | 100 units |
| Minimum stock level | 20 units |
| Maximum stock level | 100 units |
| Simulated consumption | 85 units |
| Remaining stock | 15 units |
| Replenishment proposal | 85 units |
| Confirmed purchase quantity | 85 units |
| Final stock after receipt | 100 units |

### Transaction Summary

1. Initially received 100 units of Steel Sheets.
2. Configured a reordering rule with a minimum of 20 and maximum of 100 units.
3. Simulated consumption of 85 units, reducing available stock to 15.
4. Generated an 85-unit replenishment proposal.
5. Created and confirmed a Purchase Order for 85 units.
6. Validated the incoming goods receipt.
7. Verified that final stock returned to 100 units.

## 5. Business Value

The configured workflow demonstrates how standard Odoo functionality can support:

- Centralized inventory visibility.
- Structured stock replenishment.
- Better coordination between inventory and procurement activities.
- Improved RFQ and Purchase Order traceability.
- Consistent inventory updates following receipt validation.

These are expected process benefits. No quantified operational savings, reduction in stock discrepancies or real-world production improvements were measured.

## 6. Project Limitations

- Apex Components Pvt. Ltd. is a hypothetical organization.
- Existing business problems and the AS-IS process were assumed for analysis purposes.
- Product, supplier and transaction records use sample data.
- The complete replenishment and procurement cycle was demonstrated only for Steel Sheets.
- Aluminium Rods and Copper Wire were created but not independently tested through the complete procurement cycle.
- Stock consumption was simulated using an inventory adjustment rather than an actual manufacturing transaction.
- Manufacturing, accounting and sales processes were outside the project scope.
- No custom development or external system integration was performed.
- The implementation was conducted in a local Odoo environment, not a live production deployment.

## 7. Tools and Skills

**Tools and Technologies**
- Odoo Community Edition
- Odoo Inventory
- Odoo Purchase
- Microsoft Excel
- GitHub

**Functional and Business Analysis Skills**
- Business Requirement Analysis
- Business Process Mapping (AS-IS / TO-BE)
- Gap Analysis
- Functional Requirement Definition
- ERP Functional Configuration
- Inventory and Procurement Workflow Analysis
- Functional Testing and UAT Documentation

## 8. Conclusion

This case study demonstrates how standard Odoo Inventory and Purchase functionality can support a structured raw material replenishment and procurement process.

By configuring stock thresholds and executing the workflow from replenishment identification to purchase order confirmation and goods receipt validation, the project provides practical evidence of ERP functional configuration and business process analysis.

The exercise also demonstrates the role of a Functional Analyst in translating business requirements into ERP workflows and validating those workflows through structured test scenarios.
