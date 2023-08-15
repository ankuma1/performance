from locust import User, between, task, constant
from datetime import datetime

class MyUser(User):
    #wait_time = between(1,3)
    wait_time = constant(3)

    @task
    def user_login(self):
        print(datetime.now())
