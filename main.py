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
    {"id":1, "title": "Buy rasgulla", "done": False},
    {"id":2, "title": "Call Srinjoni", "done": False},
    {"id":3, "title": "build api", "done": False},
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
        task_dict['id']=randrange(4,100000000000)
        my_tasks.append(task_dict) 
        return task_dict
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
@app.put("/tasks/{id}")
async def updatetask(id:int,task:Tasks):
    taskdict = task.model_dump()
    if (("title" in taskdict and taskdict['title'] is not None) and taskdict["title"] != ""):
        for work in my_tasks:
            if (work['id']==id):
                work['title']=taskdict['title']
                if "done" in taskdict:
                    work['done']=taskdict['done']
                return work
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
@app.delete("/tasks/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deletetask(id:int):
    for idx,work in enumerate(my_tasks):
        if work['id']==id:
            my_tasks.pop(idx)
            return 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)    

#checked with SWAGGER UI AND POSTMAN API

            

        
