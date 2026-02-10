Part 1 – Problem Framing
1. What is the real business problem?

The core business problem is not just a declining win rate, but a lack of visibility into why deals are being lost despite a healthy pipeline volume.

This suggests that while enough deals are being created, there may be issues related to:

Deal quality

Sales execution

Targeting of the right customers

Inefficiencies at specific pipeline stages

The CRO does not have clear, data-driven answers to identify where the pipeline is breaking down and what actions the sales organization should prioritize to reverse the trend.

2. What key questions should an AI system answer for the CRO?

An effective AI-driven sales intelligence system should help answer:

Which factors (industry, region, lead source, product, sales rep) are most strongly associated with wins and losses?

Are deals being lost early in the pipeline or late in the closing stages?

Are certain sales reps, regions, or lead sources underperforming relative to others?

Are longer deal cycles correlated with higher loss rates?

Which current or future deals are most at risk, and why?

These answers should enable the CRO to move from reactive monitoring to proactive decision-making.

3. What metrics matter most for diagnosing win rate issues?

Beyond overall win rate, the following metrics are critical:

Win rate by segment (industry, region, lead source, product type)

Stage-level conversion rates to identify pipeline leakage

Average deal size vs win rate to understand quality vs volume trade-offs

Deal cycle length (time from creation to close) and its relationship to outcomes

Sales rep performance consistency, not just total wins

These metrics help isolate whether the issue is driven by market targeting, process inefficiencies, or execution gaps.

4. Key assumptions about the data and business

The analysis makes the following assumptions:

Deal outcomes (won/lost) are accurately recorded

Pipeline stages are applied consistently across deals and sales reps

Historical data reflects current sales motion and strategy

All deals follow a broadly similar lifecycle, making comparisons meaningful

If any of these assumptions are violated, insights and recommendations may be biased or incomplete.


# Sales Intelligence Challenge – SkyGeni

## How to Run (VS Code)

1. Install dependencies:
```bash
pip install -r requirements.txt

2. Run EDA:
python src/eda.py

3. Run Metrics:
python src/metrics.py

4. Run Decision Engine:
python src/decision_engine.py


