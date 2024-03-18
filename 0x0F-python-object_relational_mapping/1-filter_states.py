#!/usr/bin/python3

"""
Module that connects python script to a database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    # Database connection using command-line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    # Creating query and executing query
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetches data from the query
    my_data = my_cursor.fetchall()

    # Iterating
    for row in my_data:
        print(row)

    # Closing cursors and databases
    my_cursor.close()
    my_db.close()
