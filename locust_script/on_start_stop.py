from locust import User,task,between

class MyUser(User):
    wait_time = between(1,2)

    def on_start(self):
        print("login")

    @task
    def doing_work(self):
        print("login into web")


    def on_stop(self):
        print("logout")