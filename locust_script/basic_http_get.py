from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "https://petstore.swagger.io"
    @task
    def lunch_url(self):
        self.client.get("/v2/pet/findByStatus?status=available", name="available pet details")
