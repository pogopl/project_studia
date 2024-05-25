from django.shortcuts import render, get_object_or_404
from .models import Project, Task, User
from .forms import ProjectForm, TaskForm, UserForm
from django.http import HttpResponseRedirect


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


################################################################################################

def Projects_list(request):
    return render(request, 'www/Projects.html', {
        'Projects': Project
        })

def Tasks_list(request):
    return render(request, 'www/Tasks.html', {
        'Tasks': Task
        })

def Users_list(request):
    return render(request, 'www/Users.html', {
        'Users': User
        })

def add_Project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/saved')
    else:
        form = ProjectForm()

    return render(request, 'www/add-Project.html', {'form': form})


def add_Task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/saved')
    else:
        form = TaskForm()

    return render(request, 'www/add-Task.html', {'form': form})


def add_User(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/saved')
    else:
        form = UserForm()

    return render(request, 'www/add-User.html', {'form': form})


def zapisano(request):
    return render(request, 'www/zapisano.html')