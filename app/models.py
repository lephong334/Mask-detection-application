from django.db import models

# Create your models here.

class Camera(models.Model):
  name = models.CharField(max_length=250)

  def __str__(self):
    return self.name

class Entry(models.Model):
  camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
  name = models.CharField(max_length=250)
