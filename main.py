from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np
import os

# --- 1. Load the Model and Scaler ---
MODEL_PATH = 'best_dengue_model.joblib'
SCALER_PATH = 'scaler.joblib'

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")
if not os.path.exists(SCALER_PATH):
    raise FileNotFoundError(f"Scaler file not found at: {SCALER_PATH}")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Model and Scaler loaded successfully!")
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    raise RuntimeError("Failed to load ML model dependencies.")

# --- 2. Initialize FastAPI App ---
app = FastAPI(
    title="Dengue Fever Prediction API",
    description="API for predicting 2024 dengue cases based on 2023 cases.",
    version="1.0.0",
)

# --- 3. Add CORS Middleware ---
origins = ["*"] # Allows all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 4. Define Pydantic Model for Request Body ---
class PredictionInput(BaseModel):
    cases_2023: float = Field(
        ...,
        gt=0,
        le=50000,
        description="Sum of dengue cases in 2023 (positive float, max 50,000)",
        example=5000.0
    )

# --- 5. Create API Endpoint ---
@app.post("/predict", response_model=float, summary="Predict 2024 Dengue Cases")
async def predict_dengue_cases(input_data: PredictionInput):
    """
    Predicts the sum of dengue cases for 2024 based on the sum of cases in 2023.
    """
    try:
        cases_2023_value = input_data.cases_2023
        input_array = np.array([[cases_2023_value]])
        scaled_input = scaler.transform(input_array)
        prediction = model.predict(scaled_input)[0]
        return max(0.0, round(prediction))
    except Exception as e:
        print(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error during prediction: {e}")

@app.get("/", summary="Health Check")
async def read_root():
    return {"message": "Dengue Prediction API is running!"}
