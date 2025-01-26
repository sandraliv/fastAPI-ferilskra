from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.db_models import CourseDB
from schemas.courses_pydantic import createCourse

def get_item_by_id(db: Session, item_id: int) -> CourseDB:
    return db.query(CourseDB).filter(CourseDB.id == item_id).first()

def create_item(db: Session, item: createCourse) -> CourseDB:
    item_db = CourseDB(**item.model_dump())
    db.add(item_db)
    db.commit()
    db.refresh(item_db)
    return item_db

def delete_item(db: Session, item_id: int) -> None:
    #Retrieve it from the db
    item = db.query(CourseDB).filter(CourseDB.id == item_id).first()
    #If the course does not exist, rais en exception
    if not item:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found in database")
    db.delete(item)
    db.commit()

def get_all_courses(db: Session) -> list[CourseDB]:
    return db.query(CourseDB).all()