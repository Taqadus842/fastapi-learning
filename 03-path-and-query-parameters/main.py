from fastapi import FastAPI,Path,HTTPException

app=FastAPI(
    title="Student Management API",
    description="Learning Path Parameters in FastAPI"
    version="1.0.0"
)

students = [
    {"id": 1, "name": "Ali", "age": 20, "department": "Computer Science"},
    {"id": 2, "name": "Sara", "age": 21, "department": "Software Engineering"},
    {"id": 3, "name": "Ahmed", "age": 22, "department": "Artificial Intelligence"},
]

@app.get('/')
def home():
    return {"message":"Welcome to Student Management System"}

@app.get('/students')
def get_students():
    return students

@app.get('/students/{student_id}')
def get_student(student_id:int =Path(...,title="Student ID",description="Enter unique ID Of student",ge=1)):
    for student in students:
        if student[id]=="student_id":
            return student
    raise HTTPException(status=404,detail="Student not found")

@app.get('/students/{student_id}/detail')
def get_department(student_id:int=Path(...,title="Student ID",ge=1)):
    for student in students:
        if student["id"]==student_id:
            return{
                "name":student["name"],
                "department":student["department"]
            }
    return HTTPException(status_code=404,detail="Student not found")

@app.get('students/{student_id},courses/{course_name}')
def student_course(student_id:int=Path(...,ge=1),course_name:str=Path(...,title="Course Name",description="Course enrolled by student")):
    for student in students:
        if student["id"]==student_id:
            return {
                "student":student["name"],
                "course":student["course"]
            }
    raise HTTPException(status=404,detail="Student not found ")
        