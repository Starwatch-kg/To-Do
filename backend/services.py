from storage import read_json, write_json, USERS_FILE, TASKS_FILE

def create_user(login, password):
    users = read_json(USERS_FILE)
    for user_login in users:
        if user_login['login'] == login:
            return "login already exists"       
    new_id = max([u['id'] for u in users], default=0) + 1
    new_user = {"id": new_id, "login": login, "password": password}   
    users.append(new_user)    
    write_json(USERS_FILE, users)
    return True

def add_task(user_id, task):
    users_task = read_json(TASKS_FILE)
    task_id = max([u['task_id'] for u in users_task], default=0) + 1
    task = {'user_id': user_id, 'task_id': task_id, 'task':task, 'status':False}
    users_task.append(task)
    write_json(TASKS_FILE, users_task)
    return True

def get_user_tasks(user_id):
    all_tasks = read_json(TASKS_FILE)
    my_tasks = [t for t in all_tasks if t['user_id'] == user_id]
    return my_tasks

def update_task_status(task_id, user_id, new_status):
    all_tasks = read_json(TASKS_FILE)
    for id_task in all_tasks:
        if id_task['task_id'] == task_id and id_task['user_id'] == user_id:
            id_task['status'] = new_status
            break
    write_json(TASKS_FILE, all_tasks)

def delete_task(task_id, user_id):
    all_task = read_json(TASKS_FILE)
    new_task = [t for t in all_task if (not (t['task_id'] == task_id and t['user_id'] == user_id))]
    write_json(TASKS_FILE, new_task)

def login_user(login, password):
    users = read_json(USERS_FILE)
    for user in users:
        if user['login'] == login:
            if user['password'] == password:
                return True 
    return False    