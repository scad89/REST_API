from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskTableView.as_view(), name='tasks'),
    path("tasks/<int:pk>/", views.TaskTableDetailView.as_view())
]
