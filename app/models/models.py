from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

class IntensityLevel(str, Enum):
    easy = "easy"
    moderate = "moderate"
    hard = "hard"

# --- USER ---

class UserBase(SQLModel):
    email: str

class User(UserBase, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

    check_ins: list["CheckIn"] = Relationship(back_populates="user")
    trainings: list["Training"] = Relationship(back_populates="user")
    recommendations: list["Recommendation"] = Relationship(back_populates="user")

class UserCreate(UserBase):
    pass   

class UserRead(UserBase):
    id: int
    created_at: datetime

# --- CHECK-IN ---

class CheckInBase(SQLModel):
    energy_level: int = Field(ge=1, le=5)
    motivation_level: int = Field(ge=1, le=5)
    stress_level: int = Field(ge=1, le=5)
    sleep_quality: int = Field(ge=1, le=5)
    days_since_last_workout: int = Field(ge=0)
    last_session_intensity: IntensityLevel

class CheckIn(CheckInBase, table=True):
    __tablename__ = "check_ins"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

    user: User = Relationship(back_populates="check_ins")
    recommendations: Optional["Recommendation"] = Relationship(back_populates="check_in")

class CheckInCreate(CheckInBase):
    user_id: int

class CheckInRead(CheckInBase):
    id: int
    user_id: int
    created_at: datetime

# --- TRAINING ---

class TrainingBase(SQLModel):
    training_type: str
    duration_minutes: int
    intensity: int
    rpe: Optional[int] = None
    notes: Optional[str] = None
    completed_at: datetime

class Training(TrainingBase, table=True):
    __tablename__ = "trainings"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user: Optional[User] = Relationship(back_populates="trainings")

class TrainingCreate(TrainingBase):
    user_id: int

class TrainingRead(TrainingBase):
    id: int
    user_id: int
    created_at: datetime

# --- RECOMMENDATION ---

class RecommendationBase(SQLModel):
    recommendation: str
    risk_level: str
    suggested_training: str
    reason: str
    triggered_rules: str

class Recommendation(RecommendationBase, table=True):
    __tablename__ = "recommendations"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    check_in_id: int = Field(foreign_key="check_ins.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user: Optional[User] = Relationship(back_populates="recommendations")
    check_in: Optional[CheckIn] = Relationship(back_populates="recommendations")

class RecommendationCreate(RecommendationBase):
    user_id: int
    check_in_id: int

class RecommendationRead(RecommendationBase):
    id: int
    user_id: int
    check_in_id: int
    created_at: datetime


