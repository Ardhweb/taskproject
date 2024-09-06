from django.db import models

class Task(models.Model):
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    TODO = 'ToDo'
    INPROGRESS = 'InProgress'
    DONE = 'Done'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]
    STATUS_CHOICES = [
        (TODO, 'ToDo'),
        (INPROGRESS, 'InProgress'),
        (DONE, 'Done'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,)
    due_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
