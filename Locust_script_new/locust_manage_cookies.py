import json

from locust import SequentialTaskSet, HttpUser, between
from locust.user import task
import re


class UserBehaviour(SequentialTaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        print(parent.host)
        self.jsession__id = ""
        self.user_filter_sessionID = ""
        self.rel = ""

    def on_start(self):
        res1 = self.client.get("/InsuranceWebExtJS/index.jsf", name="launch url")
        print(res1.text)
        self.jsession__id = res1.cookies["JSESSIONID"]
        rel = re.findall("j_id\d+:j_id\d+", res1.text)
        print(rel)

        with self.client.post("/InsuranceWebExtJS/index.jsf", data={"login-form": "login-form",
                                                                    "login-form:email": "anil23089@gmail.com",
                                                                    "login-form:password": "anilk844",
                                                                    "login-form:login.x": "45",
                                                                    "login-form:login.y": "9",
                                                                    "javax.faces.ViewState": rel[0]},
                              cookies={"JSESSIONID": self.jsession__id}, name="login", catch_response=True) as login:
            print("UserSessionFilter.sessionId", login.cookies["UserSessionFilter.sessionId"])
        print(self.jsession__id)

    @task
    def select_autoquote(self):
        with self.client.get("/InsuranceWebExtJS/quote_auto.jsf", cookies={"JSESSIONID": self.jsession__id,
                                                                           "UserSessionFilter.sessionId": self.user_filter_sessionID},
                             name="select auto quote", catch_response=True) as resp3:
            if ("InsuranceWeb: Automobile Instant Quote") in resp3.text:

                resp3.success()
            else:
                resp3.failure("failed")


class MyUser(HttpUser):
    wait_time = between(2, 4)
    host = "https://demo.borland.com"
    tasks = [UserBehaviour]
