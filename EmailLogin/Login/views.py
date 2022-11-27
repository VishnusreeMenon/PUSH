from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response  import Response
from .serializer import UserSerializer,VerifySerializer
from .email import *
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
# from .forms import UserForm
# Create your views here.





class EmailRegister(APIView):
    
    
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            # print(serializer)
            if serializer.is_valid():
                serializer.save()
                opt_email(serializer.data['email'])
                return Response(
                    {
                        'status':200,
                        'message':'OTP has been sent to email',
                        'data':serializer.data
                    }
                )
                
            return Response({
                'status':400,
                'message':"There was some error",
                'data' : serializer.errors
            })
            
        except Exception as e:
            print("error-",e)
            
            
class Verify(APIView):
    
    def post(self,request):
        try:
            
            data = request.data
            # print(data)
            serializer = VerifySerializer(data = data)
            # print(serializer)
            
            if serializer.is_valid():
                # serializer.save()
                email = serializer.data['email']
                otp = serializer.data['otp']
                print(otp)
                user = User.objects.filter(email = email)
                
                if not user.exists():
                    return Response({
                    'status':400,
                    'message':"There was some error",
                    'data' : 'This user does not exist'
                })
                    
                if otp != user.first().otp:
                    return Response({
                    'status':400,
                    'message':"There was some error",
                    'data' : 'The otp is invalid'
                })
                    
                user = user.first()
                user.is_verified = True
                user.save()
                    
                return Response(
                    {
                        'status':200,
                        'message':'Account verified',
                        'data':{}
                    }
                )
                
            return Response({
                'status':400,
                'message':"There was some error",
                'data' : "serializer.errors"
            })
            
        except Exception as e:
            print("error-",e)