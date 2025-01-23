from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from .config import settings
from contextlib import contextmanager

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Once we create an instance of the SessionLocal class, this instance will be the actual database session. 
#We will create an actual database session for each request later.
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

@contextmanager
def db_commit(db: Session):
    try:
        yield
        db.commit()
    except:
        db.rollback()
        raise

def get_db():
    db = SessionLocal()
    try:
        yield db  # Yield the session to the caller
    finally:
        db.close()  # Ensure the session is closed after use
