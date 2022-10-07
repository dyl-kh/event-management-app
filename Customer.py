from uuid import uuid4 as uuid
import json


class Customer():
    def __init__(self):
        self.id = uuid()
        self.name = self.setName()
        self.email = self.setEmail()
        self.phone = self.setPhone()
        self.address = self.setAddress()
        self.events = self.getEvents()
        self.saveCustomer()

    # set name with input
    def setName(self):
        valid = False
        while not valid:
            uIn = input('Please enter your name: ')
            if uIn:
                print(f'Name set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    # set email with input
    def setEmail(self):
        valid = False
        while not valid:
            uIn = input('Please enter your email: ')
            if uIn:
                print(f'Email set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    # set phone with input
    def setPhone(self):
        valid = False
        while not valid:
            uIn = input('Please enter your phone number: ')
            if uIn:
                print(f'Phone number set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    # set address with input
    def setAddress(self):
        valid = False
        while not valid:
            uIn = input('Please enter your address: ')
            if uIn:
                print(f'Address set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    def getEvents(self):
        pass

    def saveCustomer(self):
        with open('./storage/customers.json', 'r') as f:
            customers = json.load(f)

        customer = {'id': str(self.id), 'name': self.name, 'email': self.email,
                    'phone': self.phone, 'address': self.address}
        customers.append(customer)
        with open('./storage/customers.json', 'w') as f:
            json.dump(customers, f, indent=4)
