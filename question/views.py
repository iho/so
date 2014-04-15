#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

import json

from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, TemplateView, UpdateView)

from braces.views import LoginRequiredMixin
from forms import *
from taggit.models import Tag

from .models import *
from .views_mixin import AjaxableResponseMixin, FormMixin


class TagListView(ListView):
    model = Tag


class MainView(ListView):
    template_name = "main.html"
    model = Question


class CreateQuestion(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'cbv/form.html'

    def get_initial(self):
        return {'owner': self.request.user.id}


class DetailQuestion(DetailView):
    model = Question
    template_name = 'cbv/detail.html'


class ListQuestion(ListView):
    model = Question
    paginate_by = 10
    template_name = 'cbv/list.html'


class UpdateQuestion(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'cbv/form.html'


class DeleteQuestion(DeleteView):
    model = Question
    template_name = 'cbv/delete.html'
    success_url = '/'


class ProfileView(DetailView):
    model = User
    template_name = 'cbv/detail.html'


class ProfileList(ListView):
    model = User
    template_name = 'cbv/list.html'


class CreateAnswer(AjaxableResponseMixin, LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'cbv/form_upload.html'
    success_url = '/'

    def get_initial(self):
        return {'owner':  self.request.user.id}

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user


class UpdateAnswer(UpdateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'cbv/form.html'


class DeleteAnswer(DeleteView):
    model = Answer
    template_name = 'cbv/delete.html'
    success_url = '/'


class UpdateProfile(AjaxableResponseMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'cbv/form_upload.html'

    def get_initial(self):
        return {'user': self.request.user.id}


@login_required
def vote(request, pk=0):
    user = request.user
    if request.GET.get('answer', 0) == 'minus':
        get_object_or_404(Answer, pk=pk).add_minus(user)
    elif request.GET.get('answer', 0) == 'plus':
        get_object_or_404(Answer, pk=pk).add_plus(user)
    elif request.GET.get('question', 0) == 'minus':
        get_object_or_404(Question, pk=pk).add_minus(user)
    elif request.GET.get('question', 0) == 'plus':
        get_object_or_404(Question, pk=pk).add_plus(user)
    return HttpResponse('Voted!')
