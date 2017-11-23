from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^keyboard/', views.keyboard, name="keyboard"),
    url(r'^player/', views.player, name="player"),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
]
