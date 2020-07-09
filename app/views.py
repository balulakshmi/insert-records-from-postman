import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from app.models import CommonModel,CourseModel
from app.forms import CourseForm

class CommonModelOperations(View):
    def post(self,request):
        data=request.body
        dict_data = json.loads(data)
        print(dict_data)
        CourseForm()
        #CourseModel(name=dict_data['name'],fee=dict_data['fee']).save()
        json_response=json.dumps({"message":"data saved sucessfully"})
        return HttpResponse(json_response, content_type="application/json")
    def get(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass