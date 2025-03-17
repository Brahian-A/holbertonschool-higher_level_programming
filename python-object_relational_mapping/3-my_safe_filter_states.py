#!/usr/bin/python3
""" toma un argumento y muestra todos los valores
En la tabla de estados de HBTN_0E_0_USA
donde el nombre coincide con el argumento
y está a salvo de las inyecciones de SQL"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
