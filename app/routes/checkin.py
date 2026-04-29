from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database.database import get_db
from ..models.models import CheckInCreate, CheckInRead
from ..services import checkin_services as services

router = APIRouter(prefix="/check-ins", tags=["check-ins"])

@router.post("/", response_model=CheckInRead, status_code=201)
def create_check_in(check_in: CheckInCreate, db: Session = Depends(get_db)):
    return services.create_check_in(db, check_in)



