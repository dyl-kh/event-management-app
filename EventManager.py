from Staff import Staff
import pickle


class EventManager(Staff):
    def __init__(self, role):
        super().__init__(role)
        self.Nav()

    def Nav(self):
        print('Welcome Event Manager')
        open = True
        while open:
            print('Please select an option from the menu below')
            print('1. View all events')
            print('2. View event details')
            print('0. Log out')

            uIn = input('Please enter your selection: ')
            if uIn == '1':
                self.ViewAllEvents()
            if uIn == '2':
                self.ViewEventDetails()
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

        for e in events:
            print('')
            print('ID:', e['id'])
            print('Venue:', e['venue'].name)
            print('Date:', e['date'])

    # view and manage single events

    def ViewEventDetails(self):
        active = True
        while active:
            print('Please enter the ID of the event you wish to view')
            print('Enter 0 to return to the previous menu')
            uIn = input('ID: ')
            if uIn == '0':
                active = False
                break

            with open('./storage/events.pkl', 'rb') as f:
                try:
                    events = pickle.load(f)
                except EOFError:
                    events = []
                    print('No events found')
            for e in events:
                if str(e['id']) == uIn:
                    print('Package:', e['package'].name)
                    print('Venue:', e['venue'].name)
                    print('Date:', e['date'])
                    print('Guests:', e['numGuests'])
                    print('Menu:', e['menu'].name)
                    optionalNames = []
                    for o in e['optionalServices']:
                        optionalNames.append(o.name)
                    print('Optional Services:', optionalNames)
                    print(f'Total Price: ${e["totalPrice"]}')

                    # manage event
                    print('Please select an option from the menu below')
                    print('1. Manage event')
                    print('2. Delete event')
                    print('0. Go Back')
                    uIn = input('Please enter your selection: ')
                    if uIn == '1':
                        self.ManageEvent(e)
                    elif uIn == '2':
                        self.DeleteEvent(e)
                    elif uIn == '0':
                        active = False
                        break

                else:
                    print('Event not found')

    # manage event
    def ManageEvent(self, event):
        print('manage event')
        pass

    # delete event
    def DeleteEvent(self, event):
        print('delete event')
        pass
