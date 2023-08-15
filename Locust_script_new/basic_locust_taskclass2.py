from locust import TaskSet, task, User, between


class UserBehaviour(TaskSet):

    @task()
    def add_cart(self):
        print("add item to cart")

    @task()
    def view_cart(self):
        print("view the cart")


class MyUser(User):
    wait_time = between(2,4)
    tasks = [UserBehaviour]
