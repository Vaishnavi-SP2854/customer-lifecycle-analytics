import pandas as pd
import numpy as np

def add_features(df):
    df = df.copy()

    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 30, 45, 60, 100],
        labels=["Young", "Mid-Age", "Senior", "Elder"]
    )

    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 2, 5, 10, 50],
        labels=["New", "Early", "Established", "Loyal"]
    )

    df["high_balance_flag"] = (
        df["balance"] > df["balance"].median()
    ).astype(int)

    df["engagement_score"] = (
        df["is_active_member"] +
        df["has_credit_card"] +
        (df["complain"] == 0).astype(int)
    )

    df["low_satisfaction_flag"] = (
        df["satisfaction_score"] <= 2
    ).astype(int)

    df["single_product_flag"] = (
        df["numofproducts"] == 1
    ).astype(int)

    return df
