from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://petstore.swagger.io"

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)
        self.value = None

    @task(4)
    def check_pet_avilable(self):
        self.value = 10
        self.client.get("/v2/pet/findByStatus?status=available", name="available pet details")

    @task(1)
    def add_pet(self):
        print(self.value)
        self.client.post("/v2/pet", json={
            "id": 22,
            "category": {
                "id": 1,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 1,
                    "name": "string"
                }
            ],
            "status": "available"
        }, name="add new pet", headers={"accept": "application/json", "Content-Type": "application/json"})
