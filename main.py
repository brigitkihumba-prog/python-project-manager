import argparse
from datetime import date

from rich.console import Console
from rich.table import Table

from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data

console = Console()


def add_user(name, email):
    data = load_data()

    try:
        user = User(name, email)
    except ValueError as error:
        console.print(f"[red]Error: {error}[/red]")
        return

    if any(item["name"].lower() == user.name.lower()
           for item in data["users"]):
        console.print("[red]Error: This user already exists.[/red]")
        return

    data["users"].append({
        "name": user.name,
        "email": user.email
    })
    save_data(data)
    console.print(f"[green]User added:[/green] {user}")


def list_users():
    data = load_data()
    table = Table(title="Users")
    table.add_column("Name")
    table.add_column("Email")

    for user in data["users"]:
        table.add_row(user["name"], user["email"])

    console.print(table)


def add_project(user_name, title, description, due_date):
    data = load_data()

    try:
        project_date = date.fromisoformat(due_date)
        project = Project(title, description, project_date.isoformat())
    except (ValueError, TypeError) as error:
        console.print(f"[red]Error: Invalid project details: {error}[/red]")
        return

    user = next(
        (item for item in data["users"]
         if item["name"].lower() == user_name.lower()),
        None
    )

    if user is None:
        console.print("[red]Error: User not found. Add the user first.[/red]")
        return

    if any(item["title"].lower() == project.title.lower()
           and item["user"].lower() == user_name.lower()
           for item in data["projects"]):
        console.print("[red]Error: This user already has a project with that title.[/red]")
        return

    data["projects"].append({
        "user": user["name"],
        "title": project.title,
        "description": project.description,
        "due_date": project.due_date
    })

    save_data(data)
    console.print(f"[green]Project added:[/green] {project.title}")


def list_projects(user_name=None):
    data = load_data()
    table = Table(title="Projects")
    table.add_column("User")
    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Due date")
    table.add_column("Tasks")

    for project in data["projects"]:
        if user_name and project["user"].lower() != user_name.lower():
            continue

        task_count = sum(
            1 for task in data["tasks"]
            if task["project"].lower() == project["title"].lower()
        )

        table.add_row(
            project["user"],
            project["title"],
            project["description"],
            project["due_date"],
            str(task_count)
        )

    console.print(table)


def add_task(project_title, title, assigned_to):
    data = load_data()

    project_record = next(
        (item for item in data["projects"]
         if item["title"].lower() == project_title.lower()),
        None
    )

    if project_record is None:
        console.print("[red]Error: Project not found.[/red]")
        return

    try:
        task = Task(title, assigned_to or "Unassigned")
    except ValueError as error:
        console.print(f"[red]Error: {error}[/red]")
        return

    if assigned_to and not any(
        user["name"].lower() == assigned_to.lower()
        for user in data["users"]
    ):
        console.print("[red]Error: Assigned user not found.[/red]")
        return

    if any(
        item["project"].lower() == project_title.lower()
        and item["title"].lower() == task.title.lower()
        for item in data["tasks"]
    ):
        console.print("[red]Error: This task already exists in the project.[/red]")
        return

    data["tasks"].append({
        "project": project_record["title"],
        "title": task.title,
        "assigned_to": task.assigned_to,
        "status": task.status
    })

    save_data(data)
    console.print(f"[green]Task added:[/green] {task.title}")


def list_tasks(project_title=None):
    data = load_data()
    table = Table(title="Tasks")
    table.add_column("Project")
    table.add_column("Task")
    table.add_column("Assigned to")
    table.add_column("Status")

    for task in data["tasks"]:
        if project_title and task["project"].lower() != project_title.lower():
            continue

        table.add_row(
            task["project"],
            task["title"],
            task["assigned_to"],
            task["status"]
        )

    console.print(table)


def complete_task(project_title, title):
    data = load_data()

    task_record = next(
        (item for item in data["tasks"]
         if item["project"].lower() == project_title.lower()
         and item["title"].lower() == title.lower()),
        None
    )

    if task_record is None:
        console.print("[red]Error: Task not found in that project.[/red]")
        return

    task = Task(task_record["title"], task_record["assigned_to"])
    task.status = task_record["status"]
    task.complete()

    task_record["status"] = task.status
    save_data(data)
    console.print(f"[green]Task completed:[/green] {task.title}")


def main():
    parser = argparse.ArgumentParser(
        description="Manage users, projects, and tasks."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    user_add = commands.add_parser("add-user", help="Add a user")
    user_add.add_argument("--name", required=True)
    user_add.add_argument("--email", required=True)

    commands.add_parser("list-users", help="List users")

    project_add = commands.add_parser("add-project", help="Add a project")
    project_add.add_argument("--user", required=True)
    project_add.add_argument("--title", required=True)
    project_add.add_argument("--description", required=True)
    project_add.add_argument("--due-date", required=True)

    project_list = commands.add_parser("list-projects", help="List projects")
    project_list.add_argument("--user")

    task_add = commands.add_parser("add-task", help="Add a task")
    task_add.add_argument("--project", required=True)
    task_add.add_argument("--title", required=True)
    task_add.add_argument("--assigned-to", default=None)

    task_list = commands.add_parser("list-tasks", help="List tasks")
    task_list.add_argument("--project")

    task_complete = commands.add_parser(
        "complete-task", help="Mark a task as complete"
    )
    task_complete.add_argument("--project", required=True)
    task_complete.add_argument("--title", required=True)

    args = parser.parse_args()

    if args.command == "add-user":
        add_user(args.name, args.email)
    elif args.command == "list-users":
        list_users()
    elif args.command == "add-project":
        add_project(args.user, args.title, args.description, args.due_date)
    elif args.command == "list-projects":
        list_projects(args.user)
    elif args.command == "add-task":
        add_task(args.project, args.title, args.assigned_to)
    elif args.command == "list-tasks":
        list_tasks(args.project)
    elif args.command == "complete-task":
        complete_task(args.project, args.title)


if __name__ == "__main__":
    main()