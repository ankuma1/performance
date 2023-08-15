from locust import User, between, task, constant
from datetime import datetime

class MyUser(User):
    wait_time = between(1,2)
    #wait_time = constant(3)

    @task(2)
    def add_cart(self):
        print("add to cart")

    @task(4)
    def view_product(self):
        print("view the product")
