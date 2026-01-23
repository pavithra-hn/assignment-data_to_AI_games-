# Highest salary per department

import sqlite3
conn = sqlite3.connect("company.db")            
cursor = conn.cursor()

cursor.execute("""
SELECT name, department, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees e2
    WHERE e2.department = employees.department
)
""")
print(cursor.fetchall())
conn.close()


# output:
# [('Ravi', 'AI', 80000), ('John', 'ML', 65000), ('Sara', 'NLP', 75000)]

