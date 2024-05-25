from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pk>/', views.detail_project, name='detail-project'),
    path('task/<int:pk>/', views.detail_task, name='detail-task'),
    path('user/<int:pk>/', views.detail_user, name='detail-user'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
]

path('Projrcts/', views.Projects_list, name='Projects-list'),
path('Tasks/', views.Tasks_list, name='Tasks-list'),
path('Users/', views.Users_list, name='Users-list'),
path('add-Project/', views.add_Project, name='add_Project'),
path('add-Task/', views.add_Task, name='add-Task'),
path('add-User/', views.add_User, name='add-User'),
path('saved/', views.saved, name='saved'),