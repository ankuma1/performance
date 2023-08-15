import logging
import sys
import os
from locust import SequentialTaskSet, HttpUser, between
from locust.user import task
from locust.exception import StopUser
import re

Root_Dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Root_Dir)
from utility.readCsvFile import ReadCsvFile

data_folder = os.path.join(Root_Dir, "data")
file_path = os.path.join(data_folder, "credential.csv")

logger = logging.getLogger(__name__)


class UserBehaviour(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.passwd = None
        self.username = None
        logger.info(parent.host)
        self.jsession__id = ""
        self.user_filter_sessionID = ""
        self.rel = ""

    def on_start(self):

        if len(self.parent.reader1) > 0:
            reader2 = self.parent.reader1.pop()
            self.username = reader2["username"]
            self.passwd = reader2["password"]
            logger.info(self.username)
            logger.info(self.passwd)
            self.parent.reader1.insert(0, {"username": self.username, "password": self.passwd})
        else:
            logger.info("User list is empty")

        with self.client.get("/InsuranceWebExtJS/index.jsf", name="launch url",catch_response=True) as res1:
            # print(res1.text)
            if("JSESSIONID" in res1.text):
                res1.success()
            else:
                res1.failure("faild lunch url")
                self.parent.environment.runner.quit()

            self.jsession__id = res1.cookies["JSESSIONID"]
            rel = re.findall("j_id\d+:j_id\d+", res1.text)
            logger.info(rel)

        with self.client.post("/InsuranceWebExtJS/index.jsf", data={"login-form": "login-form",
                                                                    "login-form:email": self.username,
                                                                    "login-form:password": self.passwd,
                                                                    "login-form:login.x": "45",
                                                                    "login-form:login.y": "9",
                                                                    "javax.faces.ViewState": rel[0]},
                              cookies={"JSESSIONID": self.jsession__id}, name="login", catch_response=True) as login:
            logger.info(login.text)
            logger.info(self.username)
            logger.info(self.passwd)
            logger.info("UserSessionFilter.sessionId", login.cookies["UserSessionFilter.sessionId"])
        logger.info(self.jsession__id)

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
                raise StopUser()
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
            logger.info("----->" + resp5.text)
            logger.info("update user info : " + self.rel)
            if "Financial Info" in resp5.text:
                resp5.success()
            else:
                resp5.failure("failed")
        logger.info(resp5.text)

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

        logger.info(resp6.text)


class MyUser(HttpUser):
    wait_time = between(2, 4)
    tasks = [UserBehaviour]
    reader1 = ReadCsvFile(file_path).reader()
    logger.info(reader1)
