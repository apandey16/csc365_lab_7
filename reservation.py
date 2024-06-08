# This file contains the code to get information from the user about the reservation.
# Related to FR2

import os
import time
from utils import *
from commands import *

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

reservationSearchInfo = {
        'firstName': "",
        'lastName': "",
        "startDate": "",
        "endDate": "",
        "roomCode": "",
        "reservationCode": ""
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

def cancelReservation():
    os.system('clear')
    header()
    print("Reservation Cancelation\n") 

    while True:

        resCode = input("Please enter the reservation code to cancel a reservation:\n")

        if resCode.isalnum():
            return resCode
        else:
            print("Invalid reservation code. Please try again.")
            time.sleep(1)


def collectDetailedReservationInfo():
    os.system('clear')
    header()
    print("Search for a reservation using the following fields. \n")
    print("You may fill in as many or as few fields as you would like to search by. \n")
    print("Leaving all fields blank with return all reservations \n")

    reservationSearchInfo['firstName'] = input("First Name: ")
    reservationSearchInfo['lastName'] = input("Last Name: ")
    reservationSearchInfo['startDate'] = input("Start Date (Inclusive): ")
    reservationSearchInfo['endDate'] = input("End Date (Inclusive): ")
    reservationSearchInfo['roomCode'] = input("Room Code: ")
    reservationSearchInfo['reservationCode'] = input("Reservation Code: ")

    # isValid = reviewDetailedReservationInfo()

    # if isValid:
    confirmation = confirmDetailedReservation()
    if confirmation:
        return reservationSearchInfo
    else:
        collectDetailedReservationInfo()
    # else:
    #     time.sleep(1)
    #     collectDetailedReservationInfo()


# def reviewDetailedReservationInfo():
#     if reservationSearchInfo['firstName'] == '\n' or (not reservationSearchInfo['firstName'].isalpha()):
#         print("Invalid First Name")
#         return False
#     if not reservationSearchInfo['lastName'].isalpha():
#         print("Invalid Last Name")
#         return False
#     if not reservationSearchInfo['roomCode'].isalnum():
#         print("Invalid Room Code")
#         return False
#     if not reservationSearchInfo['reservationCode'].isalpha():
#         print("Invalid Reservation Code Type")
#         return False
#     if not reservationSearchInfo['startDate'].isalpha():
#         print("Invalid Start Date")
#         return False
#     if not reservationSearchInfo['endDate'].isalpha():
#         print("Invalid End Date")
#         return False
#     return True
    
def confirmDetailedReservation():
    os.system('clear')
    header()
    print("Please review your search info:")
    print("First Name: " + reservationSearchInfo['firstName'])
    print("Last Name: " + reservationSearchInfo['lastName'])
    print("Start Date: " + reservationSearchInfo['startDate'])
    print("End Date: " + reservationSearchInfo['endDate'])
    print("Room Code: " + reservationSearchInfo['roomCode'])
    print("Reservation " + reservationSearchInfo['reservationCode'])
    print("Is this information correct? (y/n)")
    response = input()
    if response == 'y':
        time.sleep(0.5)
        return True
    else:
        return False

def collectRevenueData(connector):
    os.system('clear')
    roomToTuple = {
        'AOB': 0,
        'CAS': 1,
        'FNA': 2,
        'HBB': 3,
        'IBD': 4,
        'IBS': 5,
        'MWC': 6,
        'RND': 7,
        'RTE': 8,
        'TAA': 9
    }
    revByRoom = [
        ['AOB', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['CAS', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['FNA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['HBB', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['IBD', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['IBS', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['MWC', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['RND', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['RTE', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['TAA', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['Total', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    results = executeQuery(connector, gatherRevenue)
    months =['Room', 'Jan', 'Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Yearly\n']
    for i in months:
        print(i, end="\t")
    print("")
    for row in results:
        room = row[0]
        month = row[1]
        monthlyRev = row[2]
        revByRoom[roomToTuple.get(room)][month] = monthlyRev
        revByRoom[10][month] += monthlyRev
        revByRoom[roomToTuple.get(room)][13] += monthlyRev 
        revByRoom[10][13] += monthlyRev
    for room in revByRoom[:10]:
        for item in room:
            print(item, end="\t")
        print("")
        print("\n", end="")

    for item in revByRoom[10]:
        print(item, end=" ")
    print("")
    header()
    

if __name__ == '__main__' :
    gatherReservationInfo()