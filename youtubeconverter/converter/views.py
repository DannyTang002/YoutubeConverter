from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,StreamingHttpResponse
from .import forms
from .import models
from .import youtubeConvert
from django.http import FileResponse
from pathlib import Path
from django.contrib import messages
import os
import requests
from django.conf import settings
from django.http import HttpResponse, Http404
from wsgiref.util import FileWrapper


# Create your views here.
def download(request,slug):
    video  = models.Video.objects.get(slug=slug)
    if request.method=='POST':
        path="converter/videos/"+video.title+".mp4"
        file = FileWrapper(open(path, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename='+video.title+'.mp4'
        return response
    else:
        return render(request, "converter/download.html" ,{'video':video})

def video_convert(request,slug):
    video  = models.Video.objects.get(slug=slug)
    if request.method=='POST':
        link = video.field_name
        if("youtube.com" in link):
            title = youtubeConvert.YoutubeConverter.convert(link)
            video.title = title
            video.save()
        return redirect('converter:download' ,slug=slug)
    else:
        return render(request,"converter/video_convert.html",{'video':video})

def listed_view(request):
    listed = models.Video.objects.all()
    return render(request, "converter/listed.html", {'listed':listed})

def register_view(request):
    if request.method == 'POST':
        form = forms.CreateVideo(request.POST)
        if form.is_valid():
            #save to db
            instance = form.save(commit=False)
            instance.save()
            return redirect('converter:listed')
    else:
        form = forms.CreateVideo()
        return render (request,"converter/register.html", {'form':form})
    
