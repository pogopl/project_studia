from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main_page', views.index, name='index'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('projects/', views.projects_list, name='projects-list'),
    path('tasks/', views.tasks_list, name='tasks'),
    path('users/', views.Users_list, name='Users-list'),
    path('projects/add/', views.add_Project, name='add-Project'),
    path('tasks/add/', views.add_Task, name='add-Task'),
    path('users/add/', views.add_User, name='add-User'),
    path('saved/', views.saved, name='saved'),
    path('projects/<int:pk>/', views.detail_project, name='detail-project'),
    path('tasks/<int:pk>/', views.detail_task, name='detail-task'),
    path('users/<int:pk>/', views.detail_user, name='detail-user'),
    path('get_projects/', views.get_projects, name='get_projects'),
    path('get_tasks/', views.get_tasks, name='get_tasks'),
    path('get_users/', views.get_users, name='get_users'),
    path('Projects/', views.projects_list, name='Projects-list'),
    path('Users/', views.Users_list, name='Users-list'),
    path('add-Project/', views.add_Project, name='add_Project'),
    path('add-Task/', views.add_Task, name='add-Task'),
    path('add-User/', views.add_User, name='add-User'),
]

