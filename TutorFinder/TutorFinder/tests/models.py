from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Tutor_profile(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)


	def __str__(self):
		return self.fname
		return self.lname
