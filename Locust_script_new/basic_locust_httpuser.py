import datetime
from datetime import datetime
from locust import HttpUser, between, task, constant


class MyHttpUser(HttpUser):
    wait_time = constant(5)
    host = "https://demo.guru99.com/"

    @task
    def home_page(self):
        print(datetime.now())
        print("i am login into the url")


