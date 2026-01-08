from fastapi import FastAPI
from services import add_task, get_user_tasks, delete_task, create_user, login_user, update_task_status
from storage import read_json, write_json, TASKS_FILE, USERS_FILE

app = FastAPI()

@app.get("/tasks")
def user_tasks(user_id: str):
    tasks = get_user_tasks(user_id)
    return tasks

@app.post("/register")
def register(login: str, password: str):
    user = create_user(login, password)
    return user

@app.post("/add_task")
def add_new_task(user_id: str, task: str):
    task = add_task(user_id, task)
    return task

@app.post("/set_done")
def set_done_task(task_id: int, user_id: str, new_status: bool):
    status = update_task_status(task_id, user_id, new_status)
    return status

@app.delete("/delete_task")
def delete_user_task(task_id: int, user_id: str):
    delete = delete_task(task_id, user_id)
    return delete
