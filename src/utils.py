import pandas as pd

def load_and_prepare_data(path):
    df = pd.read_csv(path)

    df['created_date'] = pd.to_datetime(df['created_date'])
    df['closed_date'] = pd.to_datetime(df['closed_date'])

    df['won_flag'] = (df['outcome'] == 'Won').astype(int)
    return df
