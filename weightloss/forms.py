from django import forms
from django.forms import ModelForm
from .models import Checklist

class ChecklistRegisterForm(ModelForm):
	workout = forms.CharField(max_length=255)

	class Meta:
		model = Checklist
		fields = ['workout']

	def save(self):
	 	data = self.cleaned_data
	 	checklist = Checklist(workout=data['workout'], author=user)
	 	checklist.save()