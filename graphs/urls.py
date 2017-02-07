# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^introduction/(?P<variable_id>\d+)$',
        view=views.introduction,
        name='introduction'
    ),
    url(
        regex=r'^introduction/$',
        view=views.introduction,
        name='introduction'
    ),
    url(
        regex=r'^graphing/$',
        view=views.graphing,
        name='graphing'
    ),
     url(
        regex=r'^ajaxfire/(?P<variable_id>\d+)/(?P<order>\d+)/(?P<number>\d+)$',
        view=views.ajaxfire,
        name='ajaxfire'
    ),
]