from locust import SequentialTaskSet, TaskSet, task, User, between


class UserBehaviour(TaskSet):

    def on_start(self):
        print("login")

    def on_stop(self):
        print("logout")

    @task(2)
    class cart_module(TaskSet):
        @task(4)
        def veiw_cart(self):
            print("view cart")
        @task(2)
        def delete_cart(self):
            print("delete cart")
        @task(1)
        def stop(self):
            print("stop")
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
            print("stop")
            self.interrupt()


class MyUser(User):
    wait_time = between(2,4)
    tasks = [UserBehaviour]


