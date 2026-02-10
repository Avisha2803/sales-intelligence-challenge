from utils import load_and_prepare_data
import matplotlib.pyplot as plt

df = load_and_prepare_data(r"\Users\shrut\OneDrive\Desktop\sales-intelligence-challenge\data\skygeni_sales_data.csv")

# Pipeline Leakage Rate
stage_leakage = df.groupby('deal_stage')['won_flag'].apply(lambda x: 1 - x.mean())
stage_leakage.plot(kind='bar', title="Pipeline Leakage Rate by Stage")
plt.show()

# Deal Risk Score
median_cycle = df['sales_cycle_days'].median()

df['deal_risk_score'] = 0
df.loc[df['sales_cycle_days'] > median_cycle, 'deal_risk_score'] += 1
df.loc[df['deal_stage'].isin(['Qualified', 'Proposal']), 'deal_risk_score'] += 1

print(df.groupby('deal_risk_score')['won_flag'].mean())

# Risk reasons
df['risk_reason'] = ""
df.loc[df['sales_cycle_days'] > median_cycle, 'risk_reason'] += "Long sales cycle; "
df.loc[df['deal_stage'].isin(['Qualified', 'Proposal']), 'risk_reason'] += "Early pipeline stage; "
df['risk_reason'] = df['risk_reason'].str.rstrip("; ")

print(df[['deal_id', 'deal_risk_score', 'risk_reason']].head())
