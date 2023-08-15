import json
import sys
import os
Root_Dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(Root_Dir)
from locust import SequentialTaskSet, HttpUser, between
from locust.user import task
from data import CredentialModule
import re


class UserBehaviour(SequentialTaskSet):
    def __init__(self, parent):
        super().__init__(parent)
        self.passwd = None
        self.username = None
        print(parent.host)
        self.jsession__id = ""
        self.user_filter_sessionID = ""
        self.rel = ""

    def on_start(self):

        if len(CredentialModule.credential) > 0:
            self.username, self.passwd = CredentialModule.credential.pop();
            print(self.username)
            print(self.passwd)
            CredentialModule.credential.insert(0, (self.username, self.passwd))
        else:
            print("User list is empty")

        res1 = self.client.get("/InsuranceWebExtJS/index.jsf", name="launch url")
        #print(res1.text)
        self.jsession__id = res1.cookies["JSESSIONID"]
        rel = re.findall("j_id\d+:j_id\d+", res1.text)
        print(rel)


        with self.client.post("/InsuranceWebExtJS/index.jsf", data={"login-form": "login-form",
                                                                    "login-form:email": self.username,
                                                                    "login-form:password": self.passwd,
                                                                    "login-form:login.x": "45",
                                                                    "login-form:login.y": "9",
                                                                    "javax.faces.ViewState": rel[0]},
                              cookies={"JSESSIONID": self.jsession__id}, name="login", catch_response=True) as login:
            print(login.text)
            print(self.username)
            print(self.passwd)
            print("UserSessionFilter.sessionId", login.cookies["UserSessionFilter.sessionId"])
        print(self.jsession__id)

    @task
    def select_autoquote(self):
        with self.client.get("/InsuranceWebExtJS/quote_auto.jsf", cookies={"JSESSIONID": self.jsession__id,
                                                                           "UserSessionFilter.sessionId": self.user_filter_sessionID},
                             name="select auto quote", catch_response=True) as resp3:
            # print(resp3.text)
            if "InsuranceWeb: Automobile Instant Quote" in resp3.text:
                resp3.success()
            else:
                resp3.failure("failed")
            self.rel = re.findall("j_id\d+:j_id\d+", resp3.text)[0]
        # print(resp3)
        print(self.rel)

    @task
    def update_vehicle_details(self):
        with self.client.post("/InsuranceWebExtJS/quote_auto.jsf",
                              headers={"Content-Type": "application/x-www-form-urlencoded"}, data={
                    "autoquote": "autoquote",
                    "autoquote:zipcode": "560098",
                    "autoquote:e-mail": "anilk844@gmail.com",
                    "autoquote:vehicle": "car",
                    "autoquote:next.x": "42",
                    "autoquote:next.y": "8",
                    "javax.faces.ViewState": self.rel},
                              cookies={"JSESSIONID": self.jsession__id,
                                       "UserSessionFilter.sessionId": self.user_filter_sessionID},
                              catch_response=True, name="update vehicle details") as resp4:
            if "Driving Record" in resp4.text:
                resp4.success()
            else:
                resp4.failure("failed")
        self.rel = re.findall("j_id\d+:j_id\d+", resp4.text)[0]
        # print(resp4.text)
        print("update_vehicle_details :  ", self.rel)

    @task
    def update_user_info(self):
        with self.client.post("/InsuranceWebExtJS/quote_auto2.jsf",
                              headers={"Content-Type": "application/x-www-form-urlencoded"},
                              data={"autoquote": "autoquote",
                                    "autoquote:age": "30",
                                    "autoquote:gender": "Male",
                                    "autoquote:type": "Excellent",
                                    "autoquote:next.x": "33",
                                    "autoquote:next.y": "16",
                                    "javax.faces.ViewState": self.rel},
                              cookies={"JSESSIONID": self.jsession__id,
                                       "UserSessionFilter.sessionId": self.user_filter_sessionID},
                              name="update user info",
                              catch_response=True) as resp5:
            self.rel = re.findall("j_id\d+:j_id\d+", resp5.text)[0]
            print("----->", resp5.text)
            print("update user info : ", self.rel)
            if "Financial Info" in resp5.text:
                resp5.success()
            else:
                resp5.failure("failed")
        print(resp5.text)

    @task
    def update_car_model(self):
        with self.client.post("/InsuranceWebExtJS/quote_auto3.jsf",
                              headers={"Content-Type": "application/x-www-form-urlencoded"},
                              data={"autoquote": "autoquote",
                                    "autoquote:year": "2007",
                                    "makeCombo": "Chrysler",
                                    "autoquote:make": "Chrysler",
                                    "modelCombo": "Aspen",
                                    "autoquote:model": "Aspen",
                                    "autoquote:finInfo": "Own",
                                    "autoquote:next.x": "29",
                                    "autoquote:next.y": "13",
                                    "javax.faces.ViewState": self.rel},
                              cookies={"JSESSIONID": self.jsession__id,
                                       "UserSessionFilter.sessionId": self.user_filter_sessionID},
                              catch_response=True, name="update car model") as resp6:
            if "Your Instant Quote is" in resp6.text:
                resp6.success()
            else:
                resp6.failure("failed")

        print(resp6.text)


class MyUser(HttpUser):
    wait_time = between(2, 4)
    host = "https://demo.borland.com"
    tasks = [UserBehaviour]
