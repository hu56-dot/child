# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-18 10:15:35
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-20 14:52:00
from django.urls import path
from django.views.generic import TemplateView

from . import views



urlpatterns = [

    path('index', TemplateView.as_view(template_name="index.html"), name='index'),
    path('dish', views.get_dish, name='dishrec'),
    path('daily', views.tess.as_view(), name='dailyrec'),
    path('userInfor', views.userInform, name='userInform'),
    path('dailyrec', TemplateView.as_view(template_name="daily.html"), name='index'),
    path('dishrec', TemplateView.as_view(template_name="dish.html"), name='index'),
    path('inforec', TemplateView.as_view(template_name="inform.html"), name='index'),
    
    # path('dishirec/',views.DailyRecipe.as_view(),name="polls")
]
