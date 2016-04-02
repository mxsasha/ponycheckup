# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Check.heartbleed_vuln'
        db.add_column(u'check_check', 'heartbleed_vuln',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Check.heartbleed_vuln'
        db.delete_column(u'check_check', 'heartbleed_vuln')


    models = {
        u'check.check': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Check'},
            'admin_forces_https': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'admin_found': ('django.db.models.fields.BooleanField', [], {}),
            'allows_trace': ('django.db.models.fields.BooleanField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'csrf_cookie_found': ('django.db.models.fields.BooleanField', [], {}),
            'heartbleed_vuln': ('django.db.models.fields.BooleanField', [], {}),
            'hsts_header_found': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_forces_https': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'login_found': ('django.db.models.fields.BooleanField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'no_of_recommendations': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'runs_debug': ('django.db.models.fields.BooleanField', [], {}),
            'session_cookie_found': ('django.db.models.fields.BooleanField', [], {}),
            'session_cookie_httponly': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'session_cookie_secure': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'supports_https': ('django.db.models.fields.BooleanField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'xframe_header_found': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['check']