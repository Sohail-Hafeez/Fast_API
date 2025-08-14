from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

def loadData():
    with open ('stu.json' , 'r') as f:
        data = json.load(f)
        return data

app = FastAPI()

@app.get("/")
def Title():
    return {"message" : "MCS student MAnagement System"}

@app.get("/about")
def about():
    return {"message" : "Managing the data of all the students of MCS a campus of NUST"}

@app.get("/view")
def data():
    data = loadData() 
    return data 

@app.get("/student/{student_id}")
def viewStudent(student_id: str):
    data = loadData()
    if student_id in data:
        return data[student_id]
    
@app.get("/students/{student_id}/{attribute}")
def viewStudent(student_id: str, attribute: str):
    data = loadData()
    if student_id in data:
        if attribute in data[student_id]:
            return {attribute: data[student_id][attribute]}
