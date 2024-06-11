from django.urls import path
from management_app.views import get_all_projects, get_all_tags, get_all_tasks

urlpatterns = [
    path('projects/', get_all_projects),
    path('tags/', get_all_tags),
    path('tasks/', get_all_tasks),
    path('tags/<int:pk>/', get_tag_by_id)
]
