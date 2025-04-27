import pytest
import os
from pytest_allure_db.parser import parse_allure_results
from pytest_allure_db.db_handler import init_db, insert_test_case

RESULTS_DIR = "allure-results"

def pytest_addoption(parser):
    parser.addini("bdd_env", help="BDD ortam bilgisi", default="default")
    parser.addoption("--bdd-env", action="store", help="BDD environment")

def pytest_configure(config):
    init_db()
    config._bdd_environment = config.getoption("bdd_env") or config.getini("bdd_env")
    config._bdd_results = []

def pytest_sessionfinish(session, exitstatus):
    config = getattr(session, "config", None)
    if not config:
        return

    if not os.path.exists(RESULTS_DIR):
        print(f"[PLUGIN WARNING] '{RESULTS_DIR}' klasörü bulunamadı, Allure çıktısı üretilmemiş.")
        return

    results = parse_allure_results(RESULTS_DIR)
    for result in results:
        insert_test_case(result, environment=config._bdd_environment)
