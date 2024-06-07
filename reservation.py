# This file contains the code to get information from the user about the reservation.
# Related to FR2

import os
import time
from utils import header

reservationInfo = {
        'firstName': "",
        'lastName': "",
        "roomCode": "",
        "bedType": "",
        "checkIn": "",
        "checkOut": "",
        "children": 0,
        "adults": 0
    }

def reviewReservationInfo():
    # Might want to add more robust error checking here
    print("\nERROR\n")
    if not reservationInfo['firstName'].isalpha():
        print("Invalid First Name")
        return False
    if not reservationInfo['lastName'].isalpha():
        print("Invalid Last Name")
        return False
    if not reservationInfo['roomCode'].isalnum():
        print("Invalid Room Code")
        return False
    if not reservationInfo['bedType'].isalpha():
        print("Invalid Bed Type")
        return False
    if not reservationInfo['checkIn'].isalpha():
        print("Invalid Check In")
        return False
    if not reservationInfo['checkOut'].isalpha():
        print("Invalid Check Out")
        return False
    if not reservationInfo['children'].isdigit():
        print("Invalid Number of Children")
        return False
    if not reservationInfo['adults'].isdigit():
        print("Invalid Number of Adults")
        return False
    return True
    

def confirmReservation():
    os.system('clear')
    header()
    print("Please review your information:")
    print("First Name: " + reservationInfo['firstName'])
    print("Last Name: " + reservationInfo['lastName'])
    print("Room Code: " + reservationInfo['roomCode'])
    print("Bed Type: " + reservationInfo['bedType'])
    print("Check In: " + reservationInfo['checkIn'])
    print("Check Out: " + reservationInfo['checkOut'])
    print("Number of Children: " + reservationInfo['children'])
    print("Number of Adults: " + reservationInfo['adults'])
    print("Is this information correct? (y/n)")
    response = input()
    if response == 'y':
        time.sleep(0.5)
        return True
    else:
        return False

def gatherReservationInfo():
    os.system('clear')
    header()
    print("Welcome to Our Reservation System\n")
    print("NOTE: If you make a mistake, please just keep going, you will be given a chance to review your information before it is submitted")
    print("Please enter the following information to make a reservation:\n")
    reservationInfo['firstName'] = input("First Name: ")
    reservationInfo['lastName'] = input("Last Name: ")
    reservationInfo['roomCode'] = input("Room Code: ")
    reservationInfo['bedType'] = input("Bed Type: ")
    reservationInfo['checkIn'] = input("Check In: ")
    reservationInfo['checkOut'] = input("Check Out: ")
    reservationInfo['children'] = input("Number of Children: ")
    reservationInfo['adults'] = input("Number of Adults: ")

    isValid = reviewReservationInfo()
    
    if isValid:
        confirmation = confirmReservation()
        if confirmation:
            print("Reservation Submitted!")
            return reservationInfo
        else:
            gatherReservationInfo()
    else:
        time.sleep(1)
        gatherReservationInfo()

if __name__ == '__main__' :
    gatherReservationInfo()