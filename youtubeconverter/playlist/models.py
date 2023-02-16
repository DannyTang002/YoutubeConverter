from django.db import models
from converter.models import Video
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class PlayList(models.Model):
    title =  models.CharField(max_length=100,default="playlist")
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    videos = models.ManyToManyField(Video)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    #author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    #foreign key is mapping a model another model
    def __str__(self):#så att databasen visar att varje article riktar mot sin titel
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    