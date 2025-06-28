#!/usr/bin/python3
""" Library to gather data from an API """

import requests
import sys

""" Function to gather data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_information = requests.request("GET", url).json()
    todo_information = requests.request("GET", todo_data).json()

    employee_name = user_information.get("name")
    total_tasks = list(filter(lambda x: (x["completed"] is True), todo_information))
    task_com = len(total_tasks)
    total_task_done = len(todo_information)

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          task_com, total_task_done))

    [print("\t {}".format(task.get("title"))) for task in total_tasks]
