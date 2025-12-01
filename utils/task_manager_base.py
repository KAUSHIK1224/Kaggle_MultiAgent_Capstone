import uuid

class TaskManagerBase:
    def __init__(self):
        self.tasks = {}

    def create_task(self, payload):
        task_id = str(uuid.uuid4())
        self.tasks[task_id] = {
            "status": "pending",
            "payload": payload,
            "result": None,
        }
        return {"task_id": task_id}

    def update_task(self, task_id, result):
        self.tasks[task_id]["result"] = result
        self.tasks[task_id]["status"] = "completed"

    def get_task(self, task_id):
        return self.tasks.get(task_id, None)
