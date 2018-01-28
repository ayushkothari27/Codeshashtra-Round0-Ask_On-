from django.conf.urls import url
from . import views

app_name = 'forum'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^profile/(?P<idx>[0-9]+)/$', views.profile, name='profile'),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.view_question, name='view_question'),
    url(r'^questions/(?P<abc>[0-9]+)/add_answer/$', views.add_answer, name='add_answer'),
<<<<<<< HEAD
    url(r'^questions/(?P<abc>[0-9]+)/favourite/$', views.favourite, name='favourite'),
=======
>>>>>>> 2fc40769ced0ed8e7d959d5ad318b826b000710e
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^answers/(?P<pk>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
]
