#!/usr/bin/python3

import sys
import requests

def get_employee_to_doprogress(employee_id):
    # API endpoints stated here

    emloyee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

  
    # Lets fetch the employee info and validate it.

    employee_response = request.get(employee_url)

    if employee_response.status_code != 200:
        print("The employer was not found")
        return
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Let's now fetch Todo info

    todo_response = request.get(todo_url)
    todo_data = todo_response.json()


    # Culculate completed tasks

    completed_tasks = [task["title"] for task in todo_data if task["completed"]]
    total_tasks = len(todo_data)

    # Displaying results

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks})")
    for task in completed_tasks:
        print(f"\t {task}")

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
            sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Employee ID must be an integer")
            sys.exit(1)
