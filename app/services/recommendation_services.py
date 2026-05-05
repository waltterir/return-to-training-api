from sqlmodel import Session, select
from fastapi import HTTPException
from ..models.models import Recommendation, RecommendationCreate, RecommendationRead, CheckIn
from ..services.recommendation_engine import run_rules


def create_recommendation(db: Session, check_in_id: int) -> Recommendation:
    check_in = db.get(CheckIn, check_in_id)
    if not check_in:
        raise HTTPException(status_code=404, detail="Check-in not found")
    result = run_rules(check_in)
    db_recommendation = Recommendation.model_validate({
        **result, 
        "user_id": check_in.user_id,
        "check_in_id": check_in_id,
    })
    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)
    return db_recommendation