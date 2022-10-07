from Staff import Staff
import pickle
import json


class EventManager(Staff):
    def __init__(self, role):
        super().__init__(role)
        self.Nav()

    # main menu for event manager
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

                        # manage event
                        print('Please select an option from the menu below')
                        print('1. Edit event')
                        print('2. Delete event')
                        print('0. Go Back')
                        uIn = input('Please enter your selection: ')
                        if uIn == '1':
                            self.EditEvent(e)
                            activeTwo = False
                        elif uIn == '2':
                            if self.DeleteEvent(e):
                                activeTwo = False
                                break

                        elif uIn == '0':
                            active = False
                            break
            else:
                print('Event not found')

    # edit event
    def EditEvent(self, event):
        active = True
        while active:
            print()
            print('Please select an option from the menu below')
            print('1. Edit Package')
            print('2. Edit Venue')
            print('3. Edit Date')
            print('4. Edit Guests')
            print('5. Edit Menu')
            print('6. Edit Optional Services')
            print('0. Go Back')
            print()

            uIn = input('Please enter your selection: ')

            priceUpdate = False
            # edit package
            if uIn == '1':
                old = event['package']
                event['package'] = event['setPackage']()
                # check guests does not exceed package max
                if event['numGuests'] > int(event['package'].maxGuests):
                    event['numGuests'] = int(event['package'].maxGuests)
                    print('Guests have been reduced due to change in package')
                priceUpdate = True
                print(
                    f'Package changed from {old.name} to {event["package"].name}')
            # edit venue
            elif uIn == '2':
                old = event['venue']
                newVenue = event['setVenue']()
                event['venue'] = newVenue
                if old.name == newVenue.name:
                    print('Venue unchanged')
                    return
                # check date is available
                if str(event['date']) in event['venue'].getUnavailableDates():
                    print('Venue is unavailable on this date')
                    event['venue'] = old
                    print('Venue not changed')
                    return
                else:
                    # free up old venue
                    old.unbookDate(event['date'])
                    # book new venue
                    event['venue'].bookDate(event['date'])
                    # undo progress
                    event = event['calculateProgress']('venueBooked', False)
                    event = event['calculateProgress'](
                        'seatingOrganised', False)
                    event['venue'] = newVenue
                    priceUpdate = True
                    print(
                        f'Venue changed from {old.name} to {event["venue"].name}')
            # edit date
            elif uIn == '3':
                old = event['date']
                newDate = event['setDate']()
                event['venue'].bookDate(newDate)
                event['venue'].unbookDate(old)

                event = event['calculateProgress']('venueBooked', False)
                event['date'] = newDate
                print(f'Date changed from {old} to {newDate}')
            # edit guests
            elif uIn == '4':
                old = event['numGuests']
                newGuests = event['setNumGuests']()
                event = event['calculateProgress']('seatingOrganised', False)
                event['numGuests'] = newGuests
                print(f'Guests changed from {old} to {event["numGuests"]}')
            # edit menu
            elif uIn == '5':
                old = event['menu']
                newMenu = event['setMenu']()
                event = event['calculateProgress']('menuOrganised', False)
                event['menu'] = newMenu
                print(f'Menu changed from {old.name} to {event["menu"].name}')
            # edit optional services
            elif uIn == '6':
                with open('./storage/optionalServices.json', 'r') as f:
                    allSelections = json.load(f)
                if 'optionalSelections' in event:
                    currentSelections = event['optionalSelections']
                    currentNames = event['optionalServicesNames']
                else:
                    currentSelections = []
                    currentNames = []
                print()
                print('Toggle optional services')
                done = False
                while not done:
                    print('Please select an option from the menu below')
                    for i, s in enumerate(allSelections):
                        if s['name'] in currentNames:
                            print(f'{i+1}. {s["name"]} Remove')
                        else:
                            print(f'{i+1}. {s["name"]} Add')
                    print('0. Done')
                    print()
                    uIn = input('Please enter your selection: ')
                    if uIn == '0':
                        done = True
                        break
                    elif int(uIn) in range(1, len(allSelections)+1):
                        if allSelections[int(uIn)-1]['name'] in currentNames:
                            currentSelections.remove(
                                allSelections[int(uIn)-1])
                            currentNames.remove(
                                allSelections[int(uIn)-1]['name'])
                        else:
                            currentSelections.append(
                                allSelections[int(uIn)-1])
                            currentNames.append(
                                allSelections[int(uIn)-1]['name'])
                    else:
                        print('Invalid input')

                    newSelections = currentSelections
                    newNames = currentNames

                    print(
                        f'Optional services updated to {newNames}')
                    event = event['calculateProgress'](
                        'optionalServicesOrganised', False)
                    event['optionalSelections'] = newSelections
                    event['optionalServicesNames'] = newNames
                    priceUpdate = True
            # go back
            elif uIn == '0':
                active = False
                return
            else:
                print('Invalid input')

            # update total price
            if priceUpdate:
                event['totalPrice'] = event['calculateTotalPrice'](event)
                print(f'Total Price updated: ${event["totalPrice"]}')

            # replace event in storage
            with open('./storage/events.pkl', 'rb') as f:
                try:
                    events = pickle.load(f)
                except EOFError:
                    events = []

            for i in range(len(events)):
                if events[i]['id'] == event['id']:
                    events[i] = event
                    break

            with open('./storage/events.pkl', 'wb') as f:
                pickle.dump(events, f)
                print('Event detail updated')

    # delete event
    def DeleteEvent(self, event):
        print()
        print('Please confirm you wish to delete this event')
        print('Enter 0 to return to the previous menu')
        print('To confirm type DELETE')
        print()
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
            return True
        else:
            print('Event not deleted')
            return False

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
