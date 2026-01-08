from services import create_user, add_task, delete_task, get_user_tasks, update_task_status

print("Регистрация")
create_user("Admin", "12345")

print("Добавление задач")
add_task("Admin", "Захватить мир")
add_task("Admin", "Покормить стул")

tasks = get_user_tasks("Admin")
print("Список задач:", tasks)

if tasks:
    first_task_id = tasks[0]['task_id']    
    print(f"Обновляем статус задачи с ID {first_task_id}...")
    update_task_status(first_task_id, "Admin", True)   
    print(f"Удаляем задачу с ID {first_task_id}")
    delete_task(first_task_id, "Admin")

print("Итоговый список:", get_user_tasks("Admin"))





