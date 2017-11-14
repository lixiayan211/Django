# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def keyboard(request):
    return render(request, 'keyboard.html')

def player(request):
    return render(request, 'player.html')
