# made from https://www.youtube.com/watch?v=byHcYRpMgI4

import sqlite3



"""
below can be used to connect to a database somewhere in memory. it wil create a temporary
database that will be deleted when the script ends and will not change the database
that was accessed from memory
"""
# conn = sqlite3.connect(':memory:')



#connect to a database. if the database does not exist, it will create a .db file
conn = sqlite3.connect('customer.db')
c = conn.cursor()

try:
    #recommended you use docstrings like ("""   """)
    c.execute("""CREATE TABLE customers(
            first_name text,
            last_name text,
            email text
        )""")
except:
    pass

    """
    Datatypes for columns are:
    -NULL
    -INTEGER
    -REAL
    -TEXT
    -BLOB
    """

#saves anything that's been inserted into the database  to the database
c.execute("INSERT INTO customers VALUES ('Luz', 'Kilian', 'heremail@yahoo.com')")
print("executed")

#Below is a way to insert many rows all at once:
many_customers = [
                    ('Wes','Brown', 'wesbrown@yes.com'),
                    ('andy','cirkus', 'andyy@yes.com'),
                    ('Wai','Knott', 'WAII@yes.com'),
                ]
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
print("Many Customers Executed")
print()
conn.commit()


#Below is a way to query the database
c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)
print(c.fetchall())
print()


#Updating Records:
c.execute("""UPDATE customers SET first_name = 'Luzmaria'
            WHERE last_name = 'Kilian'
""")
c.execute("SELECT * FROM customers")
print(c.fetchall())
print()

#Delete everything from the TABLE
c.execute("DELETE FROM customers")
conn.commit()
c.execute("SELECT * FROM customers")
print(c.fetchall())


conn.close()
