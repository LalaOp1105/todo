from django.urls import path
from .views import *

urlpatterns = [
    path('addTask/', addTask, name='addTask'),
    path('mark_as_done/<int:id>/', mark_as_done, name='mark_as_done'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
    path('mark_as_undone/<int:id>/', mark_as_undone, name='mark_as_undone' ),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
]
