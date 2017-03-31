from __future__ import unicode_literals

from django.db import models

# Create your models here.

class link(models.Model):
	links = models.TextField()
	date = models.DateTimeField(auto_now = True, auto_now_add = False)



def __unicode__(self):
	return self.links