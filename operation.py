from utlity import *

def add_task(task):
    data = read_json()

    task_json = {
        "sno" : len(data["task"])+1,
        "task": task,
        "status": "open"
    }
    data["task"].append(task_json)
    write_json(data)
    print("data add sucessfully")

def update_task(id, updated_task):
    data = read_json()
    for task in data["task"]:
        if task["sno"] == int(id):
            task["task"] = updated_task
            write_json(data)
            print(f'{task["sno"]}updated sucessfully')

def mark_done(id):
    data = read_json()
    for task in data["task"]:
        if task["sno"] == int(id):
            task["status"] = "done"
            write_json(data)
            print(f'{task["sno"]}mark done sucessfully')

def delete_task(id):
    data = read_json()
    for task in data["task"]:
        if task["sno"] == int(id):
            data["task"].remove(task)
        i = 1
        for task1 in data["task"]:
            task1["sno"] = i
            i += 1
        write_json(data)
        print(f'{task["sno"]}deleted sucessfully')