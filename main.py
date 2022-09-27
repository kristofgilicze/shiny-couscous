import requests



def parser(url):
    response = requests.get(url)        
    parsed = response.json()
    print(parsed[0])

parser("https://jsonplaceholder.cypress.io/todos")