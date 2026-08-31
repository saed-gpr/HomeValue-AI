from fastapi import APIRouter, HTTPException, status
from contextlib import asynccontextmanager
import joblib
import pandas as pd
import numpy as np
from schemas.prediction import UserEntrySchema


ml_models = {}

@asynccontextmanager
async def router_lifespan(router: APIRouter):
    try:
        model_path = "ML/artifacts/model_training_pipeline.pkl"
        ml_models['house_predictor'] = joblib.load(model_path)
        print('success!')
    except Exception as e:
        print(f'Error : {e}')

    yield

    ml_models.clear()
    print('Memory is clean')


router = APIRouter(
    prefix='/prediction',
    tags=['predict'],
    lifespan=router_lifespan
)

# predict 
@router.post('/')
def predict(data: UserEntrySchema):
    model = ml_models.get('house_predictor')

    if model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail= "The model is unavailable"
            )

    try:

        input_dict = data.model_dump()

        df = pd.DataFrame([input_dict])

        training_features = [
            'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 
            'YearBuilt', 'FullBath', 'TotRmsAbvGrd', 'GarageArea'
        ]

        df = df[training_features]

        log_prediction = model.predict(df)

        actual_price = np.expm1(log_prediction).item()

        return{
            "status" : "success",
            "predicted_price" : round(actual_price, 2)
        }

    except Exception as e:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail= f'Prediction error : {str(e)}'
        )