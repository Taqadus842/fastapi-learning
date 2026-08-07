from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import json


app = FastAPI(
    title="Patient BMI API",
    description="Mini FastAPI project for practicing POST requests and request bodies"
)


# --------------------------------------------------
# Pydantic Model
# --------------------------------------------------

class Patient(BaseModel):
    id: int
    name: str
    age: Annotated[int, Field(gt=0, le=120)]
    height: Annotated[float, Field(gt=0, description="Height in meters")]
    weight: Annotated[float, Field(gt=0, description="Weight in kilograms")]


# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def load_patients():
    with open("patients.json", "r") as file:
        return json.load(file)


def save_patients(patients):
    with open("patients.json", "w") as file:
        json.dump(patients, file, indent=4)


def calculate_bmi(height: float, weight: float):
    return round(weight / (height ** 2), 2)


def get_bmi_category(bmi: float) -> Literal[
    "Underweight",
    "Normal",
    "Overweight",
    "Obese"
]:

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# --------------------------------------------------
# GET - Home
# --------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Patient BMI API",
        "docs": "/docs"
    }


# --------------------------------------------------
# GET - All Patients
# --------------------------------------------------

@app.get("/patients")
def get_all_patients():

    patients = load_patients()

    return {
        "count": len(patients),
        "patients": patients
    }


# --------------------------------------------------
# GET - Single Patient
# --------------------------------------------------

@app.get("/patients/{patient_id}")
def get_patient(
    patient_id: Annotated[
        int,
        Path(gt=0, description="Patient ID")
    ]
):

    patients = load_patients()

    for patient in patients:

        if patient["id"] == patient_id:

            return {
                "status": "success",
                "patient": patient
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# --------------------------------------------------
# GET - Patient BMI
# --------------------------------------------------

@app.get("/patients/{patient_id}/bmi")
def get_patient_bmi(
    patient_id: Annotated[
        int,
        Path(gt=0)
    ]
):

    patients = load_patients()

    for patient in patients:

        if patient["id"] == patient_id:

            bmi = calculate_bmi(
                patient["height"],
                patient["weight"]
            )

            category = get_bmi_category(bmi)

            return {
                "id": patient["id"],
                "name": patient["name"],
                "bmi": bmi,
                "category": category
            }

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )


# --------------------------------------------------
# POST - Add Patient
# --------------------------------------------------

@app.post("/patients")
def create_patient(patient: Patient):

    patients = load_patients()

    # Check whether ID already exists
    for existing_patient in patients:

        if existing_patient["id"] == patient.id:

            raise HTTPException(
                status_code=400,
                detail="Patient with this ID already exists"
            )

    # Convert Pydantic model to dictionary
    patient_data = patient.model_dump()

    # Add patient
    patients.append(patient_data)

    # Save to JSON
    save_patients(patients)

    return {
        "status": "success",
        "message": "Patient created successfully",
        "patient": patient_data
    }


# --------------------------------------------------
# POST - Calculate BMI from Request Body
# --------------------------------------------------

@app.post("/bmi")
def calculate_bmi_from_body(patient: Patient):

    bmi = calculate_bmi(
        patient.height,
        patient.weight
    )

    category = get_bmi_category(bmi)

    return {
        "name": patient.name,
        "height": patient.height,
        "weight": patient.weight,
        "bmi": bmi,
        "category": category
    }


# --------------------------------------------------
# GET - BMI using Query Parameters
# --------------------------------------------------

@app.get("/bmi")
def calculate_bmi_from_query(
    height: Annotated[
        float,
        Query(gt=0, description="Height in meters")
    ],

    weight: Annotated[
        float,
        Query(gt=0, description="Weight in kilograms")
    ]
):

    bmi = calculate_bmi(height, weight)

    category = get_bmi_category(bmi)

    return {
        "height": height,
        "weight": weight,
        "bmi": bmi,
        "category": category
    }