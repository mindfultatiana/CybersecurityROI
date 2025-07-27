# Cybersecurity ROI Metrics Application
The calculator allows you to get the estimated savings for preventing data breaches. This way you can report it to your executive team or board of directors. It also outputs a dashboard report with visual representations. Showing the financial value of cybersecurity gives IT and other departments credibility for their efforts. This helps with budgetary requirements, which can often be a hard sell. Right now the python script is set up with sample industry data for a mid-size renewable energy utility. The output of that data is listed below. Change the values you need to update it properly. 

View the [Realistic Example Values](https://github.com/mindfultatiana/CybersecurityROI/blob/main/README.md#realistic-example-values) section below to get a list of what you may want to update. 

I've also included the [Information to Gather](https://github.com/mindfultatiana/CybersecurityROI/edit/main/README.md#information-to-gather) section with questions that can be used to help fill in the values. 

<img width="1914" height="1014" alt="Screenshot 2025-07-26 223515" src="https://github.com/user-attachments/assets/13bc0074-1d1c-47a7-9385-db3ff36d6a48" />

## Realistic Example Values:
For a mid-sized renewable energy utility:
- Attack Surface Size: 2,500 endpoints
- Zero Trust Effectiveness: 75% (0.75)
- Custom Breach Cost: $8,000,000
- Asset Criticality: 2.0 (high criticality)
- Downtime Hours: 24 hours

The program will handle all the complex calculations and generate professional charts and metrics using these inputs. You can also run multiple scenarios by adjusting these parameters to show best-case, worst-case, and most likely outcomes for the executive presentation.

### Input Explanation
1. *Attack Surface Size (integer)*
- Number of critical endpoints, systems, or high-value assets
- Examples: servers, SCADA systems, IoT devices, workstations
- Typical range: 500-5,000 for utilities

2. *Zero Trust Effectiveness Rate (decimal 0.0-1.0)*
- Estimated risk reduction percentage from zero trust implementation
- Example: 0.75 = 75% risk reduction
- Typical range: 0.60-0.90

3. *Custom Breach Cost (dollar amount, optional)*
- Client's estimated cost per cybersecurity breach
- If not provided, uses industry benchmark ($6.45M for energy sector)
- Should include: incident response, recovery, legal, regulatory fines

4. *Asset Criticality Score (decimal 1.0-3.0, optional)*
Multiplier for how critical the client's assets are
- 1.0 = standard criticality
- 2.0 = high criticality (default for utilities)
- 3.0 = extremely critical infrastructure

5. *Average Downtime Hours (integer, optional)*
- Expected hours of operational downtime per breach
- Default: 24 hours
- Critical for utilities due to service continuity requirements

## Example Output
```
=== CYBERSECURITY ROI CALCULATOR FOR RENEWABLE ENERGY UTILITIES ===

This calculator provides executive-ready metrics for board presentations.

📊 EXECUTIVE SUMMARY - MONTHLY CYBERSECURITY ROI
============================================================
Estimated breaches prevented this month: 0.086
Confidence range: 0.064 - 0.112

💰 FINANCIAL IMPACT BREAKDOWN
----------------------------------------
Direct Breach Costs: $690,000
Operational Downtime: $103,500
Regulatory Compliance: $103,500
Reputation Protection: $207,000

🎯 TOTAL ESTIMATED SAVINGS: $1,104,000
Savings range: $817,600 - $1,434,463

📈 ROI METRICS
----------------------------------------
Estimated monthly ZT investment: $62,500
ROI ratio: 17.7x return on investment
Cost efficiency: $0.06 spent per dollar saved

📋 EXECUTIVE SUMMARY TABLE
==================================================
                       Metric      Value
 Breaches Prevented (Monthly)      0.086
       Total Financial Impact $1,104,000
   Direct Breach Cost Savings   $690,000
 Operational Downtime Savings   $103,500
Regulatory Compliance Savings   $103,500
  Reputation Protection Value   $207,000
Zero Trust Monthly Investment    $62,500
   Return on Investment Ratio      17.7x
        Cost Per Dollar Saved      $0.06


🎯 SCENARIO ANALYSIS
============================================================

--- Conservative Scenario ---

🔍 SCENARIO ANALYSIS
Attack Surface: 1,500 endpoints
ZT Effectiveness: 60.0%
Asset Criticality: 1.0x
Breaches Prevented: 0.021
Total Savings: $218,437
ROI Ratio: 5.8x

--- Current Baseline Scenario ---

🔍 SCENARIO ANALYSIS
Attack Surface: 2,500 endpoints
ZT Effectiveness: 75.0%
Asset Criticality: 2.0x
Breaches Prevented: 0.086
Total Savings: $910,153
ROI Ratio: 14.6x

--- Optimistic Scenario ---

🔍 SCENARIO ANALYSIS
Attack Surface: 3,500 endpoints
ZT Effectiveness: 85.0%
Asset Criticality: 2.5x
Breaches Prevented: 0.171
Total Savings: $1,805,137
ROI Ratio: 20.6x


📊 READY FOR EXECUTIVE PRESENTATION
==================================================
This analysis provides:
✅ Quantified breach prevention metrics
✅ Comprehensive financial impact assessment
✅ Confidence intervals for risk management
✅ Industry-specific cost considerations
✅ Visual dashboard for board presentations
✅ Scenario analysis for strategic planning
```

## Executive Friendly Features

It includes Executive friendly visualizations, and has multiple dimensions of value beyond just breach prevention with the following elements:

#### Industry-Specific Focus: 
Added renewable energy utility benchmarks including
- Operational downtime costs (critical for utilities)
- Regulatory compliance considerations
- Reputation damage factors.

#### Comprehensive Cost Model: 
- Direct breach costs
- Operational downtime costs
- Regulatory compliance savings
- Reputation protection value

#### Statistical Rigor: 
- Added confidence intervals using Monte Carlo simulation to provide more credible estimates for executive presentations.

#### Executive-Ready Visualizations: 
- Savings breakdown pie chart
- Confidence interval visualization
- Cumulative savings projection
- ROI comparison charts

#### Enhanced Methodology:
- Baseline risk calculation based on attack surface size
- Asset criticality scoring
- ROI metrics calculation
- Scenario analysis capabilities

#### Professional Reporting: 
- Generated executive summary tables and comprehensive monthly reports suitable for board presentations.

## Information to Gather

### Infrastructure Assessment:
- How many servers, endpoints, and IoT devices do they have?
- What are their most critical systems (generation, distribution, control systems)?
- How many employees have network access?

### Current Security Posture:
- What security measures are currently in place?
- Have they experienced any incidents in the past?
- What's their current cybersecurity budget?

### Business Impact Understanding:
- What does an hour of downtime cost them in lost revenue?
- What regulatory requirements do they face (NERC CIP, etc.)?
- How would a breach affect customer trust and reputation?

### Zero Trust Implementation Plan:
- What level of zero trust implementation are they considering?
- Timeline for rollout?
- Expected effectiveness based on their specific environment?


