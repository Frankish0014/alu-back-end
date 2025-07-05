#!/usr/bin/python3
"""
    This python file exports data in the csv formate
"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        Request info of the user bt ID by formating the entered ID to the url
    """
    request_emplo = requests.get('https://jsonplaceholder.typicode.come/users/{}/'.format(argv[1]))
    """
        convert json to dictionary.
    """
    
    user = json.loads(request_emplo.text)
    
    """
        extracting the username
    """
    
    user_name = user.get("user_name")
    
    
    """
        Requesting user todo
    """
    
    user_todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    
    """
        Creating a dictinary to hold the tasks
    """
    
    all_tasks = {}
    
    """
        converting the todos into a dictionary 
    """
    
    todo_list = json.loads(user_todo.text)
    
    """
        get completed tasks by looping through the dictionary
    """
    
    for dictionary in todo_list:
        all_tasks.update({dictionary.get("title"): dictionary.get("completed")})
    
    """
        export to csv
    """
    
    with open('{}.csv'.format(argv[1]),mode='w') as file:
        file_editor = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k,v in all_tasks.items():
            file_editor.writerow([argv[1], user_name, v, k])
