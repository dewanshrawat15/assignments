from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
import os
def get_upload_path(instance, filename):
	return os.path.join("projects/%s" % instance.author.username, "%s" % (instance.title + '.zip'))

class Project(models.Model):
	title = models.CharField(max_length=128)
	short_description = models.CharField(max_length=256)
	long_description = models.TextField()
	languages_or_Frameworks_used = models.CharField(max_length=512)
	submitted_Date_Time = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	project = models.FileField(upload_to=get_upload_path)

	def __str__(self):
		return self.title

	def delete(self, *args, **kwargs):
		os.remove(os.path.join(settings.MEDIA_ROOT, self.project.name))
		super(Project, self).delete(*args,**kwargs)