from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.item import createCourse, Course
from services.item_service import get_all_courses, get_item_by_id, create_item, delete_item

router = APIRouter()

@router.get("/{course_id}", response_model=Course)
def read_item(course_id: int, db: Session = Depends(get_db)):
    course = get_item_by_id(db, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.post("/", response_model=Course)
def add_item(item: createCourse, db: Session = Depends(get_db)):
    item_db = create_item(db, item)
    return item.model_validate(item_db)

@router.delete("/{course_id}", response_model=Course)
def delete_a_course(course_id: int, db: Session = Depends(get_db)):
    try:
        delete_item(db, course_id)
        return {"message": f"Item with id {course_id} successfully deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=Course)
def all_courses(course_id: int, db: Session = Depends(get_db)):
    try:
        return get_all_courses(db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))