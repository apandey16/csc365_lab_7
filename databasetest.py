import getpass
import mysql.connector


if __name__ == '__main__':
    db_password = getpass.getpass()
    conn = mysql.connector.connect(user='akpravee', password=db_password,
                                   host='mysql.labthreesixfive.com',
                                   database='akpravee')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hp_goods")
    result = cursor.fetchall()
    print(result)



