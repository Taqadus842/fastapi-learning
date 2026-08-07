# FastAPI POST Request & Request Body

A beginner-friendly FastAPI mini project for practicing **POST requests, request bodies, Pydantic models, validation, and JSON responses**.

This project uses a `patients.json` file as a simple database and provides APIs for managing patients and calculating BMI.

## Project Structure

```text
05-post-request-request-body/
│
├── main.py
├── patients.json
├── requirements.txt
└── README.md
```

## Technologies

* Python
* FastAPI
* Pydantic
* Uvicorn
* JSON

## Concepts Practiced

* FastAPI application
* GET requests
* POST requests
* Request body
* Pydantic `BaseModel`
* `Field`
* `Annotated`
* `Literal`
* Path parameters
* Query parameters
* HTTP exceptions
* JSON responses
* Reading and writing JSON files
* Basic BMI calculation

## Installation

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

#### Linux/macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 🔗 API Endpoints

### Home

```http
GET /
```

Returns basic information about the API.

### Get All Patients

```http
GET /patients
```

Returns all patients stored in `patients.json`.

### Get Patient

```http
GET /patients/{patient_id}
```

Example:

```http
GET /patients/1
```

### Get Patient BMI

```http
GET /patients/{patient_id}/bmi
```

Example:

```http
GET /patients/1/bmi
```

Example response:

```json
{
    "id": 1,
    "name": "John Doe",
    "bmi": 22.86,
    "category": "Normal"
}
```

### Create Patient

```http
POST /patients
```

Request body:

```json
{
    "id": 3,
    "name": "Ume",
    "age": 23,
    "height": 1.70,
    "weight": 65
}
```

Example response:

```json
{
    "status": "success",
    "message": "Patient created successfully",
    "patient": {
        "id": 3,
        "name": "Ume",
        "age": 23,
        "height": 1.7,
        "weight": 65
    }
}
```

### Calculate BMI Using Request Body

```http
POST /bmi
```

Request body:

```json
{
    "id": 4,
    "name": "Ali",
    "age": 25,
    "height": 1.75,
    "weight": 70
}
```

Response:

```json
{
    "name": "Ali",
    "height": 1.75,
    "weight": 70,
    "bmi": 22.86,
    "category": "Normal"
}
```

### Calculate BMI Using Query Parameters

```http
GET /bmi?height=1.75&weight=70
```

Response:

```json
{
    "height": 1.75,
    "weight": 70,
    "bmi": 22.86,
    "category": "Normal"
}
```

## What Is a Request Body?

A request body contains data sent by the client to the server.

For example, when creating a patient:

```json
{
    "id": 3,
    "name": "Ume",
    "age": 23,
    "height": 1.70,
    "weight": 65
}
```

FastAPI receives this JSON and validates it using the Pydantic model:

```python
class Patient(BaseModel):
    id: int
    name: str
    age: int
    height: float
    weight: float
```

The endpoint can then receive the validated object:

```python
@app.post("/patients")
def create_patient(patient: Patient):
    ...
```

## Request Flow

```text
Client
   │
   │ POST /patients
   │
   │ JSON Request Body
   ▼
FastAPI
   │
   ▼
Pydantic Validation
   │
   ▼
Patient Object
   │
   ▼
patients.json
   │
   ▼
JSON Response
```

## BMI Formula

The BMI is calculated using:

```text
BMI = weight / height²
```

Where:

* Weight is measured in kilograms
* Height is measured in meters

BMI categories used in this project:

| BMI         | Category    |
| ----------- | ----------- |
| < 18.5      | Underweight |
| 18.5 – 24.9 | Normal      |
| 25 – 29.9   | Overweight  |
| ≥ 30        | Obese       |

## Testing

You can test the API using the automatically generated Swagger UI:

```text
http://127.0.0.1:8000/docs
```

You can also use tools such as:

* Postman
* cURL
* Thunder Client

## Learning Goal

This project is part of my **FastAPI learning journey** and focuses on understanding how FastAPI handles:

```text
POST Request
      ↓
Request Body
      ↓
Pydantic Model
      ↓
Validation
      ↓
Python Object
      ↓
JSON Response
```

## Author

**Ume Taqadus**

FastAPI Learning Project
