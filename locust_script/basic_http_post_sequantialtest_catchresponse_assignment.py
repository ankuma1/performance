from locust import HttpUser, task, between, SequentialTaskSet


class userBehaviour(SequentialTaskSet):

    def on_start(self):
        with self.client.get("/v2/pet/findByStatus?status=available", name="available pet details",
                             catch_response=True) as resp:
            print(resp.text)
            if ("doggie") in resp.text:
                resp.success()
            else:
                resp.failure("failed to find key")

    @task()
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
        }, name="add new pet", headers={"accept": "application/json", "Content-Type": "application/json"},
                              catch_response=True) as resp1:
            print(resp1.text)
            if "\":22" in resp1.text:
                resp1.success()
            else:
                resp1.failure("failed to add pet")


    @task()
    def update_pet(self):
        with self.client.post("/v2/store/order", json={"id": 22, "petId": 22,
                                                       "quantity": 1,
                                                       "shipDate": "2022-06-25T07:07:05.562Z",
                                                       "status": "placed",
                                                       "complete": True
                                                       }, name="update pet",
                              headers={"accept": "application/json", "Content-Type": "application/json"},
                              catch_response=True) as resp2:
            print(resp2.text)
            if "\"status\":\"placed\"" in resp2.text:
                pass
            else:
                resp2.failure("failed to update pet ")


class MyUser(HttpUser):
    wait_time = between(1, 2)
    host = "https://petstore.swagger.io"
    tasks = [userBehaviour]
