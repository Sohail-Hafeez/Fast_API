from pydantic import BaseModel, EmailStr, Field, ValidationError , field_validator , model_validator , computed_field
from typing import List, Dict, Optional , Annotated

class Student(BaseModel):
    name: Annotated[str  , Field(max_length=50 , title = 'name of the patient' , description="Give the name of the student in less then 50 char ", examples=['Sohail' , 'Hafeez'])]
    email: EmailStr
    age: int
    height : float  # must be in meter
    weight: float = Field(gt=0)  #must be in Kg
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
    
    
#  Field Validator is applicable only on a specific field what if we have to validate data based on two fields for taht purpose we have model_validator That allow us to acess full model

    @model_validator(mode = 'after')
    def younger_Student_Must_Have_Emergency_No(cls,model):
        if model.age <10 and 'emergency' not in model.contactDetail:
            raise ValueError("Student Having Age less then 10 must have a Emergency No...  ")
        return model
    
#  if you are given certain specific attribute and you need to create a new one and you donot want user to give it directly to you as a specific field then in that case you can use computed_field 

# Lets take an Example Consider 2 things height and weight being provided as the 2 different fields  and we will compute BMI using this
 
    @computed_field
    @property
    def BMI(self)->float:   # we are providinig the return type of our function
        bmi = round(self.weight/(self.height**2),2)
        return bmi
        
        
    
    
studentData = {
    "name": "Sohail",
    "email": "sohailhafeez6464@pakistan.com", 
    "age": 20,
    "weight": 85.8492,
    "height" : 1.72,
    "gender": "Male",
    "allergies": ["Peanuts", "Dust"],
    "contactDetail": {"number": "03473073674"}
}



try:
    student = Student(**studentData)
    print("Validation passed " )
    print(student.name)
    print(student.BMI)
except ValidationError as e:
    print("Validation failed ")
    print(e)
