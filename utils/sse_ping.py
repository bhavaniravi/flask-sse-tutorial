import time
import requests

i = 0

while True:
    requests.get("http://localhost:5000/ping")
    # requests.get(f"http://localhost:5000/hello/{i}")
    i += 1
    time.sleep(1)
