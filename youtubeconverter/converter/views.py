from django.shortcuts import render,redirect
from django.http import HttpResponse
from .import forms
from .import models
from .import youtubeConvert
from django.conf import settings
from django.http import HttpResponse, Http404
from wsgiref.util import FileWrapper
from django.contrib.auth.decorators import login_required


# Create your views here.
def download(request,slug):
    video  = models.Video.objects.get(slug=slug)
    thumb = youtubeConvert.YoutubeConverter.getThumb(video.field_name)
    if request.method=='POST':
        path="converter/videos/"+str(video.id)+".mp4"
        file = FileWrapper(open(path, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename='+video.title+'.mp4'
        return response
    else:
        return render(request, "converter/download.html" ,{'video':video, 'thumb':thumb})

def video_convert(request,slug):
    video  = models.Video.objects.get(slug=slug)
    thumb=youtubeConvert.YoutubeConverter.getThumb(video.field_name)
    if request.method=='POST':
        link = video.field_name
        if("youtube.com" in link):
            if(not video.status ):
                id = str(video.id)
                title = youtubeConvert.YoutubeConverter.convert(link,id)
                video.title = title
                video.status = True
                video.save()
        return redirect('converter:download' ,slug=slug)
    else:
        return render(request,"converter/video_convert.html",{'video':video,'thumb':thumb})
        
@login_required(login_url="/accounts/login")
def listed_view(request):
    listed = models.Video.objects.filter(user=request.user)
    return render(request, "converter/listed.html", {'listed':listed})


@login_required(login_url="/accounts/login")
def register_view(request):
    if request.method == 'POST':
        form = forms.CreateVideo(request.POST)
        if form.is_valid():
            #save to db
            instance = form.save(commit=False)
            instance.user=request.user  
            instance.save()
            return redirect('converter:listed')
    else:
        form = forms.CreateVideo()
        return render (request,"converter/register.html", {'form':form})
    
