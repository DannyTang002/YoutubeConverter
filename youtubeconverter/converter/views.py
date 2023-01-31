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


# Create your views here.

def video_convert(request,slug):
    video  = models.Video.objects.get(slug=slug)
    if request.method=='POST':
        link = video.field_name
        title = youtubeConvert.YoutubeConverter.convert(link)
        if 'convert' in request.POST:
                file_server = Path("videos/" + title +".mp4")
                if not file_server.exists():
                    messages.error(request, 'file not found.')
                    return HttpResponse(title)
                else:
                    file_to_download = open(str(file_server), 'rb')
                    response = FileResponse(file_to_download, content_type='application/force-download')
                    response['Content-Disposition'] = 'inline; filename='+title+'.mp4'
                    return response
        elif 'stream' in request.POST:
            url = 'converter/videos/'+title+".mp4"
            filename = os.path.basename(url)
            r = requests.get(url, stream=True)
            response = StreamingHttpResponse(streaming_content=r)
            response['Content-Disposition'] = f'attachement; filename="{filename}"'
            return response
        else:
            return redirect('converter:listed')
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
    
