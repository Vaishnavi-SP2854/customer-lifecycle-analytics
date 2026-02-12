def calculate_clv(df):
    df = df.copy()
    df["clv"] = df["balance"] + (df["estimatedsalary"] * 0.1)
    return df