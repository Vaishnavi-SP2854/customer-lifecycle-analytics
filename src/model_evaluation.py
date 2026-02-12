from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

def prepare_data(df):
    X = df.drop("churn", axis=1)
    y = df["churn"]

    X_encoded = pd.get_dummies(X, drop_first=True)

    return train_test_split(
        X_encoded, y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model