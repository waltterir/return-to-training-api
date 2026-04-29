from sqlmodel import Session, select
from app.models.models import CheckIn, CheckInCreate, CheckInRead

def create_check_in(db: Session, check_in: CheckInCreate) -> CheckIn:
    db_check_in = CheckIn.model_validate(check_in)
    db.add(db_check_in)
    db.commit()
    db.refresh(db_check_in)
    return db_check_in
