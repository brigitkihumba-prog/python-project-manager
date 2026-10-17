import unittest
import json
import tempfile
import os

from models.person import Person
from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data

class TestProjectManagerModels(unittest.TestCase):

    def test_person_creation(self):
        person = Person("Jane Doe", "jane@example.com")
        self.assertEqual(person.name, "Jane Doe")
        self.assertEqual(person.email, "jane@example.com")

    def test_person_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            Person("", "jane@example.com")

    def test_person_rejects_invalid_email(self):
        with self.assertRaises(ValueError):
            Person("Jane Doe", "invalid-email")

    def test_user_inherits_from_person(self):
        user = User("Jane Doe", "jane@example.com")
        self.assertIsInstance(user, Person)

    def test_user_can_add_project(self):
        user = User("Jane Doe", "jane@example.com")
        project = Project(
            "Website Project",
            "Create a website",
            "2026-12-31"
        )
        user.add_project(project)
        self.assertIn(project, user.projects)

    def test_project_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            Project("", "Create a website", "2026-12-31")

    def test_project_can_add_task(self):
        project = Project(
            "Website Project",
            "Create a website",
            "2026-12-31"
        )
        task = Task("Create homepage")
        project.add_task(task)
        self.assertIn(task, project.tasks)

    def test_task_starts_pending(self):
        task = Task("Create homepage")
        self.assertEqual(task.status, "Pending")

    def test_task_can_be_completed(self):
        task = Task("Create homepage")
        task.complete()
        self.assertEqual(task.status, "Complete")

    def test_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            Task("")


def test_save_and_load_data(self):
        original_data_file = __import__(
            "utils.storage", fromlist=["DATA_FILE"]
        ).DATA_FILE

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                import utils.storage as storage

                storage.DATA_FILE = os.path.join(
                    temp_dir, "projects.json"
                )

                test_data = {
                    "users": [{"name": "Jane", "email": "jane@example.com"}],
                    "projects": [],
                    "tasks": []
                }

                save_data(test_data)
                loaded_data = load_data()

                self.assertEqual(loaded_data, test_data)
        finally:
            import utils.storage as storage
            storage.DATA_FILE = original_data_file
            
if __name__ == "__main__":
    unittest.main()