# Right Join returns all rows from the right table and the matching rows from the left table (NULL if no match).
import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
SELECT e.name, d.dept_name, d.manager
FROM departments d
LEFT JOIN employees e
ON e.department = d.dept_name
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

# Explanation:
# the code above performs a right join Returns all rows from the right table (employees),
# If no employee exists  as  NULL
# HR has no employees


# output:
# ('Asha', 'AI', 'Anita')
# ('Ravi', 'AI', 'Anita')
# ('John', 'ML', 'Rahul')
# ('Meena', 'ML', 'Rahul')
# (None, 'HR', 'Suman')
