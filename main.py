from fastapi import FastAPI
from db.config import settings
from db.session import engine 
from db.base_class_db import Base
from api.endpoints import router as course_router
from api.study_ep import router as study_router

def create_tables():         
	Base.metadata.create_all(bind=engine) 

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()
app.include_router(course_router, prefix="/courses")
app.include_router(study_router, prefix="/studies")


