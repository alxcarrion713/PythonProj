from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime


# Create your views here.
def index (request):
    now=datetime.now()
    print (now)
    context= {
        'currenttime':now
    }
    return render(request, 'index.html',context)

def new (request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def show (request,my_val):
    
    return HttpResponse(f'placeholder to display a blog number: {my_val}')

def edit (request,my_val):
    return HttpResponse (f'placeholder to edit blog {my_val}')

def destroy(request):
    return redirect("/")

