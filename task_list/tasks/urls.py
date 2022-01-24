from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path("tasks/", views.TaskTableViewSet.as_view({'get': 'list'})),
    path("tasks/<int:pk>/",
         views.TaskTableViewSet.as_view({'get': 'retrieve'})),
])
