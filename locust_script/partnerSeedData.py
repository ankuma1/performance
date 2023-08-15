class partner_seed_data:
    def createPartner(self):
        response=self.client.get("http://fulfillment-service-soeta.dev.dunzo.com/api/v1/supply/d2d9d2b4-76f7-4a41-89a4-1caf5684009f/active_facility")
        print(response)


partner_seed_data().createPartner();