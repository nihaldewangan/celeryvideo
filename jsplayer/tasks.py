import datetime
import celery
import os
import ffmpy3
from .models import Video
from celery.schedules import crontab
from django.conf import settings
from celery.task import periodic_task

@periodic_task(run_every=crontab(minute=15, hour=15))# here we assume we want it to be run every 5 mins
def myTask():
    obj = Video.objects.all()
    print(str(obj.videofile))
    s = str(obj.videofile)
    t= s[0:len(s)-4]+'_360p.mp4'

    g = os.path.join(settings.MEDIA_ROOT,s)

    ff = ffmpy3.FFmpeg(inputs={g: None}, outputs={t: '-c:v hevc_nvenc'})
    ff.run()
    obj.save()
    print('Done')



    # Do something here
    # like accessing remote apis,
    # calculating resource intensive computational data
    # and store in cache
    # or anything you please
   