from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Post, Checklist
from .forms import ChecklistRegisterForm

@login_required
def home(request):
 	context = {
 		'title': 'Home'
 	}
 	return render(request, 'weightloss/home.html', context)

@login_required
def graph(request):
	model = Post.objects.filter(author=request.user)
	context = {
		'title': 'Graphs',
		'weight': model
	}
	return render(request, 'weightloss/graph.html', context)

@login_required
def checklist(request):
	model = Checklist.objects.filter(author=request.user).first()
	if model:
		return redirect('weightloss-checklist-update', pk=model.pk)
	else:
		return redirect('weightloss-checklist-create')
	return render(request, 'weightloss/checklist.html')

class ChecklistCreateView(LoginRequiredMixin, CreateView):
	model = Checklist
	fields = ['workout']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ChecklistUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Checklist
	fields = ['workout']
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class LogListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'weightloss/log.html'
	def get_queryset(self):
		author = Post.objects.filter(author=self.request.user).order_by('-date_posted')
		return author

class LogCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'weight', 'content', 'checklist']

	def get_context_data(self, **kwargs):
		cl = Checklist.objects.filter(author=self.request.user).first()
		if cl:
			cl = cl.workout.split(',')
		else:
			cl = "none"
		context = super().get_context_data(**kwargs)
		context["checklist"] = cl
		return context

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