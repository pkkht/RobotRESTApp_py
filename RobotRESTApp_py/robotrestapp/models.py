'''
Created on 6 Oct 2024

@author: root
'''
from django.db import models

class Robot(models.Model):
    xpos = models.IntegerField()
    ypos = models.IntegerField()
    facingdir = models.CharField(max_length=1)