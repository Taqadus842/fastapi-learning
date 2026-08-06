# 03 - Path Parameters in FastAPI

## Overview

This project demonstrates how to use **Path Parameters** in FastAPI to build dynamic API routes. It includes examples of retrieving student information by ID, accessing nested resources, validating path parameters, and handling errors using `HTTPException`.

---

## Learning Objectives

After completing this lesson, I learned how to:

- Create dynamic API routes using path parameters
- Validate path parameters with `Path()`
- Add metadata such as titles and descriptions
- Handle invalid requests using `HTTPException`
- Create endpoints with multiple path parameters
- Test APIs using FastAPI's interactive documentation

---

## Project Structure

```text
03-path-parameters/
├── main.py
└── README.md
```

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

Install the required packages:

```bash
pip install fastapi uvicorn
```

---

## Running the Application

Navigate to the project directory:

```bash
cd 03-path-parameters
```

Run the server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| GET | `/students/{student_id}/department` | Get a student's department |
| GET | `/students/{student_id}/courses/{course_name}` | Demonstrates multiple path parameters |

---

## Sample Data

```json
[
    {
        "id": 1,
        "name": "Ali",
        "age": 20,
        "department": "Computer Science"
    },
    {
        "id": 2,
        "name": "Sara",
        "age": 21,
        "department": "Software Engineering"
    },
    {
        "id": 3,
        "name": "Ahmed",
        "age": 22,
        "department": "Artificial Intelligence"
    }
]
```

---

## Concepts Covered

### Path Parameters

Path parameters allow values to be passed directly through the URL.

Example:

```
/students/1
```

FastAPI automatically converts the value to the specified type.

---

### Path Validation

`Path()` is used to validate and document path parameters.

Example:

```python
student_id: int = Path(
    ...,
    title="Student ID",
    description="Unique ID of the student",
    ge=1
)
```

Validation used in this project:

- `ge=1` → Student ID must be greater than or equal to 1.

---

### HTTPException

`HTTPException` is used to return meaningful error responses.

Example:

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

---

## Learning Outcomes

By completing this lesson, I can:

- Build dynamic routes using path parameters
- Validate path parameter values
- Raise custom HTTP exceptions
- Create nested routes
- Use multiple path parameters in a single endpoint
- Understand how FastAPI automatically documents APIs

---
