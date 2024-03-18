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

    # Creating cursor and executing a query
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM states")

    # Fetching data from query
    [print(state) for state in my_cursor.fetchall() if state[1] == argv[4]]
