from django.db import models
from django.utils import timezone
# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=128)
	short_description = models.CharField(max_length=256)
	long_description = models.TextField()
	languages_or_Frameworks_used = models.CharField(max_length=512)
	submitted_Date_Time = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	def __str__(self):
		return self.title