from db import SessionLocal
from models import Users, Tasks

def register_new_user(login, password):
    try:
        db = SessionLocal()
        existing_user = db.query(Users).filter(Users.login == login).first()
        if existing_user != None:
            return False
        new_user = Users(login=login, password=password)
        db.add(new_user)
        db.commit()
        return True
    finally:
        db.close()
  
def add_task(user_login, task_text):
   db = SessionLocal()
   try:
       owner = db.query(Users).filter(Users.login == user_login).first()
       if owner != None:
           new_task = Tasks(content=task_text, owner_id=owner.id)
           db.add(new_task)
           db.commit() 
           return True
       return False 
   finally:
       db.close()

def get_user_tasks(user_login):
    db = SessionLocal()
    try:
        user = db.query(Users).filter(Users.login == user_login).first()
        if user != None:
            task = db.query(Tasks).filter(Tasks.owner_id == user.id).all()
            return task
        return []
    finally:
        db.close()
    
def update_task_status(task_id, new_status):
    db = SessionLocal()
    try:
        task = db.query(Tasks).filter(Tasks.id == task_id).first()
        if task != None:
            task.is_done = new_status
            db.commit()
            return True
        return False
    finally:
        db.close()

def delete_task(task_id, user_login):
    db = SessionLocal()
    try:
        user = db.query(Users).filter(Users.login == user_login).first()
        if user != None:
            task = db.query(Tasks).filter(
                Tasks.id == task_id, 
                Tasks.owner_id == user.id  
            ).first()
            if task != None:
                db.delete(task)
                db.commit()
                return True   
        return False
    finally:
        db.close()

def login_user(login, password):
    db = SessionLocal()
    try:
        user = db.query(Users).filter(Users.login == login).first()
        if user != None and user.password == password:
            return True
        return False
    finally:
        db.close()

