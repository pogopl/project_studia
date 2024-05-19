from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pk>/', views.detail_project, name='detail-project'),
    path('task/<int:pk>/', views.detail_task, name='detail-task'),
    path('user/<int:pk>/', views.detail_user, name='detail-user'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
]