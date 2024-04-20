import json

TASK_DATA="data/data_task.json"

def read_json():
    try:

        with open(TASK_DATA, "r") as fr:
            data = json.load(fr)
            return data
    except:
        data={"task":[]}

def write_json(data):
    try:
        with open(TASK_DATA, "w") as fw:
            json.dump(data, fw, indent=3)
    except:
        print("unable to print the data")


