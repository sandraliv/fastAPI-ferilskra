from fastapi import FastAPI
from db.config import settings
from db.session import engine 
from db.base_class import Base
from api.items import router as items_router

def create_tables():         
	Base.metadata.create_all(bind=engine) 

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()
app.include_router(items_router, prefix="/courses")


