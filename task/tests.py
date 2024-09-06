from django.test import TestCase
from .models import Task
from .filters import filter_list
from datetime import date
class TaskFilterTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create various tasks for testing
        Task.objects.create(title="Task 1", status=Task.TODO, priority=Task.HIGH, due_date="2024-09-01")
        Task.objects.create(title="Task 2", status=Task.INPROGRESS, priority=Task.MEDIUM, due_date="2024-09-02")
        Task.objects.create(title="Task 3", status=Task.DONE, priority=Task.LOW, due_date="2024-09-03")
        Task.objects.create(title="Task 4", status=Task.TODO, priority=Task.LOW, due_date="2024-09-04")
        Task.objects.create(title="Task 5", status=Task.INPROGRESS, priority=Task.HIGH, due_date="2024-09-05")

    def test_filter_by_status_todo(self):
        """Test filtering tasks by 'ToDo' status"""
        tasks = filter_list(status=Task.TODO)
        self.assertEqual(tasks.count(), 2)
        self.assertEqual(tasks.first().title, "Task 1")

    def test_filter_by_status_done(self):
        """Test filtering tasks by 'Done' status"""
        tasks = filter_list(status=Task.DONE)
        self.assertEqual(tasks.count(), 1)
        self.assertEqual(tasks.first().title, "Task 3")

    def test_sort_by_priority(self):
        """Test sorting tasks by priority in descending order"""
      
        tasks = filter_list(sort_by="priority")
        
        self.assertEqual(tasks.first().priority, Task.HIGH)
        self.assertEqual(tasks.last().priority, Task.LOW)

    def test_empty_database(self):
        """Test filtering and sorting when no tasks exist in the database"""
        Task.objects.all().delete()  # Clear all tasks
        tasks = filter_list(status=Task.TODO)
        self.assertEqual(tasks.count(), 0)


    def test_no_filter_no_sort(self):
        """Test when no filter or sort_by is provided"""
        tasks = filter_list()
        self.assertEqual(tasks.count(), 5)
