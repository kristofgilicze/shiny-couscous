import requests

TODO_API_URL = "https://jsonplaceholder.cypress.io/todos"

def fetch_todos():
    response = requests.get(TODO_API_URL)        
    parsed = response.json()
    return parsed



if __name__ == "__main__":
    r = fetch_todos()
    print(r[0])
    