from django.urls import path
from . import views

urlpatterns = [
    path("tasks", views.TaskView.as_view()),
    path("tasks/<int:task_id>", views.TaskDetailView.as_view()),
]
