# Making the necessary imports
from fastapi import FastAPI , Path , HTTPException , Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field  
from typing import Annotated, Literal

import json

# app variable will contain our FastAPI
app = FastAPI()

# Making the BaseModel As we have learned in Pydantic

class Student(BaseModel):
    id: Annotated[str, Field(..., description='ID of the Student', examples=['0001'])]
    name: Annotated[str, Field(..., description='Name of the Student', examples=['Sohail'])]
    city: Annotated[str, Field(..., description='City of the Student', examples=['Hajira'])]
    age: Annotated[int, Field(..., gt=0 , lt= 100, description='Age of the Student', examples=[23])]
    gender: Annotated[str, Field(..., description='Gender of the Student', examples=['Male'])] 
    height: Annotated[float, Field(..., gt=0 , lt=4, description='Height of the Student in meters', examples=[1.5])]
    weight: Annotated[float, Field(..., gt=0 , lt=300, description='Weight of the Student in Kg', examples=[80])]

    # Now we will use computed_field to calculate the BMI of the students
    @computed_field
    @property
    def bmi(self) -> float:  
        bmi = round(self.weight/(self.height**2) , 2)
        return bmi

    # compute_field for Calculating Verbose
    @computed_field
    @property
    def verbose(self) -> str:  
        if self.bmi > 17 and self.bmi < 25:
            return 'Healthy Weight'
        elif self.bmi >= 25:
            return 'Over Weight'
        elif self.bmi < 17:
            return 'Under Weight'

# loadData will load stu.json in a variable called data
def loadData():
    with open('student.json' , 'r') as f:
        data = json.load(f) 
    return data   

# Function to save data
def saveData(data):
    with open('student.json' , 'w') as f:
        json.dump(data,f, indent=4)  

# Post request
@app.post('/create')
def createStudent(student : Student):
    
    # loading the data (it will appear in the form of Dictionary)
    data = loadData()
    
    # Check whether student aleady exist or not 
    if student.id in data:
        raise HTTPException( status_code=400 , detail = 'Student already Exist')
    
    # if not then we will add new Student
    data[student.id] = student.model_dump(exclude = ['id'])

    #Again Saving it in the JSON format    
    saveData(data)
    
    return JSONResponse(status_code=201 , content = {'message' : 'Student Added Sucessfully'})
