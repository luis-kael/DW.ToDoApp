from django import path
from . import views
urlpatterns = {
  path('list/',views.ToDoList , name="ToDoList") 
}