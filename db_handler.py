import sqlite3
from typing import Dict

DB_FILE = "test_bdd.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS TestRun (
            testRunID TEXT PRIMARY KEY,
            testRunName TEXT,
            runTimeStart TEXT,
            runTimeEnd TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS TestSuites (
            testRunID TEXT,
            testSuiteID TEXT,
            PRIMARY KEY (testRunID, testSuiteID)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS TestCaseExecution (
            testCaseExecutionID TEXT PRIMARY KEY,
            testCaseID TEXT,
            testSuiteID TEXT,
            executionTimeStart TEXT,
            executionTimeEnd TEXT,
            environment TEXT,
            result TEXT,
            failReason TEXT,
            testCaseName TEXT,
            testCaseStatus TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS TestStepExecutionResult (
            testCaseExecutionID TEXT,
            testStepExecutionResultID INTEGER,
            stepName TEXT,
            result TEXT,
            failReason TEXT,
            PRIMARY KEY (testCaseExecutionID, testStepExecutionResultID)
        );
        """)

        conn.commit()

def insert_test_case(case: Dict, environment: str = "default"):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT OR IGNORE INTO TestRun (
            testRunID, testRunName, runTimeStart, runTimeEnd
        ) VALUES (?, ?, ?, ?)
        """, (
            case["testRunID"],
            case.get("testCaseName"),
            case.get("executionTimeStart"),
            case.get("executionTimeEnd")
        ))

        cursor.execute("""
        INSERT OR IGNORE INTO TestSuites (
            testRunID, testSuiteID
        ) VALUES (?, ?)
        """, (
            case["testRunID"],
            case["testSuiteID"]
        ))

        cursor.execute("""
        INSERT OR REPLACE INTO TestCaseExecution (
            testCaseExecutionID, testCaseID, testSuiteID,
            executionTimeStart, executionTimeEnd, environment,
            result, failReason, testCaseName, testCaseStatus
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            case["testCaseExecutionID"],
            case["testCaseID"],
            case["testSuiteID"],
            case["executionTimeStart"],
            case["executionTimeEnd"],
            environment,
            case["testCaseStatus"],
            case["failReason"],
            case["testCaseName"],
            case["testCaseStatus"]
        ))

        for step in case["steps"]:
            cursor.execute("""
            INSERT OR REPLACE INTO TestStepExecutionResult (
                testCaseExecutionID, testStepExecutionResultID, stepName,
                result, failReason
            ) VALUES (?, ?, ?, ?, ?)
            """, (
                case["testCaseExecutionID"],
                step["testStepExecutionResultID"],
                step["stepName"],
                step["result"],
                step["failReason"]
            ))

        conn.commit()