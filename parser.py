import json
import os
from typing import List, Dict

def parse_allure_results(results_dir: str = "allure-results") -> List[Dict]:
    parsed_results = []

    for file_name in os.listdir(results_dir):
        if file_name.endswith(".json"):
            file_path = os.path.join(results_dir, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    test_case = {
                        "testCaseExecutionID": data.get("uuid"),
                        "testCaseName": data.get("name"),
                        "testCaseStatus": data.get("status"),
                        "failReason": data.get("statusDetails", {}).get("message"),
                        "executionTimeStart": data.get("start"),
                        "executionTimeEnd": data.get("stop"),
                        "testCaseID": next((l['value'] for l in data.get("labels", []) if l['name'] == "tag" and l['value'].startswith("IPC_")), None),
                        "testSuiteID": data.get("suite", {}).get("uid"),
                        "testRunID": data.get("uuid"),
                        "steps": []
                    }

                    for index, step in enumerate(data.get("steps", [])):
                        test_case["steps"].append({
                            "testStepExecutionResultID": index,
                            "stepName": step.get("name"),
                            "result": step.get("status"),
                            "failReason": step.get("statusDetails", {}).get("message")
                        })

                    parsed_results.append(test_case)
            except Exception as e:
                print(f"[ERROR] JSON dosyası okunamadı: {file_name}, Hata: {e}")

    return parsed_results