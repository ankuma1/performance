from locust import User, between


def add_cart(test):
    print("i am adding to cart")

def view_cart(test):
    print("i am viewing the cart")


class myUser(User):
    wait_time = between(2,4)
    tasks = {add_cart:2,view_cart:4}