from locust import events, User, between, task


@events.test_start.add_listener
def script_start(**kwargs):
    print("i am connecting to DB")

@events.test_stop.add_listener
def script_stop(**kwargs):
    print("i am disconnecting DB")


class httpUser(User):
    wait_time = between(2,4)

    def on_start(self):
        print("login")
    @task
    def doing(self):
        print("doing")

    def on_stop(self):
        print("logout")