#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

from django.conf.urls import include, patterns, url

from views import *

urlpatterns = patterns('',
                       url(r'^question/add$', CreateQuestion.as_view(),
                           name='question_add'),
                       url(r'^questions$', ListQuestion.as_view(),
                           name='questions'),
                       url(r'^question/(?P<slug>[-a-zA-Z0-9_]+)/$',
                           DetailQuestion.as_view(), name='question'),
                       url(r'^question/(?P<slug>[-a-zA-Z0-9_]+)/delete$',
                           DeleteQuestion.as_view(), name='question_delete'),
                       url(r'^question/(?P<slug>[-a-zA-Z0-9_]+)/edit$',
                           UpdateQuestion.as_view(), name='question_edit'),
                       url(r'^vote/(?P<pk>\d+)/$', vote, name='vote'),
                       url(r'^~profile/(?P<pk>\d+)/edit$',
                           UpdateProfile.as_view(), name='profile_edit'),
                       url(r'^~profile/(?P<pk>\d+)/$',
                           ProfileView.as_view(), name='profile'),
                       url(r'^~profiles$', ProfileList.as_view(),
                           name='profiles'),
                       url(r'^answer/(?P<pk>\d+)/delete$',
                           DeleteAnswer.as_view(), name='answer_delete'),
                       url(r'^answer/(?P<pk>\d+)/edit$',
                           UpdateAnswer.as_view(), name='answer_edit'),
                       url(r'^answer/add$', CreateAnswer.as_view(),
                           name='answer_add'),
                       url(r'^$', MainView.as_view(), name="main"),

                       url(r'^tags$', TagListView.as_view(),
                           name='tags'),
                       url(r'^tag/(?P<slug>[-a-zA-Z0-9_]+)/$',
                           TagDetailView.as_view(), name='tag'),

                       url(r'^cats$', CatListView.as_view(),
                           name='cats'),
                       url(r'^cat/(?P<slug>[-a-zA-Z0-9_]+)/$',
                           CatDetailView.as_view(), name='cat'),
                       url(r'^vote_answer/(?P<pk>\d+)/$',
                           vote_answer, name='vote_answer'),
                       url(r'^vote/(?P<pk>\d+)/$', vote, name='vote'),
                       )
