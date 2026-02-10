
# Sales Intelligence Analysis & Decision Engine

## Overview

This project analyzes historical B2B SaaS sales data to understand a decline in win rate despite a healthy pipeline.  
The goal is to move beyond surface-level metrics and build a lightweight, interpretable decision-support system that helps sales leaders identify risk early and take corrective action.

The focus is on **business reasoning**, **actionable insights**, and **decision intelligence**, rather than complex machine learning models.

---

## Dataset Summary

The analysis is based on **5,000 closed sales deals**, each representing a complete sales cycle.

**Key fields include:**
- Deal lifecycle information (created date, closed date, stage)
- Commercial attributes (deal amount, product, region)
- Sales process signals (sales cycle length, lead source)
- Final outcome (Won / Lost)

### Data Quality Notes
- No missing values observed
- Balanced outcomes (~45% Won, ~55% Lost)
- Realistic distributions for deal size and sales cycle duration

---

## Problem Understanding

Although pipeline volume remains strong, declining win rate indicates inefficiencies elsewhere in the sales process.  
The key challenge is identifying **where deals are breaking down** and **which opportunities require immediate attention**.

This project focuses on:
- Understanding pipeline leakage
- Identifying deal-level risk signals
- Enabling proactive sales intervention

---

## Exploratory Data Analysis (EDA) Results

The following insights were derived from exploratory analysis of the sales dataset.  
Each analysis focuses on understanding drivers of win rate and identifying areas for improvement.

---

### Win Rate by Deal Stage

The analysis shows a clear variation in win rate across pipeline stages.

<img width="1898" height="981" alt="image" src="https://github.com/user-attachments/assets/d46d5c65-7930-447d-aa6c-bde8ab41df8d" />



**Observation:**
- Early stages such as *Qualified* and *Proposal* exhibit the lowest win rates
- Win rate improves as deals move closer to closure

**Interpretation:**
This indicates that a large number of deals are entering the pipeline without sufficient qualification, inflating pipeline volume but reducing overall conversion.

**Business Impact:**
Sales teams may be spending significant effort on low-quality opportunities.

**Recommended Action:**
- Tighten qualification criteria at early stages
- Improve discovery and validation before advancing deals

---

### Win Rate by Lead Source

Win rates across different lead sources remain relatively similar.

<img width="1898" height="986" alt="image" src="https://github.com/user-attachments/assets/df54a4fe-415d-47dc-91e7-8d0d3c695905" />



**Observation:**
- No lead source significantly outperforms or underperforms the others
- Performance differences are marginal

**Interpretation:**
The decline in win rate is unlikely to be driven by lead acquisition channels.

**Business Impact:**
Marketing and lead generation strategies are not the primary bottleneck.

**Recommended Action:**
- Maintain current lead mix
- Shift focus toward pipeline execution and deal management

---

### Sales Cycle Length vs Win Rate

Deals were grouped into bins based on sales cycle duration.

<img width="1884" height="981" alt="image" src="https://github.com/user-attachments/assets/4b3881c7-1e0c-4aa8-a666-498fb62f2059" />



**Observation:**
- Shorter sales cycles show higher win rates
- Win rate declines as sales cycle length increases

**Interpretation:**
Long-running deals are more likely to stall or lose momentum, increasing the probability of loss.

**Business Impact:**
Deal aging is a strong early warning signal for sales risk.

**Recommended Action:**
- Introduce deal aging alerts
- Trigger intervention for deals exceeding typical cycle length

---

### Deal Amount vs Win Rate

Deal amounts were segmented into equal-sized bins.

<img width="1896" height="981" alt="image" src="https://github.com/user-attachments/assets/2df6f1ca-8198-429c-952d-2a29063bb78e" />



**Observation:**
- Win rate remains relatively stable across deal sizes
- Larger deal sizes do not significantly reduce win probability

**Interpretation:**
Pursuing higher-value deals does not inherently harm win rate.

**Business Impact:**
Revenue strategy is not constrained by deal size but by execution quality.

**Recommended Action:**
- Continue pursuing higher-value opportunities
- Ensure adequate sales support for complex deals

---

### Summary of EDA Findings

- Early-stage pipeline quality is a key issue
- Deal aging strongly correlates with loss risk
- Lead source and deal size are not primary contributors to win-rate decline

These insights directly informed the design of custom metrics and the deal risk scoring decision engine.

---

## Custom Metrics

### Pipeline Leakage Rate
Measures the proportion of deals that fail to convert at each pipeline stage.

**Purpose:**  
Identify where the sales process breaks down and where corrective action is needed.

---

### Deal Risk Score
A simple, rule-based score designed to prioritize at-risk deals using:
- Sales cycle length (above median)
- Presence in early pipeline stages

**Validation Result:**

Risk Score → Win Rate
0 → ~46%
1 → ~45%
2 → ~42%


The score is intended for **prioritization**, not precise prediction.

---

## Decision Engine: Deal Risk Scoring

A decision engine was built on top of the risk score to support weekly sales reviews.

### What the System Produces
- A ranked list of **high-risk deals**
- Clear, human-readable explanations for each risk flag

**Example risk reasons:**
- `Long sales cycle`
- `Early pipeline stage`

---

### How Sales Leaders Use It
- Review high-risk deals weekly
- Focus coaching and escalation efforts
- Disqualify low-probability opportunities earlier
- Improve overall pipeline efficiency

This shifts sales operations from **reactive reporting** to **proactive intervention**.

---

## System Design (Conceptual)

In a production setting, the system would operate as:

CRM Data → Daily Processing → Metric Computation → Risk Scoring → Alerts & Insights


### Execution Cadence
- Data ingestion and risk scoring: Daily
- Pipeline health summaries: Weekly
- Alerts triggered by risk thresholds

---

## Limitations

- Relies on structured CRM data only
- Does not capture qualitative factors such as buyer intent or competitive pressure
- Rule-based thresholds require periodic tuning

The system is designed as a **decision aid**, not a fully automated predictor.

---

## Future Improvements

With additional time, the following enhancements could be added:
- Rep-level historical performance modeling
- Segment-specific risk thresholds
- Hybrid rule-based + ML probability scoring
- Feedback loops from sales managers

---

## How to Run the Project

```bash
pip install -r requirements.txt
python src/eda.py
python src/metrics.py
python src/decision_engine.py



