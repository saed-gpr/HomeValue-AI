# 🚀 Machine Learning Model Deployment with FastAPI & Docker

This repository demonstrates a complete workflow for deploying a Machine Learning model. The model is built and trained using **scikit-learn**, exposed as a fast and robust REST API using **FastAPI**, and fully containerized using **Docker** for easy and consistent deployment across any environment.

## 🛠️ Tech Stack
- **Machine Learning:** scikit-learn, pandas, numpy
- **Backend/API:** FastAPI, Uvicorn
- **Containerization:** Docker


```text
HomeValue-AI
├── ML
│   ├── analysis
│   │   ├── .ipynb_checkpoints
│   │   │   ├── model_training_pipeline-checkpoint.ipynb
│   │   │   └── test-checkpoint.ipynb
│   │   └── model_training_pipeline.ipynb
│   ├── artifacts
│   │   └── model_training_pipeline.pkl
│   └── data
│       └── train.csv
├── app
│   ├── Backend
│   │   ├── __pycache__
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   └── prediction.py
│   │   ├── config.py
│   │   ├── database
│   │   │   ├── __init__.py
│   │   │   ├── connection.py
│   │   │   └── session.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── prediction.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   └── prediction.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   └── prediction.py
│   │   └── utils
│   │       └── preprocessiong.py
│   └── Frontend
│       └── .gitkeep
├── .git
├── .gitignore
├── requirements.txt
├── README.md
└── venv
```
