from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from fastapi import status
from fastapi import HTTPException
from fastapi import Response
from random import randrange
from typing import Optional

import sqlite3

DB_NAME="tasks.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory=sqlite3.Row
    return conn

def init_DB():
    conn= get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        done BOOLEAN NOT NULL DEFAULT 0
    )
    """)

    conn.commit()
    conn.close() 



app = FastAPI()

init_DB()



class Tasks(BaseModel):
    title: str | None = None
    done : bool=False


# my_tasks = [
#     {"id":1, "title": "Buy rasgulla", "done": False},
#     {"id":2, "title": "Call Srinjoni", "done": False},
#     {"id":3, "title": "build api", "done": False},
# ]



@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/Health")
async def statusof ():
    return {"status":"ok"}

@app.get("/tasks")
async def task():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()
    task_dict = [dict(row) for row in data]    
    conn.close()

    if task_dict is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Task not found")


    return {"data":task_dict}

@app.get("/tasks/{id}")
async def gettask(id:int,response:Response):
    for work in my_tasks:
        if work['id']==id:
            return {"task_details":work}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"task with id: {id} was not found")    

@app.post("/tasks",status_code=status.HTTP_201_CREATED)
async def createtask(task:Tasks):
    task_dict=task.model_dump()
    if (("title" in task_dict and task_dict['title'] is not None) and task_dict["title"] != ""):
        task_dict['id']=randrange(4,100000000000)
        # my_tasks.append(task_dict) 

        conn = get_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO tasks (id, title, done) VALUES (?, ?, ?)",
                       (task_dict["id"], task_dict["title"], task_dict["done"]))

        conn.commit()
        conn.close()
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
@app.put("/tasks/{id}")
async def updatetask(id:int,task:Tasks):
    task_dict = task.model_dump()
    conn= get_connection()
    cursor=conn.cursor()
    if (("title" in task_dict and task_dict['title'] is not None) and task_dict["title"] != ""):
        cursor.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?",
            (task_dict["title"], task_dict["done"], id)
        )
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
        updated_row = cursor.fetchone()
        conn.close()

        return dict(updated_row)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    
@app.delete("/tasks/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def deletetask(id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()

    deleted_count = cursor.rowcount
    conn.close()

    if deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return

#checked with SWAGGER UI AND POSTMAN API

            
#checked with first sql
        
