import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/')
    followers = models.ManyToManyField('self')
    following = models.ManyToManyField('self')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    file = models.FileField(upload_to='fichier/')
    date = models.DateTimeField(auto_now_add=datetime.datetime.now())


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=datetime.datetime.now())


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=datetime.datetime.now())
