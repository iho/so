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

from braces.views import (LoginRequiredMixin, PermissionRequiredMixin,
                          StaffuserRequiredMixin)
from forms import *
from taggit.models import Tag

from .models import *
from .views_mixin import (AjaxableResponseMixin, AllPagesMixin,
                          OwnerStaffRequiredMixin)


class TagListView(ListView):
    _name_page = 'List of tags'
    model = Tag
    template_name = 'cbv/list_tags.html'


class TagDetailView(ListView):
    _name_page = 'Question width tag'
    template_name = 'cbv/list_question_tags.html'
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(tags__slug__iexact=self.kwargs['slug']).select_related()


class CatListView(ListView):
    _name_page = 'List of categories'
    model = Category
    template_name = 'cbv/list_cats.html'


class CatDetailView(ListView):
    _name_page = 'Question width categories'
    model = Category
    template_name = 'cbv/list_question_cats.html'
    paginate_by = 10

    def get_queryset(self):
        return Question.objects.filter(cat__slug__iexact=self.kwargs['slug']).select_related()

    def get_context_data(self, **kwargs):
        ctx = super(CatDetailView, self).get_context_data(**kwargs)
        ctx['current_slug'] = self.kwargs['slug']
        return ctx


class MainView(ListView):
    template_name = "main.html"
    model = Question


class CreateQuestion(LoginRequiredMixin, CreateView):
    _name_page = 'Create Question '
    model = Question
    form_class = QuestionForm
    template_name = 'cbv/form.html'

    def get_initial(self):
        return {'owner': self.request.user.id}


class DetailQuestion(DetailView):
    _name_page = 'Question detail'
    model = Question
    template_name = 'question.html'


class ListQuestion(AllPagesMixin, ListView):
    _name_page = 'List Of Question`s'
    paginate_by = 10
    template_name = 'question-list.html'

    def get_queryset(self):
        return Question.objects.all().select_related('owner').prefetch_related('tags')

    def get_context_data(self, **kwargs):
        ctx = super(ListQuestion, self).get_context_data(**kwargs)
        ctx['current_page'] = 'List of question'
        return ctx


class UpdateQuestion(StaffuserRequiredMixin, UpdateView):
    _name_page = 'Update  Question '
    model = Question
    form_class = QuestionForm
    template_name = 'cbv/form.html'


class DeleteQuestion( StaffuserRequiredMixin, DeleteView):
    _name_page = 'Delete Question '
    model = Question
    template_name = 'cbv/delete.html'
    success_url = '/'


class ProfileView(AllPagesMixin ,DetailView):
    _name_page = 'Page of profile'
    model = User
    template_name = 'profile_detail.html'


class ProfileList(ListView):
    _name_page = 'Profile`s list'
    model = User
    template_name = 'cbv/list_profiles.html'


class CreateAnswer(AjaxableResponseMixin, LoginRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'cbv/form_upload.html'
    success_url = '/'

    def get_initial(self):
        return {'owner':  self.request.user.id}

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user


class UpdateAnswer(PermissionRequiredMixin, StaffuserRequiredMixin, UpdateView):
    permission_required = "auth.change_user"
    model = Answer
    form_class = AnswerForm
    template_name = 'cbv/form.html'


class DeleteAnswer(OwnerStaffRequiredMixin, DeleteView):
    model = Answer
    template_name = 'cbv/delete.html'
    success_url = '/'


class UpdateProfile(AjaxableResponseMixin, StaffuserRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'cbv/form_upload.html'

    def get_initial(self):
        return {'user': self.request.user.id}


@login_required
def vote(request, pk=0):
    user = request.user
    get_object_or_404(Question, pk=pk).add_plus(user)
    return HttpResponse('Voted')


@login_required
def vote_answer(request, pk=0):
    user = request.user
    get_object_or_404(Answer, pk=pk).add_plus(user)
    return HttpResponse('Voted')
