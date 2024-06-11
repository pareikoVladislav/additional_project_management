from django.urls import path

from management_app.views import get_all_projects

urlpatterns = [
    path('projects/', get_all_projects)
]