from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	weight = models.FloatField()
	checklist = models.CharField(max_length=255)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		s = f'{self.author} - {self.title} - {self.date_posted}'
		return s

	def get_absolute_url(self): #kom tilbage til det når post,update,delete og post er lavet
		return reverse('weightloss-log')

class Checklist(models.Model):
	workout = models.TextField() #Split med komma? ,,,
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.author

	def get_absolute_url(self): #kom tilbage til det når post,update,delete og post er lavet
		return reverse('weightloss-checklist-update', kwargs={'pk': self.pk})