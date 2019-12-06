# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class University(models.Model):
    University_ID=models.IntegerField()
    University_Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Email=models.CharField(max_length=50)
    Phone_Number=models.IntegerField()
    
    def __str__(self):
        return self.University_Name
    
