import matplotlib.pyplot as plt
import pandas as pd
from utils import load_and_prepare_data

df = load_and_prepare_data(r"\Users\shrut\OneDrive\Desktop\sales-intelligence-challenge\data\skygeni_sales_data.csv")

# Win rate by deal stage
stage_win_rate = df.groupby('deal_stage')['won_flag'].mean()
stage_win_rate.plot(kind='bar', title="Win Rate by Deal Stage")
plt.show()

# Win rate by lead source
lead_win_rate = df.groupby('lead_source')['won_flag'].mean()
lead_win_rate.plot(kind='bar', title="Win Rate by Lead Source")
plt.show()

# Sales cycle vs win rate
df['cycle_bin'] = pd.qcut(df['sales_cycle_days'], q=5)
cycle_win_rate = df.groupby('cycle_bin', observed=True)['won_flag'].mean()
cycle_win_rate.plot(kind='bar', title="Win Rate by Sales Cycle Length")
plt.show()

# Deal amount vs win rate
df['amount_bin'] = pd.qcut(df['deal_amount'], q=5)
amount_win_rate = df.groupby('amount_bin', observed=True)['won_flag'].mean()
amount_win_rate.plot(kind='bar', title="Win Rate by Deal Amount")
plt.show()
