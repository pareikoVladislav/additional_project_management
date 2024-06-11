from django.urls import path

from management_app.views import (
    get_all_projects,
    get_all_tags,
    get_tag_by_id,
    create_new_tag
)

urlpatterns = [
    path('projects/', get_all_projects),
    path('tags/', get_all_tags),
    path('tags/<int:pk>/', get_tag_by_id),
    path('tags/create/', create_new_tag)
]

