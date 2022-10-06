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
            print('4. Log out')

            uIn = input('Please enter your selection: ')
            if uIn == '1':
                self.ViewAllEvents()
            elif uIn == '4':
                print('Logging out')
                open = False
            else:
                print('Invalid input')

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
