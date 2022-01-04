import os
import numpy as np
import pandas as pd


def read_missing_df():
    if not os.path.exists('./data/bank-missing.csv'):
        raw_df = pd.read_csv('./data/bank.csv')
        rng = np.random.RandomState(42)
        data_missing = raw_df.copy(deep=True)
        for col in data_missing.columns:
            if rng.rand(1) > 0.5:
                frac = rng.uniform(low=0.0, high=0.2, size=1)[0]
                data_missing.loc[data_missing.sample(frac=frac, random_state=42).index, col] = np.nan
        data_missing.to_csv('./data/bank-missing.csv', index=False)
    return pd.read_csv('./data/bank-missing.csv')

