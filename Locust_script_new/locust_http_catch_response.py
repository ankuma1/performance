import json

from locust import SequentialTaskSet, task, HttpUser, between


class roomInfo(SequentialTaskSet):

    @task
    def homePage(self):
        with self.client.get("/branding", name="home page", catch_response=True) as resp1:
            if("Welcome to Shady Meadows") in resp1.text:
                resp1.success()
            else:
                resp1.failure("failed to login")

    @task
    def sendUserInfo(self):
       with self.client.post("/message/", headers={"content-type": "application/json"},
                                           data=json.dumps({"name": "anil2222",
                                                            "email": "anilk844@gmail.com",
                                                            "phone": "63633601232",
                                                            "subject": "test test",
                                                            "description": "test test test test test test test"
                                                            }),
                                           name="send message",catch_response=True) as resp2:
            if("anil2223") in resp2.text:
                resp2.success()
            else:
                resp2.failure("text not found in post call response")
            #print(resp2.status_code)
            #print(resp2.headers)


class MyUser(HttpUser):
    host = "https://automationintesting.online"
    wait_time = between(2, 4)
    tasks = [roomInfo]