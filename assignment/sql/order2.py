# Salary descending

import sqlite3
conn = sqlite3.connect("company.db")        
cursor = conn.cursor()
cursor .execute("""
SELECT name, salary
FROM employees
ORDER BY salary DESC
""")
print(cursor.fetchall())
conn.close()


# output:

# [('Ravi', 80000), ('Sara', 75000), ('Asha', 70000), ('John', 65000), ('Meena', 60000)]