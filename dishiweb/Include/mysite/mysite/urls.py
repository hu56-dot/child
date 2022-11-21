# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-18 10:09:13
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-20 15:33:05
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from polls import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("echorec/",include('polls.urls')),
    path("",include('polls.urls')),
    # path("daily/",include('polls.urls'))
    # path('dishirec/',views.DailyRecipe.as_view(),name="polls")
   
]






'''

[
	{
		"description": "",
		"field_type": "String",
		"is_checked": 1,
		"key": "name",
		"value": "石亚军",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "用户的账号",
		"field_type": "Integer",
		"is_checked": 1,
		"key": "id",
		"value": "220056",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "",
		"field_type": "Float",
		"is_checked": 1,
		"key": "height",
		"value": "170.0",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "",
		"field_type": "Float",
		"is_checked": 1,
		"key": "weight",
		"value": "60.0",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "",
		"field_type": "Float",
		"is_checked": 1,
		"key": "age",
		"value": "23.5",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "",
		"field_type": "String",
		"is_checked": 1,
		"key": "gender",
		"value": "男",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "",
		"field_type": "Float",
		"is_checked": 1,
		"key": "consumption",
		"value": "699.0",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "",
		"field_type": "Integer",
		"is_checked": 1,
		"key": "puberty",
		"value": "0",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "",
		"field_type": "Array",
		"is_checked": 1,
		"key": "prefer",
		"value": "['原味','酸甜']",
		"not_null": 1,
		"type": "Text"
	},
	{
		"description": "",
		"field_type": "String",
		"is_checked": 1,
		"key": "asser",
		"value": "{'谷薯类':'木薯'}",
		"not_null": 1,
		"type": "Text"
	}
]


'''