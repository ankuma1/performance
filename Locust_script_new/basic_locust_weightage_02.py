import datetime

from locust import HttpUser, between, task, User


class MyWebUser(User):
    wait_time = between(2,4)
    weight = 3

    @task
    def webUser(self):
        print("web user  ",datetime.datetime.now())


class MyMobileUser(User):
    wait_time = between(2, 4)
    weight = 1

    @task
    def webUser(self):
        print("mobile user  ",datetime.datetime.now())
