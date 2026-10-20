import tempfile
import unittest
from pathlib import Path
from task_manager import TaskManager

class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.storage_path = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(self.storage_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task_persists_task(self):
        task = self.manager.add_task("Finish assignment")
        self.assertEqual(task["id"], 1)
        self.assertEqual(self.manager.list_tasks()[0]["title"], "Finish assignment")

    def test_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        task = self.manager.add_task("Run tests")
        completed = self.manager.complete_task(task["id"])
        self.assertTrue(completed["completed"])

    def test_unknown_task_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.manager.complete_task(99)

if __name__ == "__main__":
    unittest.main()
