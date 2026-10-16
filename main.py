# Import the tools needed by our CLI
import argparse
from rich.console import Console
from rich.table import Table
from utils.storage import load_data, save_data

console = Console()


# Displays users in a table
def list_users(data):
    table = Table(title="Project Users")
    table.add_column("Name")
    table.add_column("Email")

    for user in data["users"]:
        table.add_row(user["name"], user["email"])

    console.print(table)


# Displays projects and their tasks
def list_projects(data, username=None):
    table = Table(title="Projects")
    table.add_column("Title")
    table.add_column("Owner")
    table.add_column("Due Date")
    table.add_column("Tasks")

    for project in data["projects"]:
        if username and project["owner"] != username:
            continue

        table.add_row(
            project["title"],
            project["owner"],
            project["due_date"],
            str(len(project["tasks"]))
        )

    console.print(table)


# Handles all CLI commands
def main():
    parser = argparse.ArgumentParser(
        description="Simple Project Management CLI"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    user_cmd = commands.add_parser("add-user")
    user_cmd.add_argument("--name", required=True)
    user_cmd.add_argument("--email", required=True)

    commands.add_parser("list-users")

    project_cmd = commands.add_parser("add-project")
    project_cmd.add_argument("--user", required=True)
    project_cmd.add_argument("--title", required=True)
    project_cmd.add_argument("--description", default="")
    project_cmd.add_argument("--due-date", default="Not set")

    list_cmd = commands.add_parser("list-projects")
    list_cmd.add_argument("--user")

    task_cmd = commands.add_parser("add-task")
    task_cmd.add_argument("--project", required=True)
    task_cmd.add_argument("--title", required=True)
    task_cmd.add_argument("--assigned-to", default="Unassigned")

    complete_cmd = commands.add_parser("complete-task")
    complete_cmd.add_argument("--project", required=True)
    complete_cmd.add_argument("--title", required=True)

    args = parser.parse_args()
    data = load_data()

    if args.command == "add-user":
        if any(u["name"] == args.name for u in data["users"]):
            console.print("[red]User already exists.[/red]")
            return

        data["users"].append({
            "name": args.name,
            "email": args.email
        })
        save_data(data)
        console.print("[green]User added successfully![/green]")

    elif args.command == "list-users":
        list_users(data)

    elif args.command == "add-project":
        if not any(u["name"] == args.user for u in data["users"]):
            console.print("[red]User not found. Add the user first.[/red]")
            return

        data["projects"].append({
            "title": args.title,
            "description": args.description,
            "due_date": args.due_date,
            "owner": args.user,
            "tasks": []
        })
        save_data(data)
        console.print("[green]Project added successfully![/green]")

    elif args.command == "list-projects":
        list_projects(data, args.user)

    elif args.command == "add-task":
        project = next(
            (p for p in data["projects"] if p["title"] == args.project),
            None
        )

        if project is None:
            console.print("[red]Project not found.[/red]")
            return

        project["tasks"].append({
            "title": args.title,
            "status": "Pending",
            "assigned_to": args.assigned_to
        })
        save_data(data)
        console.print("[green]Task added successfully![/green]")

    elif args.command == "complete-task":
        project = next(
            (p for p in data["projects"] if p["title"] == args.project),
            None
        )

        if project is None:
            console.print("[red]Project not found.[/red]")
            return

        task = next(
            (t for t in project["tasks"] if t["title"] == args.title),
            None
        )

        if task is None:
            console.print("[red]Task not found.[/red]")
            return

        task["status"] = "Complete"
        save_data(data)
        console.print("[green]Task completed![/green]")


# Starts the application
if __name__ == "__main__":
    main()