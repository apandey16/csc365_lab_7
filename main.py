
import os
import time
from utils import header
from reservation import gatherReservationInfo, cancelReservation, collectDetailedReservationInfo

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
    print("Welcome to Dijkstra's Inn: The Best Inn in Town\n")
    time.sleep(1)
    os.system('clear')
    header()


    # TODO:  Add verification to see if user to do more actions
    while True:
        userSelection = mainScreen()

        if userSelection == '1':
            pass
        elif userSelection == '2':
            reservationInfo = gatherReservationInfo()
            break
            # add stuff to connect with DB
        elif userSelection == '3':
            resCode = cancelReservation()
            # Connect to DB, check reservation code and  delete reservation
            print("Reservation " + resCode + " has been canceled")
            break
        elif userSelection == '4':
            searchCritea = collectDetailedReservationInfo()

        elif userSelection == '5':
            pass
        elif userSelection == '6':
            print("Goodbye!")
            time.sleep(1)
            os.clear()
            break
        else:
            print("Invalid command! Please try again!")
            time.sleep(1)

if __name__ == '__main__':
    main()