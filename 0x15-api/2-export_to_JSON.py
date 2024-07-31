#!/usr/bin/python3
""" Queries REST API for employee info, exports to JSON
    argv 1 = int employee ID
"""
import json
import requests as r
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    # Finds employee username by "id" param in /users/
    name_response = r.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    user_data = name_response.json()
    username = user_data.get("username")

    # Finds employee tasks by "userID" param; /users/ & /todo/ are linked
    task_response = r.get("https://jsonplaceholder.typicode.com/todos", params={'userId': user_id})
    tasks_data = task_response.json()

    # Creates JSON object with request data, writes to .json file
    json_data = {user_id: [{"task": task.get("title"), "completed": task.get("completed"), "username": username} for task in tasks_data]}

    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(json_data, jsonfile)
