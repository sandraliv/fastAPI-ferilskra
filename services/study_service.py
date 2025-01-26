from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.db_models import StudyDB, CourseDB
from schemas.courses_pydantic import Study, Course

def create_study(db: Session, item: Study) -> StudyDB:
    print(item.dict())
    study_db = StudyDB(name=item.name, slug=item.slug)
    db.add(study_db)
    db.commit()
    db.refresh(study_db)
    return study_db


def get_item_by_study(db: Session, study_slug: str) -> list[CourseDB]:

    # Fetch the study
    study = db.query(StudyDB).filter(StudyDB.slug == study_slug).first()

    # Debug log for the result
    if not study:
        print(f"No study found for slug: {study_slug}")
        raise HTTPException(status_code=404, detail="Study not found")

    print(f"Found study: {study.name} with ID: {study.id}")

    # Fetch and return courses
    return db.query(CourseDB).filter(CourseDB.study_id == study.id).all()