from locust import User, between, task, constant,TaskSet
from datetime import datetime

class UserBehaviour(TaskSet):
    @task
    def add_cart(self):
        print("add to cart")

    @task
    def view_product(self):
        print("view the product")

class MyUser(User):
    wait_time = between(1,2)
    #wait_time = constant(3)
    tasks = [UserBehaviour]
    #tasks = {add_cart:3, view_product:6}