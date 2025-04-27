from setuptools import setup, find_packages

setup(
    name="pytest-history-bdd",
    version="0.1.0",
    description="Pytest plugin to parse Allure BDD results into a structured SQLite DB",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pytest>=7.0.0",
        "pytest-bdd",
        "allure-pytest"
    ],
    entry_points={
        "pytest11": [
            "history_bdd = pytest_allure_db.plugin",
        ]
    },
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
