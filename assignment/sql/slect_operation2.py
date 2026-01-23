# SELECT * FROM TABLE

import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute("SELECT name, salary FROM employees")
print(cursor.fetchall())
conn .close()


# output:
# [('Asha', 70000), ('Ravi', 80000), ('Meena', 60000), ('John', 65000), ('Sara', 75000)]