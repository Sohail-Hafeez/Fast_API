# Pydantic  Theory & Overview

This folder contains an example `app.py` showcasing how to use **Pydantic** with FastAPI. Below is the theoretical foundation behind Pydantic: why it's useful, its key features, and common patterns.

---

##  What Is Pydantic?

- **Pydantic** is a Python library for **runtime data validation and settings management**, built on top of native Python type hints. It ensures that the data your application works with is both structured and valid.  
  
- It’s widely adopted, especially in frameworks like FastAPI, because it brings **type safety**, **serialization**, and **automatic documentation** to Python applications.  
  

---

##  Why Use Pydantic?

1. **Leverages type hints** – Simplifies validation and defines data expectations clearly.  

2. **High performance** – Core logic implemented in Rust, making validation fast.
3. 
4. **Serialization support** – Easily convert data to/from dict or JSON.  

5. **Coercion and strict typing** – Can auto-convert values (e.g., `"25"` → `25`) or enforce strict types.  

6. **Ecosystem integration** – Powers request validation and documentation in FastAPI and other libraries.  


---

##  Core Concepts & Features

### 1. **BaseModel**
- All Pydantic models inherit from `BaseModel`.
- These define schemas with annotated fields and enforce type and value constraints.  
  
### 2. **Field Constraints**
- Use `Field(...)` to define validation rules like `gt`, `ge`, `max_length`, etc.  

### 3. **Nested Models**
- You can nest models inside one another for complex structured data.  
  
### 4. **Default Values & `Field(default_factory=...)`**
- Set defaults, especially for mutable defaults, using `default_factory`; avoids shared object pitfalls.  
  
### 5. **Custom Validation**
- You can add custom validation logic using decorators like `@validator`.  

### 6. **Serialization & JSON Schema**
- Models support `.model_dump()` (or `.dict()` in v1) and can generate JSON Schema automatically.  

### 7. **Error Reporting**
- When validation fails, a `ValidationError` is raised with rich contextual feedback.   

---

##  How This Relates to FastAPI

- **Pydantic models** define request and response schemas in FastAPI.
- They power **automatic data validation**, **documentation** (OpenAPI/Swagger), and **serialization**.
- Example:
    ```python
    from fastapi import FastAPI
    from pydantic import BaseModel, EmailStr

    app = FastAPI()

    class User(BaseModel):
        name: str
        email: EmailStr

    @app.post("/users/")
    async def create_user(user: User):
        return user
    ```
    FastAPI ensures input matches the schema, raises an error if invalid, and documents the API automatically.  
    

---

##  Summary

- Pydantic converts Python type hints into **powerful runtime validation**.
- It supports **type coercion**, **serialization**, **nested validation**, and **custom logic**.
- Seamless integration with FastAPI makes it a foundation for robust, self-documenting APIs.

---

##  Next Steps

Check `app.py` in this folder for a hands-on example demonstrating:
- Defining a Pydantic model.
- Including field constraints.
- Handling validation errors.
- Using the model with FastAPI endpoints and seeing automatic documentation in action.

---

