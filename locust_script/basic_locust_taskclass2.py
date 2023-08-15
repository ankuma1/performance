from locust import User, between, task, constant,TaskSet
import logging
from datetime import datetime



class MyUser(User):
    wait_time = between(1,2)
    #wait_time = constant(3)
    #tasks = [UserBehaviour]
    @task
    class UserBehaviour(TaskSet):
        logger = logging.getLogger(__name__)
        @task
        def add_cart(self):

            self.logger.info("add to cart")

        @task
        def view_product(self):
            self.logger.info("view the product")
    #tasks = {add_cart:3, view_product:6}