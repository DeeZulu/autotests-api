import httpx

login_payload = {
    "email": "booryat@list.ru",
    "password": "123456"
}

url = "http://localhost:8000/api/v1"

login_response = httpx.post(f"{url}/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

access_token = login_response_data["token"]["accessToken"]

me_headers = {"Authorization": f"Bearer {access_token}"}
me_response = httpx.get(f"{url}/users/me", headers=me_headers)
me_response_data = me_response.json()
print("Me response:", me_response_data)
print("Status code:", me_response.status_code)