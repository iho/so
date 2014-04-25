#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import *

from .models import *


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        exclude = ('raiting',  'voted', 'owner')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('text_input', css_class='large-4 columns"'),
            Field('textarea', rows=88, css_class='input-xlarge', colls=10, ),
            Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),)
        self.helper.add_input(Submit('submit', 'Create'))
        super(QuestionForm, self).__init__(*args, **kwargs)


class AnswerForm(ModelForm):

    class Meta:
        model = Answer
        exclude = ('raiting', 'voted', 'owner')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('text_input', css_class='large-4 columns"'),
            Field('textarea', rows=88, css_class='input-xlarge', colls=10, ),
            Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),)
        self.helper.add_input(Submit('submit', 'Create'))
        super(AnswerForm, self).__init__(*args, **kwargs)


class UserForm(ModelForm):

    class Meta:
        model = User
        exclude = ['user', 'is_admin', 'is_active', 'last_login', 'password']
    #
    # def __init__(self, *args, **kwargs):
    #     self.helper = FormHelper()
    #     self.helper.layout =  Layout(
    #         Field('text_input', css_class='large-4 columns"'),
    #         Field('textarea', rows="88", css_class='input-xlarge', colls=10),
    # Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),)
    #     self.helper.add_input(Submit('submit', 'Create'))
    #     super(ProfileForm, self).__init__(*args, **kwargs)


class SignupForm(forms.Form):
    name = forms.CharField(label=_("User name"), widget=forms.TextInput(
        attrs={'placeholder':
               _('Username'),
               'autofocus': 'autofocus'}), required=True)
    email = forms.EmailField(label=_("E-mail"), required=True)

    password1 = forms.CharField(
        label=_("Password"), widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label=_("Password (again)"), widget=forms.PasswordInput, required=True)
