from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.renderers  import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def createTask(request):
    if request.method == 'POST':
        try:
            stream = io.BytesIO(request.body)
            python_data = JSONParser().parse(stream)
            serializer = TaskSerializer(data=python_data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'Task Added'}, status=201)

            return JsonResponse(serializer.errors, status=400)

        except Exception as e:
            print("Error:", e)  # shows up in terminal
            return JsonResponse({'error': str(e)}, status=500)