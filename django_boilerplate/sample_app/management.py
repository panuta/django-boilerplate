# -*- encoding: utf-8 -*-

def after_syncdb(sender, **kwargs):
	pass

from django.db.models.signals import post_syncdb
post_syncdb.connect(after_syncdb, dispatch_uid="sample_app.management")