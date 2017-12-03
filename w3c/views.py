# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import CityGallery

# Create your views here.
class IndexView(generic.ListView):

    #设置使用的模板
    template_name = 'w3c/index.html'

    # 自定义上下文变量
    context_object_name = 'latest_cities_list'

    def get_queryset(self):
        """
            重写 get_queryset 方法，取出发表的内容
        """
        return CityGallery.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = CityGallery
    template_name = 'w3c/detail.html'
    context_object_name = "city"
    pk_url_kwargs = "pk"


    def get_object(self,queryset=None):
        index=int(self.kwargs.get(self.pk_url_kwargs, None)) - 1
        return CityGallery.objects.filter(pub_date__lte=timezone.now())[index]



