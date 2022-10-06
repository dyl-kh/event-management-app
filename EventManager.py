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
            print('2. View / Manage Event')
            print('3. Update Event Progress')
            print('0. Log out')

            uIn = input('Please enter your selection: ')
            if uIn == '1':
                self.ViewAllEvents()
            elif uIn == '2':
                self.ViewEventDetails()
            elif uIn == '3':
                self.UpdateEventProgress()
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
                    print('Optional Services:', e['optionalServicesNames'])
                    print(f'Total Price: ${e["totalPrice"]}')

                    # manage event
                    print('Please select an option from the menu below')
                    print('1. Manage event')
                    print('2. Delete event')
                    print('0. Go Back')
                    uIn = input('Please enter your selection: ')
                    if uIn == '1':
                        self.ManageEvent(e)
                        return
                    elif uIn == '2':
                        self.DeleteEvent(e)
                        return
                    elif uIn == '0':
                        active = False
                        break

            else:
                print('Event not found')

    # manage event
    def ManageEvent(self, event):
        print('TO DO manage event')
        pass

    # delete event
    def DeleteEvent(self, event):
        print('Please confirm you wish to delete this event')
        print('Enter 0 to return to the previous menu')
        print('To confirm type DELETE')
        uIn = input('Please enter your selection: ')
        if uIn == '0':
            return
        elif uIn == 'DELETE':
            with open('./storage/events.pkl', 'rb') as f:
                try:
                    events = pickle.load(f)
                except EOFError:
                    events = []

            for e in events:
                if e['id'] == event['id']:
                    e['venue'].unbookDate(e['date'])
                    events.remove(e)
            with open('./storage/events.pkl', 'wb') as f:
                pickle.dump(events, f)
            print('Event deleted')
        else:
            print('Event not deleted')

    # update event progress
    def UpdateEventProgress(self):
        active = True
        while active:
            print('Enter the ID of the event you wish to update')
            print('Enter 0 to return to the previous menu')
            uIn = input('ID: ')
            if uIn == '0':
                return
            with open('./storage/events.pkl', 'rb') as f:
                try:
                    events = pickle.load(f)
                except EOFError:
                    events = []
                    print('No events found')
            for e in events:
                if str(e['id']) == uIn:
                    pass
