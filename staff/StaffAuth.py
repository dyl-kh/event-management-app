import json
from staff.EventManager import EventManager
from staff.Caterer import Caterer
from staff.LogisticsManager import LogisticsManager
from staff.FinanceManager import FinanceManager


class StaffAuth:
    def __init__(self):
        self.username = self.setUsername()
        self.password = self.setPassword()
        self.checkAuth()

    # set username with input
    def setUsername(self):
        valid = False
        while not valid:
            uIn = input('Please enter your username: ')
            if uIn:
                print(f'Username set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    # set password with input
    def setPassword(self):
        valid = False
        while not valid:
            uIn = input('Please enter your password: ')
            if uIn:
                print(f'Password set to {uIn}')
                valid = True
                return uIn
            else:
                print('Invalid input')

    # check if username and password match
    def checkAuth(self):
        with open('./storage/staff.json', 'r') as f:
            staff = json.load(f)
        for s in staff:
            if s['username'] == self.username and s['password'] == self.password:
                if s['role'] == 'Event Manager':
                    EventManager('Event Manager')
                elif s['role'] == 'Caterer':
                    Caterer('Caterer')
                elif s['role'] == 'Logistics Manager':
                    LogisticsManager('Logistics Manager')
                elif s['role'] == 'Finance Manager':
                    FinanceManager('Finance Manager')
