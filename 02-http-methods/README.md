# 02 - HTTP Methods in FastAPI

## Overview

This project demonstrates the implementation of the four primary HTTP methods in FastAPI using a simple Patient Management System. Patient records are stored in a JSON file, making it easy to understand CRUD operations before integrating a database.

## Learning Objectives

After completing this lesson, I learned how to:

- Create GET, POST, PUT, and DELETE endpoints
- Build RESTful APIs with FastAPI
- Read data from a JSON file
- Write updated data back to a JSON file
- Perform basic CRUD operations
- Test APIs using Swagger UI and ReDoc

---

## Project Structure

```text
02-http-methods/
├── main.py
├── patients.json
└── README.md
```

---

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

## Running the Application

Navigate to the project folder:

```bash
cd 02-http-methods
```

Start the server:

```bash
uvicorn main:app --reload
```

The API will be available at:

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
| GET | `/about` | Project description |
| GET | `/patients` | Retrieve all patients |
| GET | `/patients/{patient_id}` | Retrieve a patient by ID |
| POST | `/patients` | Add a new patient |
| PUT | `/patients/{patient_id}` | Update an existing patient |
| DELETE | `/patients/{patient_id}` | Delete a patient |

---

## Sample Patient Record

```json
{
    "id": 1,
    "name": "Ali Khan",
    "age": 28,
    "gender": "Male",
    "city": "Karachi"
}
```

---

## HTTP Methods Explained

### GET

Retrieves information from the server without modifying data.

### POST

Creates a new resource by sending data to the server.

### PUT

Updates an existing resource.

### DELETE

Removes a resource from the server.

---

## Learning Outcomes

- Understood the purpose of different HTTP methods
- Built RESTful API endpoints
- Implemented CRUD operations
- Read and updated JSON data
- Tested APIs using FastAPI's interactive documentation

---
