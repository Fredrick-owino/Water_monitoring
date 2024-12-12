# test_api.py
import requests

BASE_URL = "http://127.0.0.1:5000"  # Replace with your running API URL

def test_index():
    response = requests.get(f"{BASE_URL}/")
    print("Index Route:", response.status_code, response.text)

def test_get_parameters():
    response = requests.get(f"{BASE_URL}/api/parameters")
    print("GET Parameters:", response.status_code, response.json())

def test_post_parameter():
    payload = {
        "type": "water",
        "parameter": "pH",
        "value": 7.5
    }
    response = requests.post(f"{BASE_URL}/api/parameters", json=payload)
    print("POST Parameter:", response.status_code, response.json())

def test_get_thresholds():
    response = requests.get(f"{BASE_URL}/api/thresholds")
    print("GET Thresholds:", response.status_code, response.json())

def test_get_alerts():
    response = requests.get(f"{BASE_URL}/api/alerts")
    print("GET Alerts:", response.status_code, response.json())

def test_get_history():
    params = {"start_date": "2024-12-01", "end_date": "2024-12-10"}
    response = requests.get(f"{BASE_URL}/api/history", params=params)
    print("GET History:", response.status_code, response.json())

def test_inject_data():
    payload = {
        "parameter": "Temperature",
        "value": 25.5,
        "timestamp": "2024-12-10T12:00:00"
    }
    response = requests.post(f"{BASE_URL}/api/inject-data", json=payload)
    print("Inject Data:", response.status_code, response.json())

if __name__ == "__main__":
    test_index()
    test_get_parameters()
    test_post_parameter()
    test_get_thresholds()
    test_get_alerts()
    test_get_history()
    test_inject_data()
