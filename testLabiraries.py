from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

x, y = make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=10, random_state=42)

import pandas as pd

pd.DataFrame(x).to_csv("datayousif.csv", index=False)