import requests, time

api_url = "http://127.0.0.1:8000"

# Create process

resp = requests.get(api_url + "/spawn")
print(resp)
print(resp.status_code)
time.sleep(10)

resp = requests.get(api_url + "/kill")
print(resp)
print(resp.status_code)

