from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import login, authenticate,logout
# Create your views here.


class LoginViw(View):
    def get(self,request,*args,**kwargs):
        context={}     
        return  render(request,'login.html',context)
    
    def post(self,request,*args,**kwargs):
        nombre=request.POST['username']
        cont=request.POST['password']
        
        
        user=authenticate(request,username=nombre,password=cont)

        if user is not None:
            login(request,user)
            return redirect ('info')
        

        else:
            print("hola")
            context= {"error" : "Usuario o contraseña incorrecta"}
            return render(request,'login.html',context)


class Logout(View):    
    def get(self,request,*args,**kwargs):
        logout(request)
        return  redirect("login")
    
class InfoView(View):
    def get(self,request,*args,**kwargs):     
        return  render(request,'info.html' )


class FormView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'formulario.html')