# Early Stopping

from xgboost import XGBClassifier
from sklearn.datasets import load_iris

x, y = load_iris(return_X_y=True)
# Pass early_stopping_rounds to the constructor
model = XGBClassifier(n_estimators=100, early_stopping_rounds=5)

model.fit(x, y, eval_set=[(x, y)], verbose=False)

print("Training done with early stopping")

#  output
# Training done with early stopping
