#!/usr/bin/python3

"""Exports all users' todo list information to CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} USER_ID".format(sys.argv[0]))

    user_id = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos",
                         params={"userId": user_id}).json()

    with open(user_id + ".csv", "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, user.get("username"),
                             todo.get("completed"), todo.get("title")])
