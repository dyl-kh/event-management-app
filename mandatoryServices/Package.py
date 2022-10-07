import json


class Package():
    def __init__(self, name):
        self.name = name
        self.maxGuests = self.getMaxGuests()
        self.price = self.getPrice()

    def getMaxGuests(self):
        with open('./storage/packages.json', 'r') as f:
            packages = json.load(f)
        for p in packages:
            if p['name'] == self.name:
                return p['maxGuests']

    def getPrice(self):
        with open('./storage/packages.json', 'r') as f:
            packages = json.load(f)
        for p in packages:
            if p['name'] == self.name:
                return p['price']
