from locust import SequentialTaskSet, TaskSet, task, User, between


class UserBehaviour(TaskSet):

    def on_start(self):
        print("login")

    def on_stop(self):
        print("logout")

    @task(2)
    class cart_module(TaskSet):
        @task
        def veiw_cart(self):
            print("view cart")
        @task
        def delete_cart(self):
            print("delete cart")
    @task(4)
    class product_module(TaskSet):

        @task
        def view_product(self):
            print("view product")

        @task
        def add_product(self):
            print("add product")


class MyUser(User):
    wait_time = between(2,4)
    tasks = [UserBehaviour]


