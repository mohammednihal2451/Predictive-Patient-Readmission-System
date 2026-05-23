import joblib

model = joblib.load(
    'patient_readmission_model.pkl'
)

print("Model Loaded Successfully")