from django.urls import include, path
from .views import list_todos
# from todos.views import hello_world

urlpatterns = [
    path('list/',list_todos)
]