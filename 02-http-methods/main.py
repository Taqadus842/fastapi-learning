from fastapi import FastAPI
import json

app = FastAPI(
    title="Patient Management System",
    description="A simple API demonstrating HTTP methods in FastAPI"
)


def load_data():
    with open("patients.json", "r") as f:
        return json.load(f)


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


@app.get("/")
def home():
    return {"message": "Welcome to Patient Management System"}


@app.get("/about")
def about():
    return {
        "message": "A simple API built with FastAPI to learn HTTP methods."
    }


@app.get("/patients")
def get_patients():
    return load_data()


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    patients = load_data()

    for patient in patients:
        if patient["id"] == patient_id:
            return patient

    return {"message": "Patient not found"}


@app.post("/patients")
def create_patient(patient: dict):
    patients = load_data()

    patients.append(patient)
    save_data(patients)

    return {
        "message": "Patient added successfully",
        "patient": patient
    }


@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, updated_data: dict):
    patients = load_data()

    for patient in patients:
        if patient["id"] == patient_id:
            patient.update(updated_data)
            save_data(patients)

            return {
                "message": "Patient updated successfully",
                "patient": patient
            }

    return {"message": "Patient not found"}


@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    patients = load_data()

    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            save_data(patients)

            return {
                "message": "Patient deleted successfully"
            }

    return {"message": "Patient not found"}