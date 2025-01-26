from sqlalchemy import Column, Integer, String, Float
from db.base_class_db import Base
from enum import Enum as PyEnum
from sqlalchemy.dialects.postgresql import ENUM

class Month(PyEnum):
    JUN = "JUN"
    MAI = "MAI"
    DES = "DES"

class CourseDB(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    grade = Column(Float, nullable=False)
    credits = Column(Integer, nullable=False)
    school_id = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(ENUM(Month, name="month"), nullable=False)
