from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from pathlib import Path
import joblib

MODEL_PATH = Path(__file__).parent / 'student_performance_pipeline.pkl'
model = joblib.load(MODEL_PATH)

app = FastAPI(title='Student Performance Predictor')

class InputData(BaseModel):
    Hours_Studied: float
    Previous_Scores: int
    Extracurricular_Activities: str
    Sleep_Hours: int
    Sample_Question_Papers_Practiced: int
    

@app.get('/')
def home():
    return {
        'message': 'Hello Sir, This Model Will Help You To Predict The Performance Of Students'
    }


@app.post('/performance_prediction')
def performance_prediction(data: InputData):
    input_df = pd.DataFrame([{
        'Hours Studied': data.Hours_Studied,
        'Previous Scores': data.Previous_Scores,
        'Extracurricular Activities': data.Extracurricular_Activities,
        'Sleep Hours': data.Sleep_Hours,
        'Sample Question Papers Practiced': data.Sample_Question_Papers_Practiced,
    }])
    
    prediction = model.predict(input_df)
    return {
        'input': input_df.to_dict(orient='records')[0],
        'predicted_value': round(float(prediction[0]), 2)
    }
