from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(2,5)
    host = "https://automationintesting.online"

    @task
    def get_call(self):
        self.client.get("/branding", name="home page")