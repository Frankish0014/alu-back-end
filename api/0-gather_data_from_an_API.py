#!/usr/bin/python3

""" Importing neccessary libraries to gather data from API """

import requests
import sys

""" start teh code with function to gather infomation """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    rest_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id) ## pasing and formating employee_id as .formate(employee_id)

## Extract and hold todos from 
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
## Formate and hold todo 
    todo = todo.format(employee_id)
    
## We now request for the info sending a GET request to from all the url links and be parsed to the JSON file
    employee_info = requests.request("GET", rest_url).json()
    employee_todo_info = requests.request("GET", todo).json()

## Get the employee name from employee_info  
    employee_name = employee_info.get("name")
    tasks = list(filter(lambda x: (x["completed"] is True), employee_todo_info))
    taskcom = len(tasks)
    task_done = len(employee_todo_info)
    
    print("Employee {} is done with task ({}/{}):".format(employee_name, taskcom, task_done))
    
    [print("\t {}".format(task.get("title"))) for task in tasks]
