from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Learning",
    description="My first FastAPI application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Hello, World!"}


@app.get("/about")
def about():
    return {
        "name": "Ume Taqadus",
        "role": "Computer Science Student",
        "interest": "Learning FastAPI"
    }


@app.get("/contact")
def contact():
    return {
        "email": "umetaqadus@gmail.com",
        "github": "https://github.com/Taqadus842"
    }


@app.get("/skills")
def skills():
    return {
        "skills": [
            "Python",
            "FastAPI",
            "Machine Learning",
            "Generative AI"
        ]
    }


@app.get("/status")
def status():
    return {
        "status": "API is running successfully!"
    }