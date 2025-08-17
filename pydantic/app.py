from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import List, Dict, Optional , Annotated

class Student(BaseModel):
    name: Annotated[str  , Field(max_length=50 , title = 'name of the patient' , description="Give the name of the student in less then 50 char ", examples=['Sohail' , 'Hafeez'])]
    email: EmailStr
    age: int
    weight: float = Field(gt=0)
    gender: Annotated[str , Field(default='Male', description = 'Please write the gender of student') ]
    allergies: Annotated[Optional[List[str]] , Field(default=None , max_length = 5 )]
    contactDetail: Dict[str, str]

studentData = {
    "name": "Sohail",
    "email": "sohailhafeez6464@gmail.com", 
    "age": 20,
    "weight": 85.8492,  
    "gender": "Male",
    "allergies": ["Peanuts", "Dust"],
    "contactDetail": {"number": "03473073674"}
}

try:
    student = Student(**studentData)
    print("Validation passed " )
except ValidationError as e:
    print("Validation failed ")
    print(e)
