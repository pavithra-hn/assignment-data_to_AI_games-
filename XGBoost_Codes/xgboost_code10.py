# Cross Validation

from xgboost import XGBClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score

x, y = load_iris(return_X_y=True)
model = XGBClassifier()

scores = cross_val_score(model, x, y, cv=5)
print(scores.mean())

# output
# 0.9533333333333334
