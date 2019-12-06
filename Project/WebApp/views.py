# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import University
from . serializers import UniversitySerializer

# Create your views here.
 
class UniversityList(APIView):
    
    def get(self, request):
        university=University.objects.all()
        serializer=UniversitySerializer(university, many=True)
        return Response(serializer.data)
        
        
    def post(self):
        pass