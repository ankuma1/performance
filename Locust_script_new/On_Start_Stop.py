from locust import User, between, task


class myHttpUser(User):
    wait_time = between(2,4)

    def on_start(self):
        print("login")

    @task
    def doing(self):
        print("doing work")

    def on_stop(self):
        print("loging out")