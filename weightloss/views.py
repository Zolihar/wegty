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
def guide(request):
 	context = {
 		'title': 'Guides'
 	}
 	return render(request, 'weightloss/guide.html', context)

class LogListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'weightloss/log.html'
	ordering = ['-date_posted']
	def get_queryset(self):
		author = Post.objects.filter(author=self.request.user)
		return author



class LogCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'weight', 'content', 'checklist']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class LogDetailView(LoginRequiredMixin, DetailView):
	model = Post

class LogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = "/log"

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class LogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'weight', 'content', 'checklist']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False