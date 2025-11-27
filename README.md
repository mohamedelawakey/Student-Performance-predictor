# Student Performance Prediction API

This project provides a Machine Learning–based API for predicting student performance based on multiple academic and behavioral features. The model is packaged into a prediction pipeline and served using FastAPI.

The entire application is containerized with Docker and deployed on HuggingFace Spaces.

---

# 🚀 Features

- Predicts student performance based on:
    - Hours Studied
    - Previous Scores
    - Extracurricular Activities
    - Sleep Hours
    - Sample Question Papers Practiced

- Fully implemented REST API using FastAPI
- Machine Learning model built using Scikit-Learn
- Deployment-ready with Docker
- Hosted on Hugging Face Spaces

---

# 📁 Project Structure
```bash
project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── space.yaml
├── .gitignore
├── data/
│   └── Student_Performance.csv
│
├── model/
│   ├── student_performance_pipeline.pkl
│   └── student_performance_model.pkl
│
└── notebooks/
    └── StudentPerformance.ipynb
```

---

# 🧠 Model

The prediction pipeline was trained using Scikit-Learn and serialized using Joblib for efficient loading inside the API.
The file `student_performance_pipeline.pkl` contains preprocessing + model steps.

**🛠 Technologies Used: **
- Python
- FastAPI
- Scikit-Learn
- Pandas
- Joblib
- Docker
- Hugging Face Spaces

---

# 📡 API Endpoints
- GET /
    - Returns a welcome message.

- POST /performance_prediction
    - Request Body:
        ```json
        {
            "Hours_Studied": 5,
            "Previous_Scores": 80,
            "Extracurricular_Activities": "Yes",
            "Sleep_Hours": 7,
            "Sample_Question_Papers_Practiced": 3
        }
        ```
    - Response:
        ```json
        {
            "input": {...},
            "predicted_value": 88.75
        }
        ```

---

# ▶️ Running Locally
```bash
uvicorn app:app --reload
```

---

# 🐳 Docker Support
**Build and run:**
```bash
docker build -t student-perf .
docker run -p 8000:8000 student-perf
```

---

# 🌐 Deployment

The project is deployed on Hugging Face Spaces.
You can access it here: [Hugging Face Spaces](https://huggingface.co/spaces/mohamedelawakey/student-performance-predictor)

---
