# 01 - Introduction to FastAPI

## Overview

This is my first FastAPI application. In this lesson, I learned how to:

- Create a FastAPI application
- Run a FastAPI server using Uvicorn
- Define GET endpoints
- Return JSON responses
- Explore the automatically generated API documentation

## Project Structure

```
01-introduction/
├── main.py
└── README.md
```

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

## Installation

```bash
pip install fastapi uvicorn
```

## Run the Application

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns a welcome message |
| GET | `/about` | Returns basic information |

## API Documentation

FastAPI automatically generates interactive documentation.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Learning Outcomes

After completing this lesson, I can:

- Initialize a FastAPI application
- Create basic API routes
- Return JSON responses
- Run the application using Uvicorn
- Access FastAPI's automatic API documentation

## References

- https://fastapi.tiangolo.com/