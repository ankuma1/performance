from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://newtours.demoaut.com/"

    @task
    def login_url(self):
        print("login into url")
