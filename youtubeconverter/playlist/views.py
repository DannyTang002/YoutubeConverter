from django.shortcuts import render,redirect
from .forms import CreatePlayList
from .models import PlayList
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

def add_song(request): 
    data = json.b

def show_info(request,slug):
    playlist = PlayList.objects.get(slug=slug)
    return render(request, "playlist/playListInfo", {"item":playlist})
    

@login_required(login_url="/accounts/login")    
def register_playlist(request):
    if request.method == 'POST':
        form = CreatePlayList(request.POST)
        if form.is_valid():
            #save to db
            instance = form.save(commit=False)
            instance.user=request.user  
            instance.save()
            return redirect('playlist:listed')
    else:
        form = CreatePlayList()
        return render (request,"playlist/registerPlaylist.html", {'form':form})

@login_required(login_url="/accounts/login")    
def listed_playlist(request):
    listed = PlayList.objects.all()
    return render(request,"playlist/lists.html",{"listed":listed})