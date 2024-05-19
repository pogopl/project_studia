from django.db import models
from enum import Enum

class Project(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class TaskStatus(Enum):
    NOT_STARTED = 'Not Started'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'

    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace("_", " ").title()) for key in cls]

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(
            max_length=50,
            choices=TaskStatus.choices(),
            default=TaskStatus.NOT_STARTED.value)

    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name
    


class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.last_name + " " + self.name
