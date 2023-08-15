from locust import SequentialTaskSet, task, User, between


class UserBehaviour(SequentialTaskSet):
    def on_start(self):
        print("i will login")

    @task
    def find_flight(self):
        print("i will find flight by selecting criteria")

    @task
    def select_fligt(self):
        print("select flight")

    @task
    def book_flight(self):
        print("book flight")

class MyUser(User):

    wait_time = between(2,4)
    tasks = [UserBehaviour]
