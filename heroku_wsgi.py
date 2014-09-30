#!/usr/bin/env python
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "so.settings")

from dj_static import Cling

application = Cling(get_wsgi_application())
