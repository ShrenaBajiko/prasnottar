from django.db import models

class questions(models.Model):
	question = models.CharField(max_length = 30)
	courses = models.CharField(max_length = 10)

	def __str__(self):
		return self.question
