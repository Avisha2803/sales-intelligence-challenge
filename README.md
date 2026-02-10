
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

## Exploratory Analysis & Key Insights

### 1. Pipeline Stage Performance
Early pipeline stages (e.g., *Qualified*, *Proposal*) exhibit the lowest win rates.

**Insight:**  
Many deals are entering the pipeline before they are fully qualified.

**Action:**  
Tighten qualification criteria and improve early-stage discovery.

---

### 2. Sales Cycle Length
Deals with longer-than-typical sales cycles are significantly less likely to close successfully.

**Insight:**  
Deal aging is a strong indicator of loss risk.

**Action:**  
Introduce deal aging alerts and proactive review.

---

### 3. Deal Size & Lead Source
Win rates remain relatively stable across deal sizes and lead sources.

**Insight:**  
Win-rate decline is not driven by deal size strategy or lead channels.

**Action:**  
Focus improvement efforts on execution and qualification rather than sourcing.

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



