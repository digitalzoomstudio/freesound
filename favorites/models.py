# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Favorite(models.Model):
    user = models.ForeignKey(User)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = generic.GenericForeignKey()

    created = models.DateTimeField(db_index=True, auto_now_add=True)
    
    def __unicode__(self):
        return u"%s favorites %s - %s" % (self.user, self.content_type, self.content_type)
    
    class Meta:
        unique_together = (('user', 'content_type', 'object_id'),)
        ordering = ("-created", )