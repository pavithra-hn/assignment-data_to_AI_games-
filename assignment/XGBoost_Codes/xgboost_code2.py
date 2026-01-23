# Classification

from xgboost import XGBClassifier
from sklearn.datasets import load_iris

data = load_iris()
model = XGBClassifier()
model.fit(data.data, data.target)

print(model.predict([data.data[0]]))

# output : 
# [0]
