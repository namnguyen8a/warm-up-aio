import requests


user_data = requests.get(f"http://127.0.0.1:8000/patients/name/tran").json()
print(user_data)