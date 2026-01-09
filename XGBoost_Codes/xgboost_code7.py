# Predict Probabilities

from xgboost import XGBClassifier
from sklearn.datasets import load_iris

x, y = load_iris(return_X_y=True)
model = XGBClassifier()
model.fit(x, y)

print(model.predict_proba([x[0]]))

# output
# [[9.9680281e-01 2.3831055e-03 8.1413286e-04]]]
