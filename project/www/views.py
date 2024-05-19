from django.shortcuts import render, get_object_or_404
from .models import Project, Task, User


projects = Project.objects.all()
tasks = Task.objects.all()
users = User.objects.all()


# Create your views here.
def index(request):

    return render(request, 'www/index.html', {
        'projects': projects,
        'tasks': tasks,
        'users': users,
        })

def bootstrap(request):

    return render(request, 'www/bootstrap.html', {
        'users': users
        })

def detail_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'www/detail-project.html', {
        'project': project,
        'pk':pk
        })

def detail_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'www/detail-task.html', {
        'task':task,
        'pk':pk
        })

def detail_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'www/detail-user.html', {
        'user': user,
        'pk':pk
        })