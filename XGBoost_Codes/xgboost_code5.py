# Train/Test Split


from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.datasets import load_iris

x, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y)

model = XGBClassifier()
model.fit(x_train, y_train)

print(model.score(x_test, y_test))

# output
# 0.9736842105263158
