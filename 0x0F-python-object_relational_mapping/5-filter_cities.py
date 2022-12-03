#!/usr/bin/python3
"""
isplays all values in the states table of hbtn_0e_0_usa where name matches
the argument.
But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE BINARY %(state_name)s
    ORDER BY cities.id ASC""", {'state_name': argv[4]})
    states = cur.fetchall()

    print(", ".join([state[1] for state in states]))
