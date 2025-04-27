import json
import os

def parse_allure_results(results_dir="allure-results"):
    """Allure sonuçlarını işle ve liste olarak döndür."""
    test_cases = []

    for file_name in os.listdir(results_dir):
        if file_name.endswith(".json"):
            file_path = os.path.join(results_dir, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    test_cases.append(data)
            except Exception as e:
                print(f"[ERROR] JSON dosyası okunamadı: {file_name}, Hata: {e}")

    return test_cases
