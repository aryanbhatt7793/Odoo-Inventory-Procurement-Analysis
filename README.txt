# Inventory & Procurement Process Improvement

### Odoo ERP | Functional Analysis Case Study

**Client:** Apex Components Pvt. Ltd. (Hypothetical)  
**Industry:** Automotive Component Manufacturing  
**ERP:** Odoo Community Edition  
**Modules:** Inventory and Purchase  
**Project Type:** ERP Functional Analysis

---

## Project Overview

This project demonstrates how Odoo ERP can support inventory management and procurement process improvement for a hypothetical automotive component manufacturer.

The case study focuses on analyzing an assumed manual inventory process, identifying business and functional gaps, configuring Odoo workflows, and validating the replenishment and procurement cycle.

## Business Problem

The hypothetical organization relies on manual inventory records and reactive procurement activities, resulting in potential challenges such as:

- Inconsistent stock records.
- Delayed identification of material shortages.
- Reactive purchasing activities.
- Limited purchase order visibility.
- Manual inventory updates after goods receipt.

## Proposed Solution

Odoo Community Edition was configured using the Inventory and Purchase applications to demonstrate:

- Raw material product configuration.
- Supplier management.
- Minimum and maximum stock level configuration.
- Replenishment identification.
- Request for Quotation (RFQ) generation.
- Purchase Order confirmation.
- Warehouse goods receipt validation.
- Inventory quantity verification.

## Demonstrated Workflow

```text
Product and Vendor Configuration
              |
              v
     Reordering Rule Setup
              |
              v
        Stock Monitoring
              |
              v
  Replenishment Identification
              |
              v
          RFQ Creation
              |
              v
     Purchase Order Confirmation
              |
              v
       Goods Receipt Validation
              |
              v
       Updated Inventory Stock
```

**Note:** The reordering rule used a Manual trigger. The replenishment proposal required user review and action before an RFQ was generated.

## Demonstrated Results – Steel Sheets

A complete sample replenishment cycle was executed for Steel Sheets.

| Parameter | Result |
|---|---:|
| Initial Stock | 100 units |
| Minimum Stock | 20 units |
| Maximum Stock | 100 units |
| Simulated Consumption | 85 units |
| Remaining Stock | 15 units |
| Replenishment Proposal | 85 units |
| Confirmed Purchase Quantity | 85 units |
| Final Stock | 100 units |

The scenario demonstrated the workflow from low-stock identification through procurement and goods receipt validation.

## Project Documentation

| Document | Description |
|---|---|
| [Business Requirements Document](08_BRD/Business_Requirements.md) | Business background, objectives, requirements and scope |
| [Business Process Analysis](09_Process_Maps/AS_IS_TO_BE_Process.md) | AS-IS and TO-BE workflows and process comparison |
| [Gap Analysis](10_Gap_Analysis/Gap_Analysis.md) | Existing process gaps and proposed Odoo functionality |
| [UAT Test Cases](11_UAT_Testing/UAT_Test_Cases.md) | Functional test scenarios and execution results |
| [Project Summary](12_Final_Report/Project_Summary.md) | Implementation overview, results and limitations |
| [Detailed Project Report (PDF)](Apex_Components_Project_Report.pdf) | Consolidated project documentation |

## Implementation Evidence

Screenshots from the local Odoo environment are available in:

[`06_Odoo_Screenshots`](06_Odoo_Screenshots/)

The screenshots provide evidence of the configured reordering rule, simulated inventory adjustment and low-stock identification.

## Tools and Skills

**Tools**
- Odoo Community Edition
- Odoo Inventory
- Odoo Purchase
- Microsoft Excel
- GitHub

**Skills**
- Business Requirement Analysis
- AS-IS / TO-BE Process Mapping
- Gap Analysis
- ERP Functional Configuration
- Inventory and Procurement Workflow Analysis
- Functional Testing
- UAT Documentation

## Project Scope and Limitations

- Apex Components Pvt. Ltd. is a hypothetical organization.
- Business problems and the existing AS-IS workflow are assumed for analysis.
- Sample product, supplier and transaction data were used.
- The complete procurement cycle was demonstrated for Steel Sheets only.
- Stock consumption was simulated through an inventory adjustment.
- Manufacturing, accounting and sales implementation were excluded.
- No custom development or external integrations were performed.
- The implementation was performed in a local Odoo environment, not a live production deployment.

## Conclusion

This case study demonstrates the application of Odoo Inventory and Purchase functionality to a structured raw material replenishment and procurement process.

It provides practical evidence of business requirement analysis, process mapping, functional configuration and workflow testing in an ERP environment.
