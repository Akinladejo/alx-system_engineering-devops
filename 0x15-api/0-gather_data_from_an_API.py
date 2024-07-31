#!/usr/bin/python3
""" Queries REST API for employee info
    argv 1 = int employee ID
"""
import requests
import sys

def get_employee_info(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)
    completed_task_count = len(completed_tasks)

    return user.get("name"), completed_task_count, total_tasks, completed_tasks

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_task_count, total_tasks, completed_tasks = get_employee_info(employee_id)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_task_count, total_tasks))
    for task in completed_tasks:
        print("\t", task)
