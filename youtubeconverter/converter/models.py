from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    title =  models.CharField(max_length=100)
    field_name = models.URLField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg',blank=True)
    #author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    #foreign key is mapping a model another model
    def __str__(self):#så att databasen visar att varje article riktar mot sin titel
        return self.title
    
    