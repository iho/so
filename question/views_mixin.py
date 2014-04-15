#!/usr/bin/env python
# coding: utf-8
from __future__ import division, print_function, unicode_literals

from future_builtins import ascii, filter, hex, map, oct, zip


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


class FormMixin(object):

    def get_context_data(self, **kwargs):
        ctx = super(FormMixin, self).get_context_data(**kwargs)
        ctx['house'] = self.get_house()
        return ctx


class C(object):
    _exm = []

    def __init__(self):
        C._exm.append(self)
a = C()
