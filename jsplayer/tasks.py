import datetime
import celery
import os
import ffmpy3
from .models import Video
from celery.schedules import crontab
from django.conf import settings
from celery.task import periodic_task

@periodic_task(run_every=crontab(minute=57, hour=17))# here we assume we want it to be run every 5 mins
def myTask():
    obj = Video()
    s = str(obj.videofile)
    print(s.split('/'))
    r = s.split('/')[1]
    print('')
    t= r[0:len(r)-4]+'_360p.mp4'

    qw = os.path.join(settings.MEDIA_ROOT,'videos')
    g = os.path.join(qw,r)

    ff = ffmpy3.FFmpeg(inputs={g: None}, outputs={t: '-c:v hevc'})
    ff.run()
    obj.save()
    print('Done')



    # Do something here
    # like accessing remote apis,
    # calculating resource intensive computational data
    # and store in cache
    # or anything you please
   
