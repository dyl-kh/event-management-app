import json


class Venue():
    def __init__(self, name):
        self.name = name
        self.address = self.getAddress()
        self.price = self.getPrice()
        self.unavailableDates = self.getUnavailableDates()

    def getAddress(self):
        with open('./storage/venues.json', 'r') as f:
            venues = json.load(f)

        for v in venues:
            if v['name'] == self.name:
                return v['address']
                break

    def getPrice(self):
        with open('./storage/venues.json', 'r') as f:
            venues = json.load(f)

        for v in venues:
            if v['name'] == self.name:
                return v['price']
                break

    def getUnavailableDates(self):
        with open('./storage/venues.json', 'r') as f:
            venues = json.load(f)

        for v in venues:
            if v['name'] == self.name:
                return v['unavailableDates']
                break

    def bookDate(self, date):
        with open('./storage/venues.json', 'r') as f:
            venues = json.load(f)

        for v in venues:
            if v['name'] == self.name:
                v['unavailableDates'].append(str(date))
                break

        file = open('./storage/venues.json', 'w')
        json.dump(venues, file, indent=4)
        file.close()

    def unbookDate(self, date):
        with open('./storage/venues.json', 'r') as f:
            venues = json.load(f)

        for v in venues:
            if v['name'] == self.name:
                v['unavailableDates'].remove(str(date))
                break

        file = open('./storage/venues.json', 'w')
        json.dump(venues, file, indent=4)
        file.close()
