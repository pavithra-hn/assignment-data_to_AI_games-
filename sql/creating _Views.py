# Create a View

import sqlite3
conn = sqlite3.connect("company.db")    
cursor = conn.cursor()

cursor.execute("""
CREATE VIEW IF NOT EXISTS high_salary AS
SELECT name, salary
FROM employees
WHERE salary > 70000
""")
conn.commit()
conn.close()

