# Left Join returns all rows from the left table and the matching rows from the right table (NULL if no match).
import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
SELECT e.name, e.department, d.manager
FROM employees e
LEFT JOIN departments d
ON e.department = d.dept_name
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

#  Explanation:
# the code above performs a left join Returns all rows from the left table (employees),Returns all rows from employees
# If no matching department  is  NULL in manager column
# NLP has no manager in departments table

# output:
# ('Asha', 'AI', 'Anita')
# ('Ravi', 'AI', 'Anita')
# ('Meena', 'ML', 'Rahul')
# ('John', 'ML', 'Rahul')
# ('Sara', 'NLP', None)