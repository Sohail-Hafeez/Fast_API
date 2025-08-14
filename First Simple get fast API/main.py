from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message" : "Hello API users"}

@app.get("/about")
def aboutMySelf():
    return {"message" : "Hello API users.... I am Muhammad Sohail Hafeez and I am learning fast API so that i can deploy and use my MAchine Learning models and it is important for me as I am going to be an AI engineer"}