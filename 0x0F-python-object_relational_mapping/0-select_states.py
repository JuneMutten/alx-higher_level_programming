#!/usr/bin/python3

"""
Module that connects a python script to a database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    # Database connection using command-line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    # Cursor to interact with database
    my_cursor = my_db.cursor()

    # Executes a SELECT query to fetch data
    my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # Fetches data returned by query
    my_data = my_cursor.fetchall()

    # Prints each row after iteration
    for row in my_data:
        print(row)

    # Cursor and database closing
    my_cursor.close()
    my_db.close()
