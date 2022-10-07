from staff.Staff import Staff
import pickle
import json


class FinanceManager(Staff):
    def __init__(self, role):
        super().__init__(role)
        self.Nav()

    def Nav(self):
        print('Welcome Finance Manager')
        open = True
        while open:
            print()
            print('Please select an option from the menu below')
            print('1. View all events')
            print('2. View Event Financial Information')
            print('0. Log out')

            uIn = input('Please enter your selection: ')
            if uIn == '1':
                self.ViewAllEvents()
            elif uIn == '2':
                self.ViewFinancialInformation()
            elif uIn == '0':
                print('Logging out')
                open = False
            else:
                print('Invalid input')

# quick glance at all events
    def ViewAllEvents(self):
        with open('./storage/events.pkl', 'rb') as f:
            try:
                events = pickle.load(f)
            except EOFError:
                events = []
                print('No events found')

        if len(events) == 0:
            print('No events found')
            return

        for e in events:
            menuBudget = int(e['menu'].pricePerHead) * \
                int(e['numGuests']) * 0.8
            venueBudget = int(e['venue'].price) * 0.8
            logisticsTotal = 0
            logisticsBudget = 0
            if e['optionalSelections']:
                for o in e['optionalSelections']:
                    logisticsTotal += int(o.price)
                logisticsBudget = logisticsTotal * 0.8
            totalBudget = menuBudget + venueBudget + logisticsBudget
            profit = int(e['totalPrice']) - totalBudget
            print(e)
            print('')
            print('ID:', e['id'])
            print('Package', e['package'].name)
            print('Date:', e['date'])
            print(f"Total Budget: ${totalBudget}")
            print(f"Profit: ${profit}")
            print(f"Total Price: ${e['totalPrice']}")
# view financial information for a specific event

    def ViewFinancialInformation(self):
        active = True
        while active:
            print()
            print('Please enter the ID of the event you wish to view')
            print('Enter 0 to return to the previous menu')
            uIn = input('ID: ')
            if uIn == '0':
                active = False
                break

            with open('./storage/events.pkl', 'rb') as f:
                print('running')
                try:
                    events = pickle.load(f)
                except EOFError:
                    events = []
                    print('No events found')
            for e in events:
                if str(e['id']) == uIn:
                    menuBudget = int(e['menu'].pricePerHead) * \
                        int(e['numGuests']) * 0.8
                    venueBudget = int(e['venue'].price) * 0.8
                    logisticsTotal = 0
                    logisticsBudget = 0
                    if e['optionalSelections']:
                        for o in e['optionalSelections']:
                            logisticsTotal += int(o.price)
                        logisticsBudget = logisticsTotal * 0.8
                    totalBudget = menuBudget + venueBudget + logisticsBudget
                    profit = int(e['totalPrice']) - totalBudget
                    activeTwo = True
                    while activeTwo:
                        print()
                        print(
                            f"Package: {e['package'].name} : ${e['package'].price}")
                        print(
                            f"Venue: {e['venue'].name} : ${e['venue'].price}")
                        print(f"Venue Budget: ${venueBudget}")
                        print(
                            f"Menu: {e['menu'].name} : ${int(e['menu'].pricePerHead) * int(e['numGuests'])}")
                        print(f"Menu Budget: ${menuBudget}")
                        if(e['optionalSelections']):
                            print('Logistics:')
                            for o in e['optionalSelections']:
                                print(f"{o.name} : ${o.price}")
                        print(f"Logistics Budget: ${logisticsBudget}")
                        print(f"Profit: ${profit}")
                        print(f"Total Price: ${e['totalPrice']}")
                        activeTwo = False
                    break
            else:
                print('No event found with that ID')
