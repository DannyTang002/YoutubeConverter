from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .import forms
from .import models
from .import youtubeConvert


# Create your views here.

def video_convert(request,slug):
    video  = models.Video.objects.get(slug=slug)
    if request.method=='POST':
        link = video.field_name
        youtubeConvert.YoutubeConverter.convert(link)
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
    
