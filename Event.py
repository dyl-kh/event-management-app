import pickle
import json
from uuid import uuid4 as uuid
from datetime import date as dateImport
from Package import Package
from Venue import Venue
from Menu import Menu
from Band import Band
from SoundSystem import SoundSystem
from FlowerDecorations import FlowerDecorations
from Customer import Customer
from Finance import Finance


class Event():
    def __init__(self):
        self.id = uuid()
        self.package = self.setPackage()
        self.venue = self.setVenue()
        self.numGuests = self.setNumGuests()
        self.date = self.setDate()
        self.menu = self.setMenu()
        self.optionalSelections = self.setOptionalServices()
        self.totalPrice = self.calculateTotalPrice()
        self.completeBooking()

    # set package with input
    def setPackage(self):
        valid = False
        # get packages
        with open('./storage/packages.json', 'r') as f:
            packages = json.load(f)

        while not valid:
            print('Please select a package')
            i = 1
            validSelections = []
            for p in packages:
                print(
                    f"{i}. {p['name']} : ${p['price']} : Max Guests: {p['maxGuests']}")
                validSelections.append(str(i))
                i += 1
            uIn = input('Please enter your selection: ')
            if uIn in validSelections:
                print(f'{packages[int(uIn) - 1]["name"]} Package selected')
                valid = True
                return Package(packages[int(uIn) - 1]["name"])
            else:
                print('Invalid input')

    # set venue with input
    def setVenue(self):
        with open('./storage/venues.json', 'r') as f:
            venues = json.load(f)
        valid = False
        while not valid:
            print('Please select a venue')
            i = 1
            for v in venues:
                print(
                    f"{i}. {v['name']} : ${v['price']}")
                i += 1
            uIn = input('Please enter your selection: ')
            if uIn == '1':
                print('Hotel selected')
                valid = True
                return Venue('Hotel')
            elif uIn == '2':
                print('Garden selected')
                valid = True
                return Venue('Garden')
            elif uIn == '3':
                print('City Hall selected')
                valid = True
                return Venue('City Hall')
            else:
                print('Invalid input')

    # set numguests from input
    def setNumGuests(self):
        valid = False
        while not valid:
            print('Please enter the number of guests')
            uIn = input('Please enter your selection: ')
            if uIn.isdigit():
                if int(uIn) < int(self.package.maxGuests):
                    valid = True
                    return int(uIn)
                else:
                    print('Number of guests exceeds maximum')
                    print('Choose a different package or reduce guests')
            else:
                print('Invalid input')

    # set date selection from input
    def setDate(self):
        valid = False
        # get current unavailable dates
        while not valid:
            print('Please enter an available date')
            print('Format is yyyy-mm-dd')
            print('Unavailable dates: ', self.venue.unavailableDates)
            uIn = input('Please enter your selection: ')
            if uIn == '1':
                print('Test selected')
                valid = True
                return dateImport(2022, 12, 12)
            # check format of input
            try:
                uIn = dateImport.fromisoformat(uIn)
                # check if date is available
                if str(uIn) not in self.venue.unavailableDates:
                    valid = True
                    return uIn
                else:
                    print('Date is not available')
            except ValueError:
                print('Invalid input')

    # set menu selection from input
    def setMenu(self):
        valid = False
        # get menu prices
        with open('./storage/menus.json', 'r') as f:
            menus = json.load(f)
        while not valid:
            print('Please select a menu')
            i = 1
            for m in menus:
                print(f"{i}. {m['name']} : ${m['pricePerHead']} per head")
                i += 1
            uIn = input('Please enter your selection: ')
            if uIn == '1':
                print('Western menu selected')
                valid = True
                return Menu('Western')
            elif uIn == '2':
                print('Chinese menu selected')
                valid = True
                return Menu('Mexican')
            elif uIn == '3':
                print('Indian menu selected')
                valid = True
                return Menu('Indian')
            else:
                print('Invalid input')

    # set optional services from input
    def setOptionalServices(self):
        valid = False
        while not valid:
            print('Would you like any of the optional services?')
            print('These are a band, sound system, and flower decorations')
            print('1. Yes')
            print('2. No')
            uIn = input('Please enter your selection: ')
            if uIn == '1':
                print('Optional services selected')
                optServ = True
                valid = True
            elif uIn == '2':
                print('No optional services selected')
                optServ = False
                valid = True
            else:
                print('Invalid input')

        # get optional service selection
        if optServ:
            valid = False
            with open('./storage/optionalServices.json', 'r') as f:
                optionalServices = json.load(f)

            optionalSelections = []
            selectedNames = []
            while not valid:
                print('Please select an optional service')
                i = 1
                validSelections = []
                for o in optionalServices:
                    if o['name'] not in selectedNames:
                        print(f"{i}. {o['name']} : ${o['price']}")
                        validSelections.append(i)
                    i += 1

                uIn = input('Please enter your selection: ')
                if int(uIn) in validSelections:
                    print(f'{optionalServices[int(uIn) - 1]["name"]} selected')
                    if uIn == '1':
                        optionalSelections.append(Band('Band'))
                        selectedNames.append('Band')
                    elif uIn == '2':
                        optionalSelections.append(SoundSystem('Sound System'))
                        selectedNames.append('Sound System')
                    elif uIn == '3':
                        optionalSelections.append(
                            FlowerDecorations('Flower Decorations'))
                        selectedNames.append('Flower Decorations')
                    valid = True

                    print('Would you like to add another optional service?')
                    print('1. Yes')
                    print('2. No')
                    uIn = input('Please enter your selection: ')
                    if uIn == '1':
                        valid = False
                    elif uIn == '2':
                        valid = True
                        print('Optional services selected')
                        print('Optional services: ', optionalSelections)
                        return optionalSelections
                else:
                    print('Invalid input')

    # calculate total price
    def calculateTotalPrice(self):
        total = int(self.package.price)
        total += int(self.venue.price)
        total += int(self.menu.pricePerHead) * int(self.numGuests)
        if self.optionalSelections:
            for o in self.optionalSelections:
                total += int(o.price)
        return total

    # print booking details
    def printBookingDetails(self):
        print('Booking Details')
        print('Package: ', self.package.name)
        print('Venue: ', self.venue.name)
        print('Number of guests: ', self.numGuests)
        print('Date: ', self.date)
        print('Menu: ', self.menu.name)
        if self.optionalSelections:
            optionalNames = []
            for o in self.optionalSelections:
                optionalNames.append(o.name)
            print('Optional Services: ', optionalNames)
        else:
            print('Optional Services: None')
        print('Total Price: ', self.totalPrice)

    # save booking details to storage
    def saveEvent(self):

        with open('./storage/events.pkl', 'rb') as f:
            try:
                events = pickle.load(f)
            except EOFError:
                events = []

        print(events)

        event = {
            "id": self.id,
            "package": self.package,
            "venue": self.venue,
            "numGuests": self.numGuests,
            "date": self.date,
            "menu": self.menu,
            "optionalServices": self.optionalSelections,
            "totalPrice": self.totalPrice,
            "paid": True,
        }

        events.append(event)
        with open('./storage/events.pkl', 'wb') as f:
            pickle.dump(events, f, pickle.HIGHEST_PROTOCOL)

    # finalise booking
    def completeBooking(self):
        print('Event details complete')
        self.printBookingDetails()
        print('Now we just need to create your account')
        customer = Customer()
        print(f'Thanks for the information {customer.name}')
        print('Now we need your payment details')
        finance = Finance(customer.id)
        print('Payment details received')
        print(f'Please confirm payment of ${self.totalPrice}')
        valid = False
        while not valid:
            print('1. Confirm')
            print('2. Cancel')
            uIn = input('Please enter your selection: ')
            if uIn == '1':
                finance.processPayment(self.totalPrice)
                print('Booking complete')
                self.saveEvent()
                valid = True
            elif uIn == '2':
                print('Payment cancelled')
                print('Booking cancelled')
                valid = True
            else:
                print('Invalid input')
