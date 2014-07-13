from django.db import models

# Create your models here.
class Entry(models.Model):
	'''
		The posts Model
	'''
	title = models.TextField()
	body = models.TextField()
	guid = models.TextField() 

	def __str__(self):
		return "%s (%s)" % (self.title, self.body) 