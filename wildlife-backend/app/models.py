from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
import datetime
import enum
from .database import Base

class UserRole(str, enum.Enum):
    RESEARCHER = "Wildlife Researcher"
    CONSERVATION_OFFICER = "Conservation Officer"
    FOREST_OFFICER = "Forest Department Officer"
    ADMIN = "Administrator"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.RESEARCHER)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class MonitoringSite(Base):
    __tablename__ = "monitoring_sites"

    id = Column(Integer, primary_key=True, index=True)
    site_name = Column(String, nullable=False)
    protected_area = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)