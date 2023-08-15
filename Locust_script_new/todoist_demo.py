from locust import SequentialTaskSet, task, HttpUser, between
import uuid


class CreateTasks(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.request_id = None

    def on_start(self):
        self.bearerAuth = "b6786a05ea99974c07fd67abb50d6c5e30b247be"
        self.uuid = str(uuid.uuid4())
        res = self.client.post("/rest/v2/projects",
                               headers={"Authorization": "Bearer " + self.bearerAuth,
                                        "Content-Type": "application/json", "X-Request-Id": self.uuid},
                               json={"name": "Project44"}, name="Create Project")
        print(res)
        json_res = res.json()
        print(json_res)
        print(json_res["id"])
        self.request_id = json_res["id"]

    @task
    def create_task(self):
        res2 = self.client.post("/rest/v2/tasks",
                                json={"content": "My appointment",
                                      "due_lang": "en",
                                      "project_id": self.request_id
                                      },
                                headers={"Authorization": "Bearer " + self.bearerAuth,
                                    "Content-Type": "application/json", "X-Request-Id": self.request_id}, name= "create task")
        print(res2.text)
        json_res2 = res2.json()
        print(json_res2)
        print(json_res2["id"])
        self.taskId = json_res2["id"]

    @task
    def close_task(self):
        print("close task "+self.taskId)
        with self.client.post("/rest/v2/tasks/"+self.taskId+"/close", headers={"Authorization": "Bearer " + self.bearerAuth},
                              name ="close task",catch_response=True) as closeTaskResponse:
            print(closeTaskResponse.text)





class MyHttpUser(HttpUser):
    wait_time = between(2, 4)
    host = "https://api.todoist.com"
    tasks = [CreateTasks]
