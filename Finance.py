from uuid import uuid4 as uuid
import json


class Finance():
    def __init__(self, customerId):
        self.id = uuid()
        self.customerId = customerId
        self.cardNumber = self.setCardNumber()
        self.cardExpiry = self.setCardExpiry()
        self.cardCvv = self.setCardCvv()
        self.saveFinance()

    # set card number with input
    def setCardNumber(self):
        valid = False
        while not valid:
            uIn = input('Please enter your card number: ')
            if uIn:
                print(f'Card number set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    # set card expiry with input
    def setCardExpiry(self):
        valid = False
        while not valid:
            uIn = input('Please enter your card expiry: ')
            if uIn:
                print(f'Card expiry set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    # set card cvv with input
    def setCardCvv(self):
        valid = False
        while not valid:
            uIn = input('Please enter your card cvv: ')
            if uIn:
                print(f'Card cvv set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    # save finance to json
    def saveFinance(self):
        with open('./storage/finances.json', 'r') as f:
            finance = json.load(f)
        finance.append({
            'id': str(self.id),
            'customerId': str(self.customerId),
            'cardNumber': self.cardNumber,
            'cardExpiry': self.cardExpiry,
            'cardCvv': self.cardCvv
        })
        with open('./storage/finances.json', 'w') as f:
            json.dump(finance, f, indent=4)

    def processPayment(self, totalPrice):
        print('Processing payment')
        print(f'Payment of ${totalPrice} successful')
        return True
