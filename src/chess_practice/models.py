from django.db import models

# Create your models here.


class Game(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    event = models.CharField(max_length=200)
    site = models.CharField(max_length=200)
    date = models.CharField(max_length=50)
    round = models.CharField(max_length=10)
    white = models.CharField(max_length=100)
    black = models.CharField(max_length=100)
    result = models.CharField(max_length=10)
    annotator = models.CharField(max_length=200, blank=True)
    plycount = models.CharField(max_length=200, blank=True)
    time_control = models.CharField(max_length=200, blank=True)
    time = models.CharField(max_length=200, blank=True)
    termination = models.CharField(max_length=200, blank=True)
    mode = models.CharField(max_length=200, blank=True)
    fen = models.CharField(max_length=400, blank=True)
    move_text = models.TextField()
    comments = models.TextField(max_length=500, blank=True)

