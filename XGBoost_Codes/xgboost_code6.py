# Regression with Evaluation

from xgboost import XGBRegressor
from sklearn.datasets import make_regression

x, y = make_regression()
model = XGBRegressor()
model.fit(x, y, eval_set=[(x, y)], verbose=False)

print("Training done")

# output
# Training done
