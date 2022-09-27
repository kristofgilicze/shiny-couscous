import requests

r=requests.get("https://jsonplaceholder.cypress.io/todos")
r.json()

print(r.headers)

