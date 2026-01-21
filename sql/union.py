# Union combines the results of two queries into one result set by removing duplicate rows.

import sqlite3
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
SELECT department FROM employees
UNION
SELECT dept_name FROM departments
""")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

# Explanation :
# this above code performs a union operation here Combines results from both tables
# Removes duplicates
# Shows all unique departments

# output:
# ('AI',)
# ('HR',)
# ('ML',)
# ('NLP',)