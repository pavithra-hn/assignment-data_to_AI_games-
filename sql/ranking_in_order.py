# Rank by salary

import sqlite3
conn = sqlite3.connect("company.db")                
cursor = conn.cursor()

cursor.execute("""
SELECT name, salary,
RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees
""")
print(cursor.fetchall())
conn.close()


# output:
# [('Ravi', 80000, 1), ('Sara', 75000, 2), ('Asha', 70000, 3), ('John', 65000, 4), ('Meena', 60000, 5)]