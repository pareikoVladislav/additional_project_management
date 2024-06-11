from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from management_app.models import Project
from management_app.serializers.projects import AllProjectsSerializer


@api_view(["GET"])
def get_all_projects(request: Request) -> Response:
    projects = Project.objects.all()
    if not projects.exists():
        return Response(data=[], status=status.HTTP_204_NO_CONTENT)
    serialize = AllProjectsSerializer(projects, many=True)

    return Response(data=serialize.data, status=status.HTTP_200_OK)
