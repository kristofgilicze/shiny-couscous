import requests

TODO_API_URL = "https://jsonplaceholder.cypress.io/todos"

def fetch_todos():
    response = requests.get(url)        
    parsed = response.json()

fetch_todos(TODO_API_URL)

if __name__ == "__main__":
    print(r.headers())