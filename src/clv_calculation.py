import pandas as pd

def clean_data(df):
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.rename(columns={
        "exited": "churn",
        "hascrcard": "has_credit_card",
        "isactivemember": "is_active_member"
    })

    df = df.dropna()

    return df

from src.data_preprocessing import clean_data
df = clean_data(df)
