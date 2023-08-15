from locust import User, between, task


class MyUser(User):
    wait_time = between(2,4)

    @task
    def login_url(self):
        print("welcome to bangalore")
