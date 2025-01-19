from pydantic import BaseModel, ConfigDict
from enum import Enum

class Month(str, Enum):
    JUN = "júní"
    MAI = "maí"
    DES = "des"

#pydantic model for an item requests
'''A Pydantic model is a Python class used to define and validate data structures. 
It is a core feature of the Pydantic library, which is widely used in modern Python applications 
(like FastAPI) for managing structured data. Pydantic models provide an easy way to:
-Define data schemas.
-Validate input data.
-Serialize and deserialize data (convert between different formats, e.g., JSON and Python objects).
'''
class createCourse(BaseModel):
    name: str
    grade: float
    credits: int
    school_id: str
    year: int
    month: Month
    

#pydantic model for an item requests
class Course(BaseModel):
    id: int
    name: str
    grade: float
    credits: int
    school_id: str
    year: int
    month: Month

    model_config = ConfigDict(from_attributes=True)