# -*- coding: utf-8 -*-
from django.db import models
from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'question_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')
             (unique=True, max_length=80)),
            ('slug', self.gf('django.db.models.fields.SlugField')
             (unique=True, max_length=60)),
        ))
        db.send_create_signal(u'question', ['Category'])

        # Adding model 'User'
        db.create_table(u'question_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')
             (max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')
             (default=datetime.datetime.now)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')
             (max_length=100, blank=True)),
            ('use_avatar', self.gf('django.db.models.fields.BooleanField')
             (default=True)),
            ('username', self.gf('django.db.models.fields.CharField')
             (default=u'Unnamed', max_length=80, blank=True)),
            ('jabber', self.gf('django.db.models.fields.CharField')
             (max_length=80, blank=True)),
            ('icq', self.gf('django.db.models.fields.CharField')
             (max_length=12, blank=True)),
            ('msn', self.gf('django.db.models.fields.CharField')
             (max_length=80, blank=True)),
            ('aim', self.gf('django.db.models.fields.CharField')
             (max_length=80, blank=True)),
            ('yahoo', self.gf('django.db.models.fields.CharField')
             (max_length=80, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')
             (max_length=30, blank=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')
             (default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')
             (default=True)),
            ('email', self.gf('django.db.models.fields.EmailField')
             (unique=True, max_length=50)),
        ))
        db.send_create_signal(u'question', ['User'])

        # Adding model 'Question'
        db.create_table(u'question_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')
             (max_length=60)),
            ('slug', self.gf('django.db.models.fields.SlugField')
             (unique=True, max_length=60)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')
             (to=orm['question.User'])),
            ('raiting', self.gf('django.db.models.fields.PositiveIntegerField')
             (default=0)),
            ('cat', self.gf('django.db.models.fields.related.ForeignKey')
             (to=orm['question.Category'], null=True, blank=True)),
        ))
        db.send_create_signal(u'question', ['Question'])

        # Adding unique constraint on 'Question', fields ['name', 'owner']
        db.create_unique(u'question_question', ['name', 'owner_id'])

        # Adding M2M table for field voted on 'Question'
        m2m_table_name = db.shorten_name(u'question_question_voted')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID',
             primary_key=True, auto_created=True)),
            ('question',
             models.ForeignKey(orm[u'question.question'], null=False)),
            ('user', models.ForeignKey(orm[u'question.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['question_id', 'user_id'])

        # Adding model 'Answer'
        db.create_table(u'question_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')
             (primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name=u'answers', to=orm['question.Question'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')
             (auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')
             (auto_now_add=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')
             (to=orm['question.User'])),
            ('raiting', self.gf('django.db.models.fields.PositiveIntegerField')
             (default=0)),
        ))
        db.send_create_signal(u'question', ['Answer'])

        # Adding M2M table for field voted on 'Answer'
        m2m_table_name = db.shorten_name(u'question_answer_voted')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID',
             primary_key=True, auto_created=True)),
            ('answer', models.ForeignKey(orm[u'question.answer'], null=False)),
            ('user', models.ForeignKey(orm[u'question.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['answer_id', 'user_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'Question', fields ['name', 'owner']
        db.delete_unique(u'question_question', ['name', 'owner_id'])

        # Deleting model 'Category'
        db.delete_table(u'question_category')

        # Deleting model 'User'
        db.delete_table(u'question_user')

        # Deleting model 'Question'
        db.delete_table(u'question_question')

        # Removing M2M table for field voted on 'Question'
        db.delete_table(db.shorten_name(u'question_question_voted'))

        # Deleting model 'Answer'
        db.delete_table(u'question_answer')

        # Removing M2M table for field voted on 'Answer'
        db.delete_table(db.shorten_name(u'question_answer_voted'))

    models = {
        u'question.answer': {
            'Meta': {'ordering': "[u'-created']", 'object_name': 'Answer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['question.User']"}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'answers'", 'to': u"orm['question.Question']"}),
            'raiting': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'voted': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'voted_answer'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['question.User']"})
        },
        u'question.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'question.question': {
            'Meta': {'ordering': "[u'-created']", 'unique_together': "((u'name', u'owner'),)", 'object_name': 'Question'},
            'cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['question.Category']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['question.User']"}),
            'raiting': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '60'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'voted': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "u'voted_question'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['question.User']"})
        },
        u'question.user': {
            'Meta': {'object_name': 'User'},
            'aim': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50'}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'msn': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'use_avatar': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'default': "u'Unnamed'", 'max_length': '80', 'blank': 'True'}),
            'yahoo': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        }
    }

    complete_apps = ['question']
