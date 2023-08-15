from locust import User, between, task, constant
from datetime import datetime


def add_cart(userclass):
    print("add to cart")


def view_product(userclass):
    print("view the product")

class MyUser(User):
    wait_time = between(1,2)
    #wait_time = constant(3)
    #tasks = [add_cart,view_product]
    tasks = {add_cart:3, view_product:6}