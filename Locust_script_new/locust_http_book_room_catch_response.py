import json
from pickle import FALSE
import random as rand

from locust import SequentialTaskSet, HttpUser, task, between


class BookRoom(SequentialTaskSet):

    @task
    def goToHomePage(self):
        with self.client.get("/branding", name="home page", catch_response=True) as resp1:
            if("Welcome to Shady Meadows") in resp1.text:
                resp1.success()
            else:
                resp1.failure("room not found")

    @task
    def sendMessage(self):
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

    @task
    def bookRoom(self):
        ranNum = rand.randrange(0, 1000)
        with self.client.post("/booking/",headers = {"content-type": "application/json"},
                              data = json.dumps({"bookingdates": {
                                                "checkin": "2023-08-04",
                                                "checkout": "2023-08-06"
                                                },
                                                "depositpaid": "false",
                                                "firstname": "sunil",
                                                "lastname": "kumat",
                                                "roomid": ranNum,
                                                "email": "anilk843@gmail.com",
                                                "phone": "63633601237"})) as resp3:
            print(resp3.text)
            print(resp3.status_code)



class MyUSer(HttpUser):
    wait_time = between(2,4)
    host = "https://automationintesting.online"
    tasks = [BookRoom]