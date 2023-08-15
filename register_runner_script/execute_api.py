import math

from locust import HttpUser, between, task, constant, TaskSet, SequentialTaskSet, LoadTestShape
from datetime import datetime
from locust.exception import StopUser
import util


# curl -X POST -H "Content-Type: application/json" --data $'{"username":"mukund@dunzo.in","password":"admin123"}' http://espresso-mvpv2rts.dev.dunzo.com/api/v1/auth/web-auth/
class register(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)

    @task()
    def get_operator_auth(self):
        value = self.parent.data.pop()
        print(value)
        self.parent.data.insert(0, {"username": value.get("username"), "password": value.get("password")})
        print(self.parent.data)

        with self.client.post("/api/v1/auth/web-auth/",
                              json={"username": value.get("username"),
                                    "password": value.get("password")},
                              headers={"Content-Type": "application/json"}, catch_response=True) as oper_auth:
            print(oper_auth.json().get("data").get("token"))

            if "\"code\":\"200\"" in oper_auth.text:
                oper_auth.success()
                # print(oper_auth.json())
            else:
                oper_auth.failure()
                raise StopUser()
                #self.parent.environment.runner.quit()




class MyUser(HttpUser):
    wait_time = between(1, 4)
    data = util.get_operator_credential()
    print(data)
   #host = "http://espresso-test.dev.dunzo.com"
    # wait_time = constant(3)
    tasks = [register]
    # tasks = {add_cart:3, view_product:6}


class StepLoadShape(LoadTestShape):
    """
    A step load shape
    Keyword arguments:
        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds
    """

    step_time = 30
    step_load = 10
    spawn_rate=1
    cd = 10
    time_limit = 600

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)
