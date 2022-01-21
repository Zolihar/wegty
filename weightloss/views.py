from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Post, Checklist
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Din bruger er nu registreret!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	context = {
		'title': 'Registrer bruger',
		'form': form,
	}
	return render(request, 'weightloss/users/register.html', context)

@login_required
def home(request):
 	context = {
 		'title': 'Hjem'
 	}
 	return render(request, 'weightloss/home.html', context)

@login_required
def graph(request):
	model = Post.objects.filter(author=request.user).order_by('date_posted')
	e = False
	if model.first():
		e = True
	else:
		e = False
	context = {
		'title': 'Kurve',
		'weight': model,
		'exist': e
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

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cs = {
			'state': 'create',
			'title': 'Lav Tjekliste'
		}
		context["context"] = cs
		return context

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

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cs = {
			'state': 'update',
			'title': 'Opdater Tjekliste'
		}
		context["context"] = cs
		return context

class LogListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'weightloss/log.html'
	def get_queryset(self):
		author = Post.objects.filter(author=self.request.user).order_by('-date_posted')
		return author

	def get_context_data(self, **kwargs):
		author = Post.objects.filter(author=self.request.user)
		context = super().get_context_data(**kwargs)
		state = True
		if author:
			state = True
		else:
			state = False
		cs = {
			'state': state,
			'title': 'Indlæg'
		}
		context['context'] = cs
		return context

class LogCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'weight', 'content', 'checklist']

	def get_context_data(self, **kwargs):
		cl = Checklist.objects.filter(author=self.request.user).first()
		if cl:
			cl = cl.workout.split('\n')
		else:
			cl = "none"
		context = super().get_context_data(**kwargs)
		cs = {
			'checklist': cl,
			'title': 'Lav Indlæg'
		}
		context["context"] = cs
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

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cs = {
			'title': 'Slet indlæg'
		}
		context["context"] = cs
		return context

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

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cs = {
			'update': 'update',
			'title': 'Opdater indlæg'
		}
		context["context"] = cs
		return context