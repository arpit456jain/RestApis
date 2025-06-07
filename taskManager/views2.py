
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
@api_view(['GET'])
def getAllTask(request):
    try:
        # task_id = request.data.get("task_id") # to get from body
        task_id = request.query_params.get("task_id") # to get from request param
        print(task_id)
        if task_id is not None:
            obj = Task.objects.get(task_id=task_id)
            serializer = TaskSerializer(obj)
            return Response(serializer.data)
        else:
            obj_list = Task.objects.all()
            serializer = TaskSerializer(obj_list,many=True)
            return Response(serializer.data)
    except Exception as e:
        return Response({'Error Occured' : str(e)})
    
@api_view(['POST','PUT'])
def saveOrUpdate(request):
    try:
        if request.method == "POST":
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg' : "Data Created"},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            task_id = request.data.get("task_id") # to get from body
            obj = Task.objects.get(task_id=task_id)
            serializer = TaskSerializer(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg' : "Data Updated"},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'Error Occured' : str(e)},status=status.HTTP_400_BAD_REQUEST)