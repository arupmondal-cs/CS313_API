#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:09:55 2019

@author: arup
"""

from rest_framework import serializers
from . models import University

class UniversitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=University
        #fields=('University_ID', 'University_Name')
        fields='__all__'
        