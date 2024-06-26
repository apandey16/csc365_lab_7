
import os
import time
import getpass
import mysql.connector
from utils import *
from reservation import gatherRoomInfo, gatherReservationInfo, cancelReservation, collectDetailedReservationInfo, collectRevenueData

# Don't change
dbhost = 'mysql.labthreesixfive.com'
db = 'akpravee'
#Set to curUser = <Username>
curUser = 'akpravee'

def mainScreen():
    print("1. Rooms and Rates")
    print("2. Make a reservation")
    print("3. Cancel a reservation")
    print("4. Lookup a reservation")
    print("5. Revenue")
    print("6. Exit")
    print("\nPlease select an option: ")
    selection = input()
    return selection

def main():
    db_password = getpass.getpass()
    conn = mysql.connector.connect(user=curUser, password=db_password,
                                   host=dbhost,
                                   database=db)
    cursor = conn.cursor()
    try:
        setUpConnection = executeQuery(cursor, "show tables")
        print("Connected to Database")
        print(setUpConnection)
    except:
        print("Connection Issue to Database")
    time.sleep(2)
    print("Welcome to Dijkstra's Inn: The Best Inn in Town\n")
    time.sleep(1)
    os.system('clear')
    header()


    # TODO:  Add verification to see if user to do more actions
    while True:
        userSelection = mainScreen()

        if userSelection == '1':
            gatherRoomInfo(cursor)
        elif userSelection == '2':
            reservationInfo, code = gatherReservationInfo(cursor, conn)
            print("Reservation ", code, " has been made. Thank you for choosing Dijkstra's Inn!")
            # add stuff to connect with DB
        # UPDATE FOR CONN
        elif userSelection == '3':
            resCode = cancelReservation(cursor, conn)
            # Connect to DB, check reservation code and  delete reservation
            if resCode is not None:
                pass
            else:
                print("Cancelled Cancelation.")
        elif userSelection == '4':
            collectDetailedReservationInfo(cursor)

        elif userSelection == '5':
            collectRevenueData(cursor)
        elif userSelection == '6':
            print("Goodbye!")
            cursor.close()
            conn.close()
            time.sleep(1)
            os.system("clear")
            break
        else:
            print("Invalid command! Please try again!")
            time.sleep(1)

if __name__ == '__main__':
    main()