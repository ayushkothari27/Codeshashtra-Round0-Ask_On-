from django.conf.urls import url
from . import views

app_name = 'forum'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^profile/(?P<idx>[0-9]+)/', views.profile, name='profile'),
    url(r'^question/add/', views.add_question, name='add_question'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^questions/(?P<pk>[0-9]+)/', views.view_question, name='view_question'),
]