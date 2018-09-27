from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('Welcome!')
    return render(request, 'homepage.html')


def about(request):
    #return HttpResponse('Hello!')
    return render(request, 'about.html')
