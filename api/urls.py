from django.urls import path, include
from .views import *

app_name = 'api'

urlpatterns = [
  path('todos/', TodoListView.as_view(), name='todo-list'),
  path('todos/<int:todo_id>/', TodoListView.as_view(), name='todo'),
  path('create-todo/', CreateTodoView.as_view(), name='create-todo'),
  path('edit-todo/<int:todo_id>/', EditTodoView.as_view(), name='edit-todo'),
  path('delete-todo/<int:todo_id>/', DeleteTodoView.as_view(), name='delete-todo'),

]
