from django.db import models

class questions(models.Model):
	question = models.CharField(max_length = 30)
	courses = models.CharField(max_length = 10)

	def __str__(self):
		return self.question


class profile(models.Model):
	email=models.CharField(max_length=30)
	username=models.CharField(max_length=10)
	address=models.CharField(max_length=10)
	# emp_id=models.IntegerField()

	def __str__(self):
		return self.email


