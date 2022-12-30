from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.TodoListCreateView.as_view(), name='todo-list-create'),
    path('<int:pk>/', views.TodoView.as_view(), name='todo'),
    path('mine/', views.TodoUserListView.as_view(), name='todo-mine'),
    path('random/', views.RandomTodoView.as_view(), name='todo-random'),
]