from locust import User, between, task, constant,SequentialTaskSet,TaskSet
from datetime import datetime

class UserBehaviour(TaskSet):
    @task(2)
    class cart_module(TaskSet):
        @task(4)
        def add_cart(self):
            print("add item in cart")

        @task(2)
        def delete_cart(self):
            print("delete item from cart")

        @task(1)
        def stop(self):
            self.interrupt()

    @task(4)
    class product_module(TaskSet):

        @task(4)
        def view_product(self):
            print("view product")

        @task(2)
        def add_product(self):
            print("add product")

        @task(1)
        def stop(self):
            self.interrupt()

class MyUser(User):
    wait_time = between(1,2)
    #wait_time = constant(3)
    tasks = [UserBehaviour]
    #tasks = {add_cart:3, view_product:6}