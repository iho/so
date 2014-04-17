#!/usr/bin/env python
# coding: utf-8
from __future__ import division, print_function, unicode_literals

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Avg, Count
from django.http import Http404
from django.shortcuts import redirect

from future_builtins import ascii, filter, hex, map, oct, zip

from .forms import SignupForm
from .models import Category


class AjaxableResponseMixin(object):

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        print("response")
        if self.request.is_ajax():
            print(form.errors)
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        print("response1")
        if self.request.is_ajax():
            data = {
                'Result': True,
            }
            print(data)
            return self.render_to_json_response(data)
        else:
            return response


class AllPagesMixin(object):

    def get_context_data(self, **kwargs):
        ctx = super(AllPagesMixin, self).get_context_data(**kwargs)
        ctx['qcats'] = Category.objects.annotate(
            num_question=Count('question')).order_by('-num_question')[:15]
        ctx['show_forms'] = True
        ctx['form_reg'] = SignupForm()
        ctx['form_login'] = AuthenticationForm()

        ctx['current_page'] = getattr(self, '_name_page', '')

        ctx['is_main'] = self.__class__.__name__ == "MainView" or False
        return ctx


class OwnerStaffRequiredMixin(object):

    def get_object(self, queryset=None):
        obj = super(OwnerStaffRequiredMixin, self).get_object()
        if (obj.owner_id == self.request.user.pk) or (self.request.user.is_staff):
            messages.success(self.request, 'Done!')
            return obj
        messages.warning(self.request,
                         'You have not permission to this object.')
        raise Http404
