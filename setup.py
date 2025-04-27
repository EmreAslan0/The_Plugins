from setuptools import setup

setup(
    name="pytest-allure-db",
    version="1.0",
    packages=["pytest_allure_db"],
    entry_points={"pytest11": ["pytest_allure_db = pytest_allure_db.plugin"]},
    install_requires=["pytest", "pytest-bdd", "allure-pytest"],
)
