from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from management_app.models import Project, Tag, Task
from management_app.serializers.projects import AllProjectsSerializer
from management_app.serializers.tags import AllTagsSerializer
from management_app.serializers.tasks import AllTasksSerializer

@api_view(["GET"])
def get_all_projects(request: Request) -> Response:
    projects = Project.objects.all()
    if not projects.exists():
        return Response(data=[], status=status.HTTP_204_NO_CONTENT)
    serialize = AllProjectsSerializer(projects, many=True)

    return Response(data=serialize.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_tags(request: Request) -> Response:
    tags = Tag.objects.all()
    if not tags.exists():
        return Response(data=[], status=status.HTTP_204_NO_CONTENT)
    serialize = AllTagsSerializer(tags, many=True)

    return Response(data=serialize.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_all_tasks(request: Request) -> Response:
    tasks = Task.objects.all()
    if not tasks.exists():
        return Response(data=[], status=status.HTTP_204_NO_CONTENT)
    serialize = AllTasksSerializer(tasks, many=True)

    return Response(data=serialize.data, status=status.HTTP_200_OK)

@api_view(["Get"])
def get_tag_by_id(request: Request, pk: int) -> Response:
    try:
        tag_by_id = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)

    serialize = AllTagsSerializer(tag_by_id)
    
    return Response(data=serialize.data, status=status.HTTP_200_OK)

