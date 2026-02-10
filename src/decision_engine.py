from utils import load_and_prepare_data

df = load_and_prepare_data(r"\Users\shrut\OneDrive\Desktop\sales-intelligence-challenge\data\skygeni_sales_data.csv")

# Risk scoring
median_cycle = df['sales_cycle_days'].median()

df['deal_risk_score'] = 0
df.loc[df['sales_cycle_days'] > median_cycle, 'deal_risk_score'] += 1
df.loc[df['deal_stage'].isin(['Qualified', 'Proposal']), 'deal_risk_score'] += 1

# Risk category
def risk_bucket(score):
    if score >= 2:
        return "High Risk"
    elif score == 1:
        return "Medium Risk"
    return "Low Risk"

df['risk_category'] = df['deal_risk_score'].apply(risk_bucket)

# Explainability
df['risk_reason'] = ""
df.loc[df['sales_cycle_days'] > median_cycle, 'risk_reason'] += "Long sales cycle; "
df.loc[df['deal_stage'].isin(['Qualified', 'Proposal']), 'risk_reason'] += "Early pipeline stage; "
df['risk_reason'] = df['risk_reason'].str.rstrip("; ")

# High-risk deals
high_risk_deals = df[df['risk_category'] == "High Risk"] \
    .sort_values('sales_cycle_days', ascending=False)

print("\nTop High-Risk Deals:\n")
print(
    high_risk_deals[
        ['deal_id', 'deal_stage', 'sales_cycle_days', 'deal_amount', 'risk_reason']
    ].head(10)
)
