import requests
import json

url = requests.get("https://jsonplaceholder.typicode.com/users")
text = url.text
print(type(text))

data = json.loads(text)
print(type(data))
user = data[0]
print(user['name'])
address = user['address']
print(address)

