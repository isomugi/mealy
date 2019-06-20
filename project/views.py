from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from .models import Post, PostModel
from .forms import UserCreateForm, LoginForm

def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	context = { 'latest_post_list': latest_post_list }
	return render(request, 'project/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	context = { 'post': post }
	return render(request, 'project/detail.html', context)

def create(request):
	return render(request, 'project/create.html')

def post(request):
	if request.method == 'POST':
		form = PostModel(request.POST, request.FILES)
		if form.is_valid():
			new_post = form.save()
			return redirect('project:detail', post_id = new_post.id)
	else:
		form = PostModel()
	return render(request, 'project/create.html', { 'form': form })

def mypage(request):
	return render(request, 'project/mypage.html')

def register(request, *arg, **kwargs):
	if request.method == 'POST':
		form = UserCreateForm(data=request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('project:index')
	else:
		form = UserCreateForm()
	return render(request, 'registration/register.html', { 'form': form })

def login(request, *arg, **kwargs):
	if request.method == 'POST':
		form = LoginForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			user = User.objects.get(username=username)
			login(request, user)
			return redirect('project:index')
	else:
		form = LoginForm()
	return render(request, 'registration/login.html', { 'form': form })
