from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

def getAllTask(request):
    try:
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        print("Error:", e)
        return JsonResponse({'error': str(e)}, status=500)


def getTaskById(request, task_id):
    try:
        task = Task.objects.get(task_id=task_id)
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)
    except Exception as e:
        print("Error:", e)
        return JsonResponse({'error': str(e)}, status=500)


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
            print("Error:", e)
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def updateTask(request):
    if request.method == 'PUT':
        try:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get("task_id")
            obj = Task.objects.get(task_id=id)
            serializer = TaskSerializer(obj, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'Data Updated'}, status=200)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            print("Error:", e)
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def deleteTask(request,task_id):
    if request.method == 'DELETE':
        try:
            task = Task.objects.get(task_id=task_id)
            task.delete()
            return JsonResponse({'msg': 'Task deleted'}, status=200)
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)