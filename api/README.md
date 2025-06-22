# Web Infrastructure


### Background Context

Old-school system administrators typically rely on Bash for scripting, which can become messy and inefficient compared to other programming languages. The new generation of system administrators, known as Site Reliability Engineers (SREs), possess a broader skill set beyond Bash scripting. One effective way to expose applications and datasets is through APIs, which serve as the public-facing components of websites and microservices, allowing external interactions with data.

In this project, you will access employee data via an API to organize and export it into different data structures, demonstrating the need for Python scripts over Bash.

## Resources

### Read or Watch

- Friends don’t let friends program in shell script
- What is an API
- What is an API? In English, please
- What is a REST API
- What are microservices
- PEP8 Python style - maintaining clean code is crucial in the industry

## Learning Objectives

At the end of this project, you should be able to explain the following concepts:

- Limitations of Bash scripting
- What an API is
- What a REST API is
- The concept of microservices
- CSV format
- JSON format
- Pythonic naming conventions for packages, modules, classes, variables, functions, and constants
- Significance of CapWords or CamelCase in Python

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files must be interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Libraries imported in Python files must be organized in alphabetical order
- A `README.md` file at the root of the project folder is mandatory
- Code must adhere to PEP 8 style guidelines
- All files must be executable
- The length of files will be tested using `wc`
- All modules must include documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`)
- Use `get` to access dictionary values by key (this prevents exceptions if the key doesn’t exist)
- Code should not be executed when imported (use `if __name__ == "__main__":`)

## Tasks

### 0. Gather Data from an API (Mandatory)

Write a Python script that retrieves information about an employee's TODO list progress using a REST API.

**Requirements:**
- Use `urllib` or `requests` module
- Accept an integer as a parameter (the employee ID)
- Display the employee's TODO list progress in the specified format.

**Example:**
```bash
$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     ...
```
**Repo:**
- GitHub repository: `alu-back-end`
- Directory: `api`
- File: `0-gather_data_from_an_API.py`

### 1. Export to CSV (Mandatory)

Extend the previous script to export data in CSV format.

**Requirements:**
- Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- File name: `USER_ID.csv`

**Example:**
```bash
$ python3 1-export_to_CSV.py 2
$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
...
```
**Repo:**
- GitHub repository: `alu-back-end`
- Directory: `api`
- File: `1-export_to_CSV.py`

### 2. Export to JSON (Mandatory)

Extend the previous script to export data in JSON format.

**Requirements:**
- Format: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ...] }`
- File name: `USER_ID.json`

**Example:**
```bash
$ python3 2-export_to_JSON.py 2
$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, ...]}
```
**Repo:**
- GitHub repository: `alu-back-end`
- Directory: `api`
- File: `2-export_to_JSON.py`

### 3. Dictionary of List of Dictionaries (Mandatory)

Extend the previous script to export data from all employees in JSON format.

**Requirements:**
- Format: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ] }`
- File name: `todo_all_employees.json`

**Example:**
```bash
$ python3 3-dictionary_of_list_of_dictionaries.py
$ cat todo_all_employees.json
{"1": [{"username": "Bret", "task": "delectus aut autem", "completed": false}, ...]}
```
**Repo:**
- GitHub repository: `alu-back-end`
- Directory: `api`
- File: `3-dictionary_of_list_of_dictionaries.py`

## Score

Your score will be updated as you progress. Please review all tasks before starting the peer review.

---

**Copyright © 2025 ALU, All rights reserved.**

