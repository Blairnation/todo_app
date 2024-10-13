from django.urls import path, include
from . import views

app_name = 'todo'

urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.createTodo, name='create-todo'),
    path('update/',views.updateTodo, name='update-todo'),
    path('delete/',views.deleteTodo, name='delete-todo'),

]