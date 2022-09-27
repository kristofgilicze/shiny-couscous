import requests
import pprint


TODO_API_URL = "https://jsonplaceholder.cypress.io/todos"

def fetch_todos():
    response = requests.get(TODO_API_URL)        
    parsed = response.json()
    return parsed



if __name__ == "__main__":

  todos = fetch_todos()
  #print(todos[0])

  def todoSort():
      groupTodos = {}
      for todo in todos:
          id = todo["userId"]
          if id not in groupTodos:
              groupTodos[id] = []
          groupTodos[id].append(todo)
      return groupTodos

  todos = todoSort()

  def fancy_print(id, todos):
      todo_list = todos[id]
      for todo in todo_list:
          pprint.pprint(todo)

  fancy_print(3, todos)

