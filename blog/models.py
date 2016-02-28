from django.db import models
from django.utils import timezone
from time import time

def get_upload_file_name(instance , filename):
	return "uploaded_files/%s_%s" %(str(time()).replace('.','_'),filename)
	
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	text = models.TextField()
	thumbnail = models.FileField(upload_to = get_upload_file_name)
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True,null = True)
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __unicode__(self):
		return self.title
