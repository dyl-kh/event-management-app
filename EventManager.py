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
            print()
            print('Please select an option from the menu below')
            print('1. View all events')
            print('2. View / Edit / Delete Event')
            print('3. Update Event Progress')
            print('0. Log out')

            uIn = input('Please enter your selection: ')
            if uIn == '1':
                self.ViewAllEvents()
            elif uIn == '2':
                self.ViewEventDetails()
            elif uIn == '3':
                self.EventProgress()
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
            print(f"Progress: {e['eventProgress']}%")

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
                    print('1. Edit event')
                    print('2. Delete event')
                    print('0. Go Back')
                    uIn = input('Please enter your selection: ')
                    if uIn == '1':
                        self.EditEvent(e)
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
    def EditEvent(self, event):
        print('TO DO edit event')
        pass

    # delete event
    def DeleteEvent(self, event):
        print()
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
    def EventProgress(self):
        active = True
        while active:
            print()
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
                    valid = False
                    while not valid:
                        print()
                        print(f'Current progress: {e["eventProgress"]}%')
                        print(
                            'If any of the following tasks have been completed, please enter the number of the task')
                        print(
                            'If none of the following tasks have been completed, please enter 0')
                        print()
                        print('1. Venue booked')
                        print('2. Seating Organised')
                        print('0. None')
                        uIn = input('Please enter your selection: ')
                        if uIn == '1':
                            updatedEvent = e['calculateProgress'](
                                'venueBooked', True)
                            valid = True
                        elif uIn == '2':
                            updatedEvent = e['calculateProgress'](
                                'seatingOrganised', True)
                            valid = True
                        elif uIn == '0':
                            return
                        else:
                            print('Invalid input')

                    # replace event in list
                    for i in range(len(events)):
                        if events[i]['id'] == e['id']:
                            events[i] = updatedEvent
                    with open('./storage/events.pkl', 'wb') as f:
                        pickle.dump(events, f)
                        print('Event progress updated')
                        print(
                            f'New progress: {updatedEvent["eventProgress"]}%')
                        return
