from django.shortcuts import render, get_object_or_404
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

@login_required
def home(request):
 	context = {
 		'title': 'Home'
 	}
 	return render(request, 'weightloss/home.html', context)

@login_required
def log(request):
 	context = {
 		'title': 'Log'
 	}
 	return render(request, 'weightloss/log.html', context)

@login_required
def post(request):
 	context = {
 		'title': 'Post'
 	}
 	return render(request, 'weightloss/post.html', context)

@login_required
def guide(request):
 	context = {
 		'title': 'Guides'
 	}
 	return render(request, 'weightloss/guide.html', context)

class LogListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'weightloss/log.html'
	ordering = ['-date_posted']

class LogCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'weight', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class LogDetailView(LoginRequiredMixin, DetailView):
	model = Post
