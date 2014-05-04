#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

import hashlib

from django.contrib.auth.models import AbstractBaseUser
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from future_builtins import ascii, filter, hex, map, oct, zip
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from managers import MyUserManager
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(_('Slug'), max_length=60, unique=True)

    def get_absolute_url(self):
        return reverse('cat', args=[str(self.slug)])

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categorys')

    def __unicode__(self):
        return self.name


class User(AbstractBaseUser):
    avatar = models.ImageField(upload_to='avatars')
   # avatar_thumbnail = ImageSpecField(source='avatar', processors=[ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})
    use_avatar = models.BooleanField(default=True)
    username = models.CharField(
        max_length=80, default="Unnamed", blank=True, help_text='Email stores in lowercase')
    jabber = models.CharField('Jabber', max_length=80, blank=True)
    icq = models.CharField('ICQ', max_length=12, blank=True)
    msn = models.CharField('MSN', max_length=80, blank=True)
    aim = models.CharField('AIM', max_length=80, blank=True)
    yahoo = models.CharField('Yahoo', max_length=80, blank=True)
    location = models.CharField(_('Location'), max_length=30, blank=True)
    is_moderator = models.BooleanField(default=False)
    created = models.DateTimeField(verbose_name=_('Crated'), auto_now_add=True)

    views = models.PositiveIntegerField(_('Views'), default=0, editable=False)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
        ordering = ['-created']
        get_latest_by = 'created'

    def get_absolute_url(self):
        return reverse("profile", args=[self.id])

    def get_avatar(self):
        if self.use_avatar and self.avatar:
            return self.avatar.url
        email_hash = hashlib.md5(self.email.lower()).hexdigest()
        url = 'http://www.gravatar.com/avatar/%s?s=200&d=identicon' % email_hash
        return url

    def clean(self):
        self.email = self.email.lower()

    def __unicode__(self):
        return _("{}'s ").format(self.username)

    def views(self):
        raise NotImplementedError()

    # For Custom User

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=50, unique=True)
    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['password']

    objects = MyUserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        if self.pk == 1:
            return True
        return False

    def has_module_perms(self, app_label):
        if self.pk == 1:
            return True
        return False

    @property
    def is_staff(self):
        return self.is_moderator


class Question(models.Model):
    tags = TaggableManager()
    name = models.CharField(_('Name'), max_length=60)
    slug = models.SlugField(
        _('Slug'), max_length=60)
    text = models.TextField(_('Question'))
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)
    created = models.DateTimeField(verbose_name=_('Crated'), auto_now_add=True)
    owner = models.ForeignKey(User, verbose_name=_('Owner'))
    # , editable=False)
    raiting = models.PositiveIntegerField(_('Plus'), default=0)
    voted = models.ManyToManyField(
        User, verbose_name=_('Voted'), related_name='voted_question', null=True, blank=True)
    cat = models.ForeignKey(
        Category, verbose_name=_('Category'), blank=False, null=True)

    views = models.PositiveIntegerField(_('Views'), default=0, editable=False)

    def tags_list(self):
        return ', '.join(tag.name for tag in self.tags.all())
    tags_list.short_description = 'Tags'

    def add_plus(self, user):
        if not (user in self.voted.all()):
            self.raiting += 1
            self.voted.add(user)
            self.save()

    def get_absolute_url(self):
        return reverse('question', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.id:
            self.do_unique_slug(slugify(self.name.strip()))
            import ipdb; ipdb.set_trace()

        super(Question, self).save(*args, **kwargs)

    def do_unique_slug(self, slug):
        orig_slug = slug
        counter = 1

        while True:
            import ipdb; ipdb.set_trace()
            if not self.__class__.objects.filter(slug=slug).exists():
                self.slug = slug
                break

            slug = '%s-%s' % (orig_slug, counter)
            counter += 1

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        unique_together = ('name', 'owner')

    def __unicode__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answers', verbose_name=_('Question'))
    text = models.TextField(verbose_name=_('Text'))
    updated = models.DateTimeField(verbose_name=_('Updated'), auto_now=True)
    created = models.DateTimeField(verbose_name=_('Crated'), auto_now_add=True)
    owner = models.ForeignKey(User, blank=False, verbose_name=_('Owner'))
    raiting = models.PositiveIntegerField(_('Plus'), default=0, editable=False)
    voted = models.ManyToManyField(
        User, verbose_name=_('Voted'), related_name='voted_answer', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.created)

    def add_plus(self, user):
        if not user in self.voted.all():
            self.raiting += 1
            self.voted.add(user)
            self.save()

    class Meta:
        ordering = ['-created']
        get_latest_by = 'created'
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
