# Query the View

import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM high_salary")
print(cursor.fetchall())
conn.close()



# output:
# [('Ravi', 80000), ('Sara', 75000)]
