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
        
        # print(str(obj.videofile))
        # s=str(obj.videofile)


        # g = os.path.join(settings.MEDIA_ROOT,s)
        # print(g)
        # print(s[0:1])

        # ff = ffmpy3.FFmpeg(inputs={g: None}, outputs={: '-c:v hevc_nvenc'},)
        # ff.run()





        obj.save()

        

        #  ff = ffmpy3.FFmpeg( inputs={'input.mp4': None},  outputs={'output.avi': None} )
         

        # stream = ffmpeg.input(g)
        # stream = ffmpeg.scale(stream)
        # stream = ffmpeg.output(stream, 'output2.mp4')
        # ffmpeg.run(stream)

        return HttpResponse("<h1>Hello</h1>")

    else:
        return render(request,'index.html' )
            



