from django.shortcuts import render 
from rest_framework.views import APIView 
# from . models import *
from rest_framework.response import Response 
from DBCalls import DBCalls
# from . serializer import *
# Create your views here. 
  
class loginView(APIView): 
    

    # Maybe serializer stuff???

    def post(self,request, info): 
        return DBCalls.login(info.email,info.password)#If this is true, login sucessfully and move to the next page, if not display an error
    


class signupView(APIView):

    def post(self, request, info):
        return DBCalls.add_student(info.email, info.password)#This will be true or false. Do stuff differently depending on this
    # Like if false, it didn't add a student, so have an error message pop up

        

        
