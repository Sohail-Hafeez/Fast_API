from fastapi import FastAPI, Path,HTTPException , Query
from pydantic import BaseModel
import json

def loadData():
    with open ('stu.json' , 'r') as f:
        data = json.load(f)
        return data

app = FastAPI()

@app.get("/")
def Title():
    return {"message" : "MCS student Management System"}

@app.get("/about")
def about():
    return {"message" : "Managing the data of all the students of MCS a campus of NUST"}

@app.get("/view")
def data():
    data = loadData() 
    return data 

@app.get("/student/{student_id}")
def viewStudent(student_id: str  = Path(..., description = "Enter the number of student" , examples = 'student1' )):
    data = loadData()
    if student_id in data:
        return data[student_id]
    raise HTTPException(status_code=404 , detail="Student not found")
 
 
    
@app.get("/students/{student_id}/{attribute}")
def viewStudent(student_id: str = Path(..., description = "Enter the number of student" , examples = 'student1' ), attribute: str= Path(..., description = "Enter the number of attribute" , example = 'id/name and .....' )):
    data = loadData()
    if student_id in data:
        if attribute in data[student_id]:
            return {attribute: data[student_id][attribute]}
        raise HTTPException(status_code=404 , detail=f"No attribute of {attribute} in {student_id}")
    raise HTTPException(status_code=404 , detail=f"No student as {student_id} found")



    
@app.get('/sort')
def sortStudents(sort_by: str = Query(..., description= "Sort on the bases of id , CGPA"), order: str = Query(description="Sort in asc or desc order")):
    field = ['id' , "CGPA" , "projects"]
    if sort_by not in field:
        raise HTTPException(status_code=400 , detail=f"No method of sorting such as {sort_by} exists")
    if order not in ['asc' , 'desc']:
        raise HTTPException(status_code=400 , detail=f"inorder order selection kindly select asc or desc")
    
    data = loadData()
    
    sortData = True if order=='desc' else False
    
    sortedData = sorted(data.values() , key = lambda x: x.get(sort_by , 0), reverse = sortData )
    
    return sortedData
