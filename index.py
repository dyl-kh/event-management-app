#import event.py
from Event import Event
from StaffAuth import StaffAuth

open = True
print('Welcome to Perfect Event Agency')
while open:

    print('Please select an option from the menu below')
    print('1. Create an Event')
    print('2. Track an Event')
    print('3. Staff login')
    print('0. Exit')
    uIn = input('Please enter your selection: ')

    if uIn == '1':
        print('Create an Event')
        Event()
    elif uIn == '2':
        print('Track an Event')
    elif uIn == '3':
        print('Staff login')
        StaffAuth()

    elif uIn == '0':
        print('Goodbye')
        open = False
    else:
        print('Invalid input')
