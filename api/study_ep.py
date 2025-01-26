from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.courses_pydantic import Study, Course
from services.course_service import *
from services.study_service import *
from db.session import db_commit
from typing import List

router = APIRouter()


@router.get("/{study_slug}", response_model=list[Course])
def courses_by_study(study_slug: str, db: Session = Depends(get_db)):
    try:
        courses =  get_item_by_study(db, study_slug)
        print(courses)
        if not courses:
            raise HTTPException(status_code=404, detail="No courses found for the specified study.")
        return courses
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
@router.post("/")
def add_study(item: Study, db: Session = Depends(get_db)):
    try:
        with db_commit(db):
            create_study(db, item)
        return {"message": f"{item} successfully added"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something happened, couldn't add study")
