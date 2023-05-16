from os import sys
from typing import Any, Dict, List
from sys import exit
import database_class as task_db


def first_display() -> None:
    print("TASK MANAGER MENU")
    print("1. Create new task")
    print("2. Get all tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")


def update_display() -> None:
    print("TASK UPDATE MENU")
    print("1. Update task title")
    print("2. Update the description of the task")
    print("3. Update the end time of the task (YYYY-MM-DD HH:MM)")
    print("4. Update task status (waiting, running, paused, completed)")
    print("5. Back")
    print("6. Exit")


def first_display_choise_cli() -> int:
    choice = input("Enter your choice (1-5): ")
    return choice


def update_display_choice() -> int:
    choice = input("Enter your choice (1-6): ")
    return choice


def add_task_cli() -> None:
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    end_time = input("Enter the end time of the task (YYYY-MM-DD HH:MM): ")
    status = input(
        "Enter the status of the task (waiting, running, paused, completed): "
    )
    new_task = {
        "task title": title,
        "task description": description,
        "task end time": end_time,
        "task status": status,
    }
    task_id = task_db.create_task(new_task)
    print(f"Task added with ID: {task_id}")


def display_tasks(tasks: List[Dict[str, Any]]) -> None:
    print("TASKS:")
    for task in tasks:
        print(f"ID: {task['_id']}")
        print(f"Title: {task['task title']}")
        print(f"Description: {task['task description']}")
        print(f"Task end time: {task['task end time']}")
        print(f"Status: {task('task status')}")
        print("------------------------")


def view_all_tasks_cli() -> None:
    tasks = task_db.get_all_tasks()
    display_tasks(tasks)


def update_task_title_cli() -> None:
    title = input("Enter title of the task, you want to update: ")
    new_title = input("Enter new title: ")
    count = task_db.update_task(task_name=title, task_updates={"task title": new_title})
    print(f"{count} task(s) updated")


def update_task_description_cli() -> None:
    title = input("Enter title of the task, you want to update: ")
    new_description = input("Enter new description: ")
    count = task_db.update_task(
        task_name=title, task_updates={"task description": new_description}
    )
    print(f"{count} task(s) updated")


def update_task_end_time() -> None:
    title = input("Enter title of the task, you want to update: ")
    new_time = input("Enter new end time (YYYY-MM-DD HH:MM): ")
    count = task_db.update_task(
        task_name=title, task_updates={"task end time": new_time}
    )
    print(f"{count} task(s) updated")


def update_task_status_cli() -> None:
    title = input("Enter title of the task, you want to update: ")
    new_status = input("Enter new status (waiting, running, paused, completed): ")
    count = task_db.update_task(
        task_name=title, task_updates={"task status": new_status}
    )
    print(f"{count} task(s) updated")


def delete_task_cli() -> None:
    title = input("Enter title of the task, you want to delete: ")
    count = task_db.delete_task(title)
    print(f"{count} task(s) deleted")


def main() -> None:
    while True:
        first_display()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task_cli()

        if choice == "2":
            display_tasks()

        if choice == "3":
            display_tasks()
            update_display()
            update_choice = input("Enter your choice (1-6): ")
            if update_choice == "1":
                update_task_title_cli()
            if update_choice == "2":
                update_task_description_cli()
            if update_choice == "3":
                update_task_end_time()
            if update_choice == "4":
                update_task_status_cli()
            if update_choice == "5":
                break
            if update_choice == "6":
                exit("Task manager closed")

        if choice == "4":
            delete_task_cli()
        if choice == "5":
            exit("Task manager closed")


main()
