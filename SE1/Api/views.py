from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

def student_detail(request,id):
    #This will get Student object instance with id
    stu=Student.objects.get(id=1) 
    # This wil convert stu into python native
    serializer=StudentSerializer(stu)
    # This will render python native into JSON
    # json_data=JSONRenderer().render(serializer.data)
    # #this will return json response
    # return HttpResponse(json_data,content_type='application/json')
    # By using JsonResponse we do not need to use JSONRenderer and HttpResponse
    return JsonResponse(serializer.data)


def student_list(request):
    #This will get Student object instance with id
    stu=Student.objects.all() 
    # This wil convert stu into python native
    serializer=StudentSerializer(stu,many=True)
    # This will render python native into JSON
    json_data=JSONRenderer().render(serializer.data)
    #this will return json response
    return HttpResponse(json_data,content_type='application/json')