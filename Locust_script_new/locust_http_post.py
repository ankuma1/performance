import json

from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(2,5)
    host = "https://automationintesting.online"

    @task
    def homePage(self):
        self.client.get("/branding", name="home page")

    @task
    def sendUserInfo(self):
        self.client.post("/message/", headers={"content-type": "application/json"},
                         data=json.dumps({"name": "anil2222",
                                          "email": "anilk844@gmail.com",
                                          "phone": "63633601232",
                                          "subject": "test test",
                                          "description": "test test test test test test test"
                                          }),
                         name="send message")