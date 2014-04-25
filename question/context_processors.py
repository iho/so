#!/usr/bin/env python
# coding: utf-8
from __future__ import division, print_function, unicode_literals

from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Avg, Count

from future_builtins import ascii, filter, hex, map, oct, zip

from .forms import SignupForm
from .models import Category


def forms_context(request):
    return {'qcats':
            Category.objects.annotate(
                num_question=Count('question')).order_by('-num_question')[:15],
            'show_forms': True,
            'form_reg': SignupForm(),
            'form_login': AuthenticationForm(),

            }
