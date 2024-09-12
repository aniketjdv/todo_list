from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.todo,name="todolist"),
    path('delete/<int:item_task_id>/', views.delete_item, name='delete_item'),

]
