from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi import status
from fastapi import HTTPException
from fastapi import Response



app = FastAPI()

class Tasks(BaseModel):
    id : int
    title: str
    done : bool


my_tasks = [
    {"id":1, "title": "Buy rasgulla", "completed": False},
    {"id":2, "title": "Call Srinjoni", "completed": False},
    {"id":3, "title": "build api", "completed": False},
]



@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/Health")
async def statusof ():
    return {"status":"ok"}

@app.get("/tasks")
async def task():
    return {"data":my_tasks}

@app.get("/tasks/{id}")
async def gettask(id:int,response:Response):
    for work in my_tasks:
        if work['id']==id:
            return {"task_details":work}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"task with id: {id} was not found")    


    



