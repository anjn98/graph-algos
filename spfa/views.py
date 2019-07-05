from django.shortcuts import render
from django.http import HttpResponse
from heapq import *
import re

def home_view(request,*args,**kwargs):
	return render(request,"index.html")

def projects_view(request,*args,**kwargs):
	return render(request,"projects.html")

def profiles_view(request,*args,**kwargs):
	return render(request,"profiles.html")

def resume_view(request,*args,**kwargs):
	return render(request,"resume.html")

