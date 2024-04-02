import requests

res = requests.get("http://127.0.0.1:3000/")
if res.status_code == 200:
    print("DONE")
else:
    print("Error")
