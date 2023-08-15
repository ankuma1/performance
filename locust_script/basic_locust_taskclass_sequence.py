from locust import User, between, task, constant,SequentialTaskSet
from datetime import datetime

class UserBehaviour(SequentialTaskSet):
    def on_start(self):
        print("i will login into site")
    @task
    def flight_finder(self):
        print("flight finder")

    @task
    def select_flight(self):
        print("select flight")

    @task
    def book_flight(self):
        print("book flight")

class MyUser(User):
    wait_time = between(1,2)
    #wait_time = constant(3)
    tasks = [UserBehaviour]
    #tasks = {add_cart:3, view_product:6}