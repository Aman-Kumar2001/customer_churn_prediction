from fastapi import FastAPI
from schema.pydantic_model import Customer
from src.predict import predict_churn
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

@app.get('/')
def home():
    return {'message' : 'This is the home page'}

@app.get('/health')
def health():
    return {"Status" : 'OK'}

@app.post('/predict')
def predict(data: Customer):
    input = data.model_dump()
    input_df = pd.DataFrame([input])

    response = predict_churn(input_df)

    return JSONResponse(content = response, status_code=200)