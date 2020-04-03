from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"hello i am the from views"}
    return render(request,'the_app/index.html',context=my_dict)
