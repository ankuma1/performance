from locust import HttpUser,task,between,SequentialTaskSet


class userBehaviour(SequentialTaskSet):
    @task(1)
    def check_pet_avilable(self):
        with self.client.get("/v2/pet/findByStatus?status=available", name="available pet details", catch_response=True) as resp:
            print(resp.text)
            if("doggie") in resp.text:
                resp.success()
            else:
                resp.failure("failed to find key")

    @task(10)
    def add_pet(self):
        with self.client.post("/v2/pet", json={
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
        }, name="add new pet", headers={"accept": "application/json", "Content-Type": "application/json"}, catch_response=True) as resp1:
            print(resp1.text)
            if "\":22\"" in resp1.text:
                resp1.success()
            else:
                resp1.failure("failed to find key")



class MyUser(HttpUser):
    wait_time = between(1,2)
    host = "https://petstore.swagger.io"
    tasks = [userBehaviour]

