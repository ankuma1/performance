from locust import User, between, task


class httpUser(User):
    wait_time = between(2,4)

    @task(2)
    def add_cart(self):
        print( " i am adding to cart")

    @task(4)
    def view_product(self):
        print("i am viewing the cart")
