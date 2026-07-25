from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session



# Assuming you have these imported from your existing files:
from app.database import get_pg_db, get_mongo_db
from app.models import User
from app.auth import get_password_hash, verify_password, create_access_token
from app.schemas import UserCreate, UserResponse, Token
from .database import pg_engine, Base, get_pg_db, get_mongo_db
from .models import User, MonitoringSite
from .datasets import DatasetIntegrator

# Initialize PostgreSQL Tables
Base.metadata.create_all(bind=pg_engine)

app = FastAPI(title="Wildlife Population Intelligence System API")
@app.get("/", tags=["Health Check"])
def root():
    return {"status": "Online", "message": "Wildlife Intelligence System API is running. Visit /docs for the dashboard."}

# --- 1. POSTGRESQL ROUTE: Structured Data ---
@app.post("/api/v1/sites", tags=["Monitoring Sites"])
def create_monitoring_site(site_name: str, lat: float, lon: float, db: Session = Depends(get_pg_db)):
    """Saves relational spatial data to PostgreSQL."""
    new_site = MonitoringSite(site_name=site_name, protected_area="General", latitude=lat, longitude=lon)
    db.add(new_site)
    db.commit()
    db.refresh(new_site)
    return new_site

# --- 2. MONGODB ROUTE: Unstructured Sensor Logs ---
@app.post("/api/v1/sensor/log", tags=["MongoDB Metadata"])
def log_raw_sensor_data(device_id: str, payload: dict, mongo_db = Depends(get_mongo_db)):
    """Saves flexible JSON metadata from camera traps/audio sensors to MongoDB."""
    collection = mongo_db["raw_sensor_logs"]
    log_entry = {
        "device_id": device_id,
        "timestamp": datetime.utcnow(),
        "raw_payload": payload
    }
    result = collection.insert_one(log_entry)
    return {"message": "Logged to MongoDB successfully", "log_id": str(result.inserted_id)}

# --- 3. DATASET PIPELINE VERIFICATION ---
@app.get("/api/v1/datasets/status", tags=["Datasets Integration"])
def get_dataset_links():
    """Verifies all 5 specific datasets for Milestone 1 evaluation."""
    return {
        "1_Serengeti": DatasetIntegrator.verify_serengeti(),
        "2_iNaturalist": DatasetIntegrator.verify_inaturalist(),
        "3_BirdCLEF": DatasetIntegrator.verify_birdclef(),
        "4_Animal_Kingdom": DatasetIntegrator.verify_animal_kingdom(),
        "5_GBIF": DatasetIntegrator.verify_gbif()
    }

### --- REGISTRATION ENDPOINT --- ###
@app.post("/api/v1/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Authentication"])
def register_user(user: UserCreate, db: Session = Depends(get_pg_db)):
    # 1. Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Email already registered"
        )
    
    # 2. Hash password and save to PostgreSQL
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password, role_id=user.role_id)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

### --- LOGIN ENDPOINT --- ###
@app.post("/api/v1/auth/login", response_model=Token, tags=["Authentication"])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_pg_db)):
    # Note: OAuth2PasswordRequestForm uses 'username' by default, 
    # so in Swagger you will type your email into the 'username' field.
    
    # 1. Fetch user
    user = db.query(User).filter(User.email == form_data.username).first()
    
    # 2. Verify existence and password
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Generate JWT
    access_token = create_access_token(
        data={"sub": user.email, "role_id": user.role_id}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}