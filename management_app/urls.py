from django.urls import path

from management_app.views import get_all_projects, get_all_tags

urlpatterns = [
    path('projects/', get_all_projects),
    path('tags/', get_all_tags),
]
