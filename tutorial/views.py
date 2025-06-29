from django.shortcuts import render
from .models import Studennt,Employee
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt



from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.
def student_detail(request,pk):
    stu = Studennt.objects.get(id=pk)
    print(stu) #complex Data
    serializer = StudentSerializer(stu) #convertd python data
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type="application/json")

def allStudent(request):
    stu = Studennt.objects.all()
    print(stu) #complex Data
    serializer = StudentSerializer(stu,many=True) #convertd python data
    print(serializer)
    print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data,content_type="application/json")
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def saveStudent(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        print(serializer)
        if(serializer.is_valid()):
            # print(serializer.validated_data)
            serializer.save()
            return JsonResponse({"msg" : "Saved Succesfully"})
        else:
            print(serializer.error_messages)
            return JsonResponse(serializer.errors)

@csrf_exempt     
def StudentDetailsByFunctionView(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id",None)
        if id is not None:
            print(id)
            stu = Studennt.objects.get(id=id)
            print(stu)
            serializer = StudentSerializer(stu) 
            return JsonResponse(serializer.data,safe=False)
        else:   
            stu = Studennt.objects.all()
            serializer = StudentSerializer(stu,many=True) #convertd python data
            return JsonResponse(serializer.data,safe=False)
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse({"msg" : "Saved Succesfully"})
        else:
            print(serializer.error_messages)
            return JsonResponse(serializer.errors)
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id",None)
        stu = Studennt.objects.get(id=id)
        serializer = StudentSerializer(stu,data=python_data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse({"msg" : "Updated Succesfully"})
        else:
            print(serializer.error_messages)
            return JsonResponse(serializer.errors)
    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id",None)
        stu = Studennt.objects.get(id=id)
        stu.delete()
        return JsonResponse({"msg" : "Deleted Succesfully"})
    return JsonResponse({"msg" : "Some Error Occured"}) 
    

@method_decorator(csrf_exempt,name='dispatch')
class StudentDetailsByClassView(View):
    def get(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id",None)
        if id is not None:
            print(id)
            stu = Studennt.objects.get(id=id)
            print(stu)
            serializer = StudentSerializer(stu) 
            return JsonResponse(serializer.data,safe=False)
        else:   
            stu = Studennt.objects.all()
            serializer = StudentSerializer(stu,many=True) #convertd python data
            return JsonResponse(serializer.data,safe=False)
    def post(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse({"msg" : "Saved Succesfully"})
        else:
            print(serializer.error_messages)
            return JsonResponse(serializer.errors)
    
    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id",None)
        stu = Studennt.objects.get(id=id)
        serializer = StudentSerializer(stu,data=python_data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse({"msg" : "Updated Succesfully"})
        else:
            print(serializer.error_messages)
            return JsonResponse(serializer.errors)

    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id",None)
        stu = Studennt.objects.get(id=id)
        stu.delete()
        return JsonResponse({"msg" : "Deleted Succesfully"})




from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

@api_view(['POST','GET'])
def EmployeeDetailsByFunctionApiView(request):
    if request.method == 'GET':
        # id = request.data.get("id") # it will fetch id from body
        id = request.GET.get('id')
        print(id)
        if id is not None:
            
            emp = Employee.objects.get(id=id)
            
            serializer = EmployeeSerializer(emp) 
            return Response(serializer.data)
        else:   
            emp = Employee.objects.all()
            serializer = EmployeeSerializer(emp,many=True) #convertd python data
            return Response(serializer.data)
    if request.method == 'POST':
        serializer = EmployeeSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"msg" : "Saved Succesfully"})
        else:
            return Response(serializer.errors)
        
    #same for put and delete
    
class EmployeeDetailsByClassApiView(APIView):
    def get(self,request,format=None):
        emp_id = request.GET.get("id")
        if(emp_id is None):
                
            emp = Employee.objects.all()
            serializer = EmployeeSerializer(emp,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)  
        else:
            emp = Employee.objects.get(id=emp_id)
            serializer = EmployeeSerializer(emp)
            return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : "Saved Succesfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        emp_id = request.data.get("id",None)
        emp = Employee.objects.get(id=emp_id)
        serializer = EmployeeSerializer(emp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : "Updated Successfully"},status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, format=None):
        emp_id = request.GET.get("id")

        if not emp_id:
            return Response({"msg": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return Response({"msg": "Deleted Successfully"}, status=status.HTTP_200_OK)

        except Employee.DoesNotExist:
            return Response({"msg": "Employee ID does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin


# Pk not needed for create and fetch
class EmployeeDetailsByModelMixinGetOrCreate(GenericAPIView,ListModelMixin,CreateModelMixin,):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    

class EmployeeDetailsByModelMixinUpdateAndDestroy(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs) 
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs,partial=True)
    
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class ConcreteViewGetORCreate(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ConcreteViewGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    

