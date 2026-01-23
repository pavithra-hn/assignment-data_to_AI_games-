#  Binary Classification

from sklearn.datasets import make_classification
from xgboost import XGBClassifier

x, y = make_classification()
model = XGBClassifier()
model.fit(x, y)

print(model.predict(x[:5]))

# output
# [1 1 0 0 1]
