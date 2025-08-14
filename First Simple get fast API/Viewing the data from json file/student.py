from fastapi import FastAPI
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