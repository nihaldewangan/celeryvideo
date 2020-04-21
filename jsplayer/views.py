from django.shortcuts import render
from .models import Video
from django.http import HttpResponse
import ffmpy3
import os
from django.conf import settings
import asyncio
import sys

# Create your views here.


def upload(request):
    if request.method == 'POST':
        obj = Video()
        obj.name = request.POST['name']
        obj.videofile = request.FILES['videofile']
        # print(obj.videofile)
        print('')
        obj.save()

        
        return HttpResponse("<h1>Hello</h1>")


    else:
        return render(request,'index.html' )
            



