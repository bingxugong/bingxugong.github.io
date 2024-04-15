import requests

url = 'https://api.tttt.one/rest-v1/http/echo'

method = 'GET'
headers = {
    "name" : "gbx"
}
body = {
    "username": "bing",
    "password": "123456",
}
response = requests.request(method=method, url=url, headers=headers, json=body)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)

