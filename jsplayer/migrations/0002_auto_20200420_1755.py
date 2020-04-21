# Generated by Django 3.0.5 on 2020-04-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsplayer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='v360p',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='video',
            name='v4800p',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='video',
            name='v540p',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]