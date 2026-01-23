# Save & Load Model

from xgboost import XGBClassifier
import joblib

model = XGBClassifier()
joblib.dump(model, "xgb.pkl")

model2 = joblib.load("xgb.pkl")
print("Model Loaded")

# output
# Model Loaded
