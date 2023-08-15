from locust import User, between, task, constant
from datetime import datetime

class MyWebUser(User):
    wait_time = between(1,3)
    #wait_time = constant(3)
    weight = 3
    @task
    def user_login(self):
        print("i am login into web")

class MyMobileUser(User):
    wait_time = between(1,3)
    #wait_time = constant(3)
    weight = 1
    @task
    def user_login(self):
        print("i am login into mobile")
