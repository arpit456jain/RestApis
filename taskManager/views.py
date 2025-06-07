from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.renderers  import JSONRenderer
from django.http import HttpResponse,JsonResponse

def getAllTask(request):
    queryset = Task.objects.all()
    serializer = TaskSerializer(queryset, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data,safe=False)


def getTaskById(request,task_id):
    task = Task.objects.get(task_id=task_id)
    serializer = TaskSerializer(task)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data)

