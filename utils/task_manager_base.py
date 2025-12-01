import requests


class TaskManagerBase:
    def __init__(self, api_url="http://0.0.0.0:10001"):
        self.api_url = api_url.rstrip("/")

    def create_task(self, payload: dict):
        url = f"{self.api_url}/task"
        r = requests.post(url, json=payload)
        r.raise_for_status()
        return r.json()

    def execute_task(self, task_id: str):
        url = f"{self.api_url}/task/{task_id}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
