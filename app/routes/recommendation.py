from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database.database import get_db
from ..models.models import RecommendationRead
from ..services import recommendation_services as services

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

@router.post("/{check_in_id}", response_model=RecommendationRead, status_code=201)
def create_recommendation(check_in_id: int, db: Session = Depends(get_db)):
    return services.create_recommendation(db, check_in_id)