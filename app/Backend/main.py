from fastapi import FastAPI
from api.prediction import router as prediction_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title='HomeValue-AI API',
    description='API for House Price Prediction',
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(prediction_router)

@app.get('/')
def read_root():
    return {
        'status' : 'active',
        'message' : "Welcome to HomeValue-AI Backend"
    }