# -*- coding: utf-8 -*-
# @Author: echo.suisui echojarn@gmail.com
# @Date:   2022-11-18 10:09:13
# @Last Modified by:   echo.suisui echojarn@gmail.com
# @Last Modified time: 2022-11-18 16:18:02
"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_asgi_application()
