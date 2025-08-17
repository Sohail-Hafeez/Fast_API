# Student API  

This is a simple **FastAPI project** that manages student data. The API allows you to **create, read, and store student details** in a JSON file. It also calculates **BMI (Body Mass Index)** and provides a **verbose description** of the student’s health status.  

---

##  Features  
- Create student records with the following fields:  
  - `id` (Unique identifier, used as the key in JSON)  
  - `name`  
  - `city`  
  - `age`  
  - `gender` (Male, Female, Other)  
  - `height` (in meters)  
  - `weight` (in kg)  
  - `bmi` (auto-calculated)  
  - `verbose` (health status based on BMI)  

- **Automatic BMI Calculation**  
  - BMI = weight / (height²)  
  - Health categories:  
    - Underweight  
    - Normal weight  
    - Overweight  
    - Obese  

- Data stored in `student.json`.  

---

##  Project Structure  

student_api/
│── app.py # FastAPI application
│── student.json # JSON file storing student data
│── README.md # Project documentation


---

##  Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/student-api.git
   cd student-api

2. Create a virtual environment (optional but recommended): 
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3. Install dependencies:
pip install fastapi uvicorn pydantic

4. Running the API

Start the FastAPI server using uvicorn:
uvicorn app:app --reload

5. The API will run at:
 http://127.0.0.1:8000 this was my local host it will be change in your case

** Example student.json
{
  "0001": {
    "name": "Sohail",
    "city": "Hajira",
    "age": 23,
    "gender": "Male",
    "height": 1.75,
    "weight": 70,
    "bmi": 22.86,
    "verbose": "Normal weight"
  }
}
