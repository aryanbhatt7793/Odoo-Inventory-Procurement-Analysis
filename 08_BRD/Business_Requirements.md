# BUSINESS REQUIREMENTS DOCUMENT (BRD)

## Project Information

| Field | Details |
|---|---|
| Project | Inventory & Procurement Process Improvement |
| Client | Apex Components Pvt. Ltd. (Hypothetical) |
| Industry | Automotive Component Manufacturing |
| ERP Platform | Odoo Community Edition |
| Modules | Inventory and Purchase |
| Project Type | Functional Analysis Case Study |

## 1. Business Background

Apex Components Pvt. Ltd. is a hypothetical automotive component manufacturer that uses raw materials such as steel sheets, aluminium rods and copper wire in its production processes.

For this case study, the existing business process is assumed to rely on manual inventory records and reactive procurement activities. These practices can lead to stock discrepancies, delayed purchasing decisions and potential production interruptions.

## 2. Business Problem

The assumed business challenges include:

- Inventory quantities are not consistently updated.
- Raw material shortages may be identified late.
- Procurement requests are initiated reactively rather than through planned replenishment.
- Purchase order tracking lacks centralized visibility.
- Incoming material records are not consistently synchronized with inventory records.

## 3. Business Objectives

The project aims to:

- Improve visibility of raw material stock levels.
- Establish minimum and maximum inventory thresholds.
- Identify products that require replenishment.
- Standardize vendor and purchasing workflows.
- Ensure inventory quantities are updated after goods receipt validation.

## 4. Business Requirements

| ID | Requirement | Priority |
|---|---|---|
| BR-01 | Maintain product and inventory records. | High |
| BR-02 | Configure minimum and maximum stock levels. | High |
| BR-03 | Identify products requiring replenishment. | High |
| BR-04 | Generate purchase requests for quotation (RFQs). | High |
| BR-05 | Confirm purchase orders. | High |
| BR-06 | Validate incoming goods receipts. | High |
| BR-07 | Update inventory quantities after receipt validation. | High |

## 5. Project Scope

### 5.1 In Scope

- Inventory product configuration
- Vendor management
- Reordering rule configuration
- Replenishment identification
- RFQ generation
- Purchase order confirmation
- Goods receipt validation
- Stock quantity verification

### 5.2 Out of Scope

- Manufacturing execution
- Accounting implementation
- Sales management
- Custom module development
- External supplier system integration

## 6. Expected Business Benefits

The proposed Odoo workflows are expected to provide:

- Improved inventory visibility.
- More structured procurement coordination.
- Better control over stock replenishment.
- Improved purchase order traceability.
- Reduced reliance on manual inventory tracking.

*Note: These are expected benefits of the proposed process, not measured business results.*

## 7. Assumptions and Constraints

- Apex Components Pvt. Ltd. is a hypothetical organization created for this case study.
- Existing operational problems and the AS-IS workflow are assumed for analysis purposes; they are not based on an actual company audit.
- Odoo Community Edition is used in a local environment.
- Product, vendor and transaction records are sample data created for demonstration.
- Functional testing is limited to the inventory and procurement workflow demonstrated in Odoo.

## 8. Acceptance Criteria

The proposed workflow is considered functionally demonstrated when:

1. Products and vendors can be maintained in Odoo.
2. Minimum and maximum stock thresholds can be configured.
3. Low-stock products can be identified through the replenishment screen.
4. A replenishment proposal can generate an RFQ.
5. An RFQ can be confirmed as a purchase order.
6. An incoming goods receipt can be validated.
7. The received quantity is reflected in the updated inventory balance.
