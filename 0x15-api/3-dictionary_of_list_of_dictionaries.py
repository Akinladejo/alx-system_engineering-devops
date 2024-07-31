#!/usr/bin/python3
"""Exports all to-do list information for all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users").json()

    all_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]

        todos = requests.get(url + "/todos", params={"userId": user_id}).json()

        user_tasks = []
        for todo in todos:
            task = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            user_tasks.append(task)

        all_tasks[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
