# Feature Importance

from xgboost import XGBClassifier
from sklearn.datasets import load_iris

x, y = load_iris(return_X_y=True)
model = XGBClassifier()
model.fit(x, y)

print(model.feature_importances_)

# output
# [0.00959796 0.01645038 0.6765859  0.2973658 ]