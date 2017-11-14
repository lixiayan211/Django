# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import BlogPost
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/templates/blog/'

# Create your views here.


def archive(request):
    posts = BlogPost.objects.all()[:10]
    return render(request, BASE_DIR+'archive.html', {'posts': posts})

def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(title=request.POST.get('title'),
                 body=request.POST.get('body'),
                 timestamp=datetime.now(),).save()
        return HttpResponseRedirect('/blog/')