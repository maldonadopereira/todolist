from django.urls import path, include

from tarefas import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home')
]