import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

# Insert data
cursor.executemany("""
INSERT INTO employees (name, department, salary)
VALUES (?, ?, ?)
""", [
    ("Asha", "AI", 70000),
    ("Ravi", "AI", 80000),
    ("Meena", "ML", 60000),
    ("John", "ML", 65000),
    ("Sara", "NLP", 75000)
])

conn.commit()
conn.close()
