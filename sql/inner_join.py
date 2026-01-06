#Inner Join returns only the rows that have matching values in both tables.

import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
SELECT e.name, e.department, d.manager
FROM employees e
INNER JOIN departments d
ON e.department = d.dept_name
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

# Explanation :
# the code above performs an inner join  Returns only matching rows from both tables
# Departments common in both tables: AI, ML
# NLP (employees) and HR (departments) are excluded

# output:
# ('Asha', 'AI', 'Anita')
# ('Ravi', 'AI', 'Anita')
# ('Meena', 'ML', 'Rahul')
# ('John', 'ML', 'Rahul')
