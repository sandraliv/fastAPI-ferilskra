from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Optional
from slugify import slugify

class Month(str, Enum):
    JUN = "JUN"
    MAI = "MAI"
    DES = "DES"

#pydantic model for an item requests
'''A Pydantic model is a Python class used to define and validate data structures. 
It is a core feature of the Pydantic library, which is widely used in modern Python applications 
(like FastAPI) for managing structured data. Pydantic models provide an easy way to:
-Define data schemas.
-Validate input data.
-Serialize and deserialize data (convert between different formats, e.g., JSON and Python objects).
'''

class Study(BaseModel):
    name: str
    _slug: str = ""

    @property
    def slug(self):
        return slugify(self.name)
    
    #Returns the modified dictionary of the BaseModel and adds a slug field in the dict.
    def dict(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        data["slug"] = self.slug  # Include slug in serialized output
        return data
  

class createCourse(BaseModel):
    name: str
    grade: float
    credits: int
    school_id: str
    year: int
    month: Month
    study: Study

#pydantic model for an item requests
class Course(BaseModel):
    id: int
    name: str
    grade: float
    credits: int
    school_id: str
    year: int
    month: Month
    study: Study

    model_config = ConfigDict(from_attributes=True)

    #pydantic model for a course update
class CourseUpdate(BaseModel):
    name: Optional[str] = None
    grade: Optional[float] = None
    credits: Optional[int] = None
    school_id: Optional[str] = None
    year: Optional[int] = None
    month: Optional[Month] = None
    Study: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)