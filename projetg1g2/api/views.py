from django.shortcuts import render



def home(request):


    context={}
    return   render(request,'Home.html',context=context)
