import os
import sqlite3

DB_FILE = "database.db"

def init_db():
    """Veritabanını başlatır ve tabloyu oluşturur."""
    if os.path.exists(DB_FILE):
        try:
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute("PRAGMA integrity_check;")
                result = cursor.fetchone()
                if result[0] != "ok":
                    print("[WARNING] Database corrupted. Recreating...")
                    os.remove(DB_FILE)
        except sqlite3.DatabaseError:
            print("[ERROR] Database error. Recreating...")
            os.remove(DB_FILE)

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                test_name TEXT,
                status TEXT,
                duration FLOAT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def get_db_connection():
    """Yeni bir veritabanı bağlantısı döndürür."""
    return sqlite3.connect(DB_FILE)

def save_test_result(test_name, status, duration):
    """Test sonucunu veritabanına kaydeder."""
    print(f"[INFO] Saving test result: {test_name}, Status: {status}, Duration: {duration}")  # Debugging için eklendi
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO test_results (test_name, status, duration) VALUES (?, ?, ?)",
            (test_name, status, duration)
        )
        conn.commit()

def fetch_all_results():
    """Veritabanındaki tüm test sonuçlarını getirir ve ekrana basar."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test_results")
        results = cursor.fetchall()
        print("[INFO] Database Records:")
        for row in results:
            print(row)
