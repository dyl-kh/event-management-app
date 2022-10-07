from Staff import Staff
import pickle


class LogisticsManager(Staff):
    def __init__(self, role):
        super().__init__(role)
        self.Nav()

    def Nav(self):
        print('Welcome Logistics Manager')
        open = True
        while open:
            print()
            print('Please select an option from the menu below')
            print('1. View All Events')
            print('2. View Event')
            print('3. Update Event Progress')
            print('0. Logout')
            uIn = input('Please enter your selection: ')

            if uIn == '1':
                print('View All Events')
                self.ViewAllEvents()
            elif uIn == '2':
                print('View Event')
                self.ViewEvent()
            elif uIn == '3':
                print('Update Event Progress')
                self.UpdateEventProgress()
            elif uIn == '0':
                print('Logging out')
                open = False
            else:
                print('Invalid input')

    # View all events
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
            print('Optional Services:', e['optionalServicesNames'])
            print('Date:', e['date'])
            print(f"Progress: {e['eventProgress']}%")

    # View a specific event
    def ViewEvent(self):
        active = True
        while active:
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
                    activeTwo = True
                    while activeTwo:
                        print()
                        print('Package:', e['package'].name)
                        print('Venue:', e['venue'].name)
                        print('Date:', e['date'])
                        print('Guests:', e['numGuests'])
                        print('Menu:', e['menu'].name)
                        print('Optional Services:', e['optionalServicesNames'])
                        print(f'Total Price: ${e["totalPrice"]}')
                        print(f"Progress: {e['eventProgress']}%")
                        print()
                        return

    # Update event progress
    def UpdateEventProgress(self):
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
                        print('1. Optional Services organised')
                        print('0. None')
                        uIn = input('Please enter your selection: ')
                        if uIn == '1':
                            updatedEvent = e['calculateProgress'](
                                'optionalServicesOrganised', True)
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
