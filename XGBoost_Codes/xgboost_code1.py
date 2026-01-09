# Linear Regression
from xgboost import XGBRegressor
from sklearn.datasets import make_regression

x, y = make_regression(n_samples=100, n_features=1)
model = XGBRegressor()
model.fit(x, y)

print(model.predict([[5]]))
