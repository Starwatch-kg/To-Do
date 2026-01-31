from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from services import add_task, get_user_tasks, delete_task, create_user, login_user, update_task_status
from storage import read_json, write_json, TASKS_FILE, USERS_FILE

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    user = request.cookies.get("user_login")
    if user is None:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    else:
        my_tasks = get_user_tasks(user)
        return templates.TemplateResponse("index.html", {
            "request": request, 
            "tasks": my_tasks, 
            "user": user
        })

@app.post("/add_task_form")
def add_task_form(request: Request, task: str = Form()):
    user = request.cookies.get("user_login")   
    if user:
        add_task(user, task)     
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/delete_task_form")
def delete_task_form(request: Request, task_id: int = Form()):
    user = request.cookies.get("user_login")
    if user:
        delete_task(task_id, user)
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/update_status_form")
def update_status_form(request: Request, task_id: int = Form(), new_status: bool = Form()):
    user = request.cookies.get("user_login") 
    if user:
        update_task_status(task_id, user, new_status)  
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/register_user")
def register_new_user(request: Request, login: str=Form(), password: str=Form()):
    create_user(login, password)
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/logout")
def logout_user():
    response = RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie(key="user_login")
    return response

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login_user")
def user_login(request: Request, login: str=Form(), password: str=Form()):
    is_valid = login_user(login, password)
    if is_valid == True:
        response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
        response.set_cookie(key="user_login", value=login)
        return response
    else:
        return RedirectResponse("login", status_code=status.HTTP_303_SEE_OTHER)

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
