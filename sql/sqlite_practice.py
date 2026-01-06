import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

# Insert employees data
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

# 🔹 ONLY DEPARTMENT TABLE ADDED BELOW

# Create departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_name TEXT,
    manager TEXT
)
""")

# Insert departments data
cursor.executemany("""
INSERT INTO departments (dept_name, manager)
VALUES (?, ?)
""", [
    ("AI", "Anita"),
    ("ML", "Rahul"),
    ("HR", "Suman")
])

conn.commit()
conn.close()
