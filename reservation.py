# This file contains the code to get information from the user about the reservation.
# Related to FR1, FR2, FR5
# Add pretty table import

import os
import time
import re
from utils import *
from commands import *
from prettytable import PrettyTable

def gatherRoomInfo(connector):
    os.system('clear')
    results = executeQuery(connector, gatherRoomsList)
    table = PrettyTable()
    table.field_names = ["Room", "Room Name", "Beds", "Bed Type", "Maximum Occupancy", "Base Price", "Decor", "Popularity", "Earliest Opening", "Length Of Most Recent Stay"]
    for row in results:
        table.add_row(row)
    print(table)
    header()

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
    regex = re.compile(r"^\d{4}-\d{2}-\d{2}$")
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
    try:
        regex.match(reservationInfo["checkIn"])
        regex.match(reservationInfo["checkOut"])
        if reservationInfo['checkIn'] > reservationInfo['checkOut']:
            print("Invalid Date Range")
            return False
    except:
        print("Invalid Date Format for CheckIn or CheckOut")
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

def gatherReservationInfo(connector):
    os.system('clear')
    header()
    print("Welcome to Our Reservation System\n")
    print("NOTE: If you make a mistake, please just keep going, you will be given a chance to review your information before it is submitted")
    print("Please enter the following information to make a reservation:\n")
    reservationInfo['firstName'] = input("First Name: ")
    reservationInfo['lastName'] = input("Last Name: ")
    reservationInfo['roomCode'] = input("Room Code (or Any for no preference): ")
    reservationInfo['bedType'] = input("Bed Type (or Any for no preference): ")
    reservationInfo['checkIn'] = input("Check In (yyyy-mm-dd): ")
    reservationInfo['checkOut'] = input("Check Out (yyyy-mm-dd): ")
    reservationInfo['children'] = input("Number of Children: ")
    reservationInfo['adults'] = input("Number of Adults: ")

    isValid = reviewReservationInfo()
    totalPeople = int(reservationInfo['children']) + int(reservationInfo['adults'])

    if isValid:
        # Add DB query here
        query = """
                with occRooms as (
                    select *
                    from 
                        lab7_reservations re join lab7_rooms ro on ro.RoomCode = re.Room 
                    where
                        re.CheckIn < \'%s\'
                        AND re.CheckOut > \'%s\'
                )
                select * 
                from
                    lab7_rooms r1
                where
                    not exists
                    (
                        select * 
                        from occRooms o
                        where o.RoomCode = r1.RoomCode
                    )
                    and %d < r1.maxOcc
                    and r1.RoomCode like \'%s\'
                    and r1.BedType like \'%s\'
            """
        if reservationInfo['roomCode'] == 'Any':
            reservationInfo['roomCode'] = '%'
        if reservationInfo['bedType'] == 'Any':
            reservationInfo['bedType'] = '%'

        results = executeQuery(connector, query % (reservationInfo['checkOut'], reservationInfo['checkIn'], totalPeople, reservationInfo['roomCode'], reservationInfo['bedType']))

        print(results)

        confirmation = confirmReservation()
        if confirmation:
            print("Reservation Submitted!")
            return reservationInfo
        else:
            gatherReservationInfo()
    else:
        time.sleep(1)
        gatherReservationInfo()

def cancelReservation(connector):
    os.system('clear')
    header()
    print("Reservation Cancelation\n") 

    while True:

        resCode = input("Please enter the reservation code to cancel a reservation:\n")

        if resCode.isnumeric():
            confirmation = input("Are you sure you want to try to cancel reservation " + resCode + "? (y/n)\n")
            if confirmation == 'y':
                print("Processing...")
                try:
                    query = "DELETE FROM lab7_reservations WHERE code = %s;"
                    results = executeQuery(connector, query, (resCode))
                    print("Reservation " + resCode + " has been canceled.")
                    time.sleep(1)
                    return results
                except:
                    print("An error occurred. Invalid room code.")
                    time.sleep(1)
            else:
                print("Reservation " + resCode + " has not been canceled.")
                time.sleep(1)
                return None

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
    for row in results:
        room = row[0]
        month = row[1]
        monthlyRev = row[2]
        revByRoom[roomToTuple.get(room)][month] = monthlyRev
        revByRoom[10][month] += monthlyRev
        revByRoom[roomToTuple.get(room)][13] += monthlyRev 
        revByRoom[10][13] += monthlyRev
    table = PrettyTable()
    table.field_names = ['Room', 'Jan', 'Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Yearly']
    for room in revByRoom:
        table.add_row(room)
    print(table)
    header()




if __name__ == '__main__' :
    gatherReservationInfo()