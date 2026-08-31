from fastapi import APIRouter, HTTPException, status
from contextlib import asynccontextmanager
import joblib
from app.Backend.schemas.prediction import UserEntrySchema


ml_models = {}

@asynccontextmanager
async def router_lifespan(router: APIRouter):
    try:
        model_path = "ML/analysis/optimized_house_price_pipeline.pkl"
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

    return {"status": "success", "message": "Model is ready to predict!"}