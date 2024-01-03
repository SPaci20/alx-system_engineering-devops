#!/usr/bin/python3
"""
A script that, using the given REST API, returns information about an
           employee's TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches information about the employee's TODO list progress and prints
                        the required output.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
    """
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch user details
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch user's TODO list
    todo_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)

    # Print the output
    print(f"Employee {employee_name} is done with tasks(
            {completed_tasks}/{total_tasks}):
            ")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
