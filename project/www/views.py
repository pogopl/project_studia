from django.shortcuts import render, get_object_or_404
from .models import Project, Task, User
from .forms import ProjectForm, TaskForm, UserForm
from django.http import HttpResponseRedirect, JsonResponse


def index(request):
    return render(request, 'www/index.html')


def get_projects(request):
    projects = Project.objects.all().values('id', 'name')
    projects_list = list(projects)
    print(projects_list)
    return JsonResponse({'Projects': projects_list})


def get_tasks(request):
    tasks = Task.objects.all().values('id', 'name', 'projects__name')
    tasks_list = list()
    for task in tasks:
        task_data = {
            'id': task['id'],
            'name': task['name'],
            'projects': task['projects__name']
        }
        tasks_list.append(task_data)
    return JsonResponse({'tasks': tasks_list})


def get_users(request):
    users = User.objects.all().values('id', 'name', 'last_name', 'email')
    users_list = list(users)
    return JsonResponse({'users': users_list})


def bootstrap(request):
    users = User.objects.all()
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

def projects_list(request):
    projects = Project.objects.all().values('id', 'name')
    projects_list = list(projects)
    print(projects_list)
    return render(request, 'www/Projects.html', {
        'Projects': projects_list 
        })


def tasks_list(request):
    tasks = Task.objects.all().prefetch_related('projects')
    task_list = []
    for task in tasks:
        task_list.append({
            'id': task.id,
            'name': task.name,
            'projects': ', '.join([project.name for project in task.projects.all()])
        })
    return render(request, 'www/Tasks.html', {'tasks': task_list})


def Users_list(request):
    users = User.objects.all()
    print(users)
    return render(request, 'www/Users.html', {
        'Users': users
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


def saved(request):
    return render(request, 'www/saved.html')
