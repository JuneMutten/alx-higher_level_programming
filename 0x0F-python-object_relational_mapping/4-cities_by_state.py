#!/usr/bin/python3

"""
Module that connects a python script to a databse
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":

    # Database connection using command-line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)

    # Creating cursor and executing queries
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON \
            states.id = cities.state_id \
            ORDER BY cities.id")

    # Fetching data from the queries
    [print(city) for city in my_cursor.fetchall()]
