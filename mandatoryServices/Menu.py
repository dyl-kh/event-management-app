import json


class Menu():
    def __init__(self, name):
        self.name = name
        self.pricePerHead = self.getPricePerHead()

    def getPricePerHead(self):
        with open('./storage/menus.json', 'r') as f:
            menus = json.load(f)

        for m in menus:
            if m['name'] == self.name:
                return m['pricePerHead']
