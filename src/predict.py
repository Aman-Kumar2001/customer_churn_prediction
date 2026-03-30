import joblib
from schema.pydantic_model import Customer

model = joblib.load('artifacts/model.pkl')

def predict_churn(data):
    
    prob = model.predict_proba(data)[0,1]
    prob = float(prob)

    # Risk bands 
    if prob >= 0.30:
        risk_level = "HIGH"
        churn_prediction = 1
        message = "High risk of churn. Immediate action recommended."
    elif prob >= 0.20:
        risk_level = "MEDIUM"
        churn_prediction = 1   
        message = "Moderate churning risk. Review suggested."
    else:
        risk_level = "LOW"
        churn_prediction = 0
        message = "Low churning risk."

    return {
        "churn_probability" : round(prob,3),
        "prediction" : churn_prediction,
        "risk_level" : risk_level,
        "message" : message
    }