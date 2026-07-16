from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi import status
from fastapi import HTTPException
from fastapi import Response
from random import randrange
from typing import Optional



app = FastAPI()

class Tasks(BaseModel):
    title: str | None = None
    done : bool=False


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

@app.post("/tasks",status_code=status.HTTP_201_CREATED)
async def createtask(task:Tasks):
    task_dict=task.model_dump()
    if (("title" in task_dict and task_dict['title'] is not None) and task_dict["title"] is not ""):
        task_dict['id']=randrange(4,10)
        my_tasks.append(task_dict) 
        return task_dict
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        