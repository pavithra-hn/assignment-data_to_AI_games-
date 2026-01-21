#  Rank within department

import sqlite3
conn = sqlite3.connect("company.db")    
cursor = conn.cursor()


cursor.execute("""
SELECT name, department, salary,
RANK() OVER (PARTITION BY department ORDER BY salary DESC)
FROM employees
""")
print(cursor.fetchall())
conn.close()


# outpouts:
# [('Ravi', 'AI', 80000, 1), ('Asha', 'AI', 70000, 2), ('John', 'ML', 65000, 1), ('Meena', 'ML', 60000, 2), ('Sara', 'NLP', 75000, 1)]