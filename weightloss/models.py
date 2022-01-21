from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100, verbose_name='Titel')
	content = models.TextField(verbose_name='Indhold')
	weight = models.FloatField(verbose_name='Vægt')
	checklist = models.CharField(max_length=255, verbose_name='Tjekliste')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		s = f'{self.author} - {self.title} - {self.date_posted}'
		return s

	def get_absolute_url(self): #kom tilbage til det når post,update,delete og post er lavet
		return reverse('weightloss-log')

class Checklist(models.Model):
	workout = models.TextField() #Split med komma? ,,, splitter med ny linje istedet
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		s = f'{self.author}'
		return s

	def get_absolute_url(self): #kom tilbage til det når post,update,delete og post er lavet
		return reverse('weightloss-checklist-update', kwargs={'pk': self.pk})