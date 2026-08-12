import random
import time
import requests
from datetime import datetime

URL = "http://127.0.0.1:5000/sensor-data"

def read_sensor():
    return {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 80.0), 2),
        "timestamp": datetime.now().isoformat()
    }

if __name__ == "__main__":
    while True:
        reading = read_sensor()
        response = requests.post(URL, json=reading)
        print("Sent:", reading, "| Server said:", response.json())
        time.sleep(3)