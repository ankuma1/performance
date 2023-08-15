import json

from locust import SequentialTaskSet, task, HttpUser, between


class roomInfo(SequentialTaskSet):

    @task
    def homePage(self):
        response = self.client.get("/branding", name="home page")
        print(response.text)
        print(response.status_code)

    @task
    def sendUserInfo(self):
        messageResponse = self.client.post("/message/", headers={"content-type": "application/json"},
                         data=json.dumps({"name": "anil2222",
                                          "email": "anilk844@gmail.com",
                                          "phone": "63633601232",
                                          "subject": "test test",
                                          "description": "test test test test test test test"
                                          }),
                         name="send message")
        print(messageResponse.text)
        print(messageResponse.status_code)
        print(messageResponse.headers)



class MyUser(HttpUser):
    host = "https://automationintesting.online"
    wait_time = between(2,4)
    tasks = [roomInfo]