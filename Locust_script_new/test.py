import json

from locust import Locust, User, task, HttpUser, between


class myClass(HttpUser):
    wait_time = between(1, 3)
    host = "https://automationintesting.online"
    @task
    def calltest(self):
        print("anil")
        messageResponse = self.client.post("/message/", headers={"content-type": "application/json"}, data=json.dumps({"name": "anil2222",
                                                         "email": "anilk844@gmail.com",
                                                         "phone": "63633601232",
                                                         "subject": "test test",
                                                         "description": "test test test test test test test"
                                                         }),
                                       name="send message")
        print(messageResponse.text)
        print(messageResponse.status_code)


