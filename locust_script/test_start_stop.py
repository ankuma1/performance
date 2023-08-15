from locust import User,task,between,events

@events.test_start.add_listener
def script_start(**kwargs):
    print("connecting to db")

@events.test_stop.add_listener
def script_stop(**kwargs):
    print("disconnecting from db")

class MyUser(User):
    wait_time = between(1,2)

    def on_start(self):
        print("login")

    @task
    def doing_work(self):
        print("login into web")


    def on_stop(self):
        print("logout")