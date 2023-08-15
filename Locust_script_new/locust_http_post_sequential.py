from locust import SequentialTaskSet, task, HttpUser, between


class roomInfo(SequentialTaskSet):

    @task
    def homePage(self):
        self.client.get("/branding", name="home page")

    @task
    def sendUserInfo(self):
        self.client.post("/message", data={"name": "anil",
                                           "email": "anilk844@gmail.com",
                                           "phone": "63633601232",
                                           "subject": "test test",
                                           "description": "test test test test test test test"
                                           },
                         name="send message")


class MyUser(HttpUser):
    host = "https://automationintesting.online"
    wait_time = between(2,4)
    tasks = [roomInfo]