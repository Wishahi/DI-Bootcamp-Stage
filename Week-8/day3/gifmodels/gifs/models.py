from turtle import mode
from django.db import models

# Create your models here.

class GifModel(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    gifs = models.ManyToManyField(GifModel, related_name='categories', blank=True)


    def __str__(self):
        return self.name