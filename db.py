import sqlite3

def init_db():
    conn = sqlite3.connect("wellness.db")
    cursor = conn.cursor()

    # Create tables for hydration, activity, and mood logs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hydration (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            intake INTEGER
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            activity_type TEXT,
            duration INTEGER,
            calories INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mood (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            mood INTEGER,
            stress INTEGER,
            energy INTEGER
        )
    """)

    conn.commit()
    conn.close()

# Initialize the database
init_db()
