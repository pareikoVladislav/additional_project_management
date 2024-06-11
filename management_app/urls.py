from django.urls import path

from management_app.views import get_all_projects, create_new_tag

urlpatterns = [
    path('projects/', get_all_projects),
    path('tags/create/', create_new_tag)
]