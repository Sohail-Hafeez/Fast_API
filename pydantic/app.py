from pydantic import BaseModel, EmailStr, Field, ValidationError , field_validator
from typing import List, Dict, Optional , Annotated

class Student(BaseModel):
    name: Annotated[str  , Field(max_length=50 , title = 'name of the patient' , description="Give the name of the student in less then 50 char ", examples=['Sohail' , 'Hafeez'])]
    email: EmailStr
    age: int
    weight: float = Field(gt=0)
    gender: Annotated[str , Field(default='Male', description = 'Please write the gender of student') ]
    allergies: Annotated[Optional[List[str]] , Field(default=None , max_length = 5 )]
    contactDetail: Dict[str, str]
    
    # Concept of field Validator 
    # If you want to make Custom Email validator or some thing Similar so you have to maek a field VAlidator 

    @field_validator('email')
    @classmethod 
    def emailValidator(cls , value):
        validDomain = ['pakistan.com' , 'nust.com']
        domainName = value.split('@')[-1]
        
        if domainName not in validDomain:
            raise ValueError("Not a Valid Domain")
        return value
    
    
    # using a field validator for name 
    @field_validator('name')
    @classmethod
    def namevalidator(cls,value):
        return value.upper()
        
    
    
studentData = {
    "name": "Sohail",
    "email": "sohailhafeez6464@pakistan.com", 
    "age": 20,
    "weight": 85.8492,  
    "gender": "Male",
    "allergies": ["Peanuts", "Dust"],
    "contactDetail": {"number": "03473073674"}
}



try:
    student = Student(**studentData)
    print("Validation passed " )
    print(student.name)
except ValidationError as e:
    print("Validation failed ")
    print(e)
