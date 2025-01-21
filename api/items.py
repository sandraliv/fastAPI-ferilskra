from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.item import createCourse, Course
from services.item_service import get_all_courses, get_item_by_id, create_item, delete_item
from db.session import db_commit
from typing import List


router = APIRouter()

''' --------- GET METHODS ------------'''

@router.get("/{course_id}", response_model=Course)
def read_item(course_id: int, db: Session = Depends(get_db)):
    course = get_item_by_id(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/", response_model=List[Course])
def all_courses(db: Session = Depends(get_db)):
    try:
        return get_all_courses(db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
''' ------------ POST METHODS ------------ '''

@router.post("/", response_model=Course)
def add_item(item: createCourse, db: Session = Depends(get_db)):
    with db_commit(db):
        item_db = create_item(db, item)
        return item_db

'''---------- DELETE METHODS --------------'''

@router.delete("/{course_id}", response_model=Course)
def delete_a_course(course_id: int, db: Session = Depends(get_db)):
    try:
        delete_item(db, course_id)
        return {"message": f"Item with id {course_id} successfully deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
