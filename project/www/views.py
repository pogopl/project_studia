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

def wydzialy_lista(request):
    return render(request, 'www/wydzialy.html', {
        'wydzialy': wydzialy
        })

def kierunki_lista(request):
    return render(request, 'www/kierunki.html', {
        'kierunki': kierunki
        })

def studenci_lista(request):
    return render(request, 'www/studenci.html', {
        'studenci': studenci
        })

def dodaj_wydzial(request):
    if request.method == 'POST':
        form = WydzialForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = WydzialForm()

    return render(request, 'www/dodaj-wydzial.html', {'form': form})


def dodaj_kierunek(request):
    if request.method == 'POST':
        form = KierunekForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = KierunekForm()

    return render(request, 'www/dodaj-kierunek.html', {'form': form})


def dodaj_studenta(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/zapisano')
    else:
        form = StudentForm()

    return render(request, 'www/dodaj-studenta.html', {'form': form})


def zapisano(request):
    return render(request, 'www/zapisano.html')