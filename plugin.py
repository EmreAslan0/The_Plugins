import os
import sqlite3
import pytest
import allure
from pytest_bdd import scenarios, given, when, then
from pytest_allure_db.db_handler import save_test_result, init_db, get_db_connection

test_results = []  # 🔴 Test sonuçlarını kaydetmek için global liste

@pytest.hookimpl
def pytest_sessionstart(session):
    """Testler başlamadan önce veritabanını başlat."""
    print("[INFO] Pytest oturumu başladı, veritabanı başlatılıyor...")
    init_db()

@pytest.hookimpl
def pytest_bdd_apply_tag(tag, function):
    """BDD testlerindeki özel etiketleri işle."""
    if tag == "db":
        function.db_required = True
        return True
    return None

@pytest.fixture
def db():
    """Veritabanı bağlantısını sağlayan fixture."""
    conn = get_db_connection()
    yield conn
    conn.close()

@pytest.hookimpl
def pytest_runtest_logreport(report):
    """Test sonuçlarını global değişkende tutar."""
    if report.when == "call":  # Sadece çalıştırma aşamasındaki sonuçları kaydet
        test_results.append((report.nodeid, report.outcome, report.duration))
        print(f"[LOG] Test Sonucu Kaydediliyor: {report.nodeid}, {report.outcome}, {report.duration}")

def pytest_sessionfinish(session, exitstatus):
    """Pytest tamamlandığında test sonuçlarını veritabanına ekler."""
    conn = get_db_connection()
    cursor = conn.cursor()

    for test_name, status, duration in test_results:
        cursor.execute("INSERT INTO test_results (test_name, status, duration) VALUES (?, ?, ?)", (test_name, status, duration))

    conn.commit()
    conn.close()
