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
    url(r'^questions/(?P<abc>[0-9]+)/favourite/$', views.favourite, name='favourite'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^answers/(?P<pk>[0-9]+)/add_comment/$', views.add_comment, name='add_comment'),
    url(r'^questions/add/$', views.add_question, name='add_question'),
    url(r'^questions/(?P<pk>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^thesaurus/$', views.thesaurus, name='thesaurus'),
    url(r'^wordoftheday/$', views.word_of_the_day, name='word_of_the_day'),
    url(r'^dict/apicall/$', views.Weather.as_view(), name='weats'),
]
