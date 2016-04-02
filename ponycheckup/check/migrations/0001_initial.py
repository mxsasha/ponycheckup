# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Check'
        db.create_table('check_check', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('hsts_header_found', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('xframe_header_found', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('admin_found', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('admin_forces_https', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('login_found', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('login_forces_https', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allows_trace', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('csrf_cookie_found', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('session_cookie_found', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('session_cookie_httponly', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('check', ['Check'])


    def backwards(self, orm):
        # Deleting model 'Check'
        db.delete_table('check_check')


    models = {
        'check.check': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Check'},
            'admin_forces_https': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admin_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allows_trace': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'csrf_cookie_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsts_header_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_forces_https': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'login_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'session_cookie_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session_cookie_httponly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'xframe_header_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['check']