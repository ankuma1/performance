from locust import HttpUser,task,between,SequentialTaskSet


class userBehaviour(SequentialTaskSet):
    @task(1)
    def check_pet_avilable(self):
        resp = self.client.get("/v2/pet/findByStatus?status=available", name="available pet details")
        print(resp.text)

    @task(10)
    def add_pet(self):
        resp1 = self.client.post("/v2/pet", json={
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
        print(resp1.text)


class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "https://petstore.swagger.io"
    tasks = [userBehaviour]

