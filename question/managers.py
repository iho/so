#!/usr/bin/env python
# coding: utf-8
from __future__ import division, print_function, unicode_literals

from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)

        user.is_admin = True
        user.save(using=self._db)
        return user
