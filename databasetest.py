import getpass
import mysql.connector


if __name__ == '__main__':
    dbhost = 'mysql.labthreesixfive.com'
    db = 'akpravee'


    #CHANGE THIS LINE DEPENDING ON WHO YOU ARE
    #USE UR CALPOLY USERNAME
    curUser = 'akpravee'
    db_password = getpass.getpass()
    conn = mysql.connector.connect(user=curUser, password=db_password,
                                   host=dbhost,
                                   database=db)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hp_goods")
    result = cursor.fetchall()
    print(result)

    cursor.close()
    conn.close()



