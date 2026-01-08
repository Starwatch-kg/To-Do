import json
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
USERS_FILE = DATA_DIR / "users.json"
TASKS_FILE = DATA_DIR / "tasks.json"

def read_json(path):
    try:        
        if path.is_file():
            with path.open() as file:
                data = json.load(file)
                return data
        else:
            return []
    except json.JSONDecodeError:
        return []

def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        


