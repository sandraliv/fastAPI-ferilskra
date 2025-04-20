from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from core.security import create_access_token, verify_password, hash_password
from db.models.db_models import User  # My SQLAlchemy user model
from db.session import get_db
from schemas.users import *

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/register", response_model=UserRead)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_in.username).first()
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        username=user_in.username,
        password=hash_password(user_in.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},  # Required by OAuth2 spec
        )

    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
