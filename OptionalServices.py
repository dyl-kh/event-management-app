import json


class OptionalServices:
    def __init__(self, name):
        self.name = name
        self.price = self.getPrice()

    def getPrice(self):
        with open('./storage/optionalServices.json', 'r') as f:
            optionalServices = json.load(f)
        for service in optionalServices:
            if service['name'] == self.name:
                return service['price']
