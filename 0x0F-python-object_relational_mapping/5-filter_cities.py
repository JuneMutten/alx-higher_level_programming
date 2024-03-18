#!/usr/bin/python3

"""
Module that connects a python script to a database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    # Database connection with command-line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    # Creating cursor and query execution
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM cities INNER JOIN states \
            ON cities.state_id = states.id ORDER BY cities.id")

    # Fetching data from query
    print(", ".join([city[2] for city in my_cursor.fetchall()
                    if city[4] == argv[4]]))
