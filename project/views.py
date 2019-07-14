from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as login, authenticate, logout

from .models import Post, PostModel, Like, Comment
from .forms import UserCreateForm, UserUpdateForm, LoginForm, CommentForm

def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	context = { 'latest_post_list': latest_post_list }
	return render(request, 'project/index.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk = post_id)
	form = CommentForm()
	context = { 'post': post ,'form': form}
	return render(request, 'project/detail.html', context)

def create(request):
	if not request.user.is_authenticated:
		return redirect('project:login')
	return render(request, 'project/create.html')

def post(request):
	if not request.user.is_authenticated:
		return redirect('project:login')
	elif request.method == 'POST':
		form = PostModel(request.POST, request.FILES)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.user = request.user
			new_post.save()
			return redirect('project:detail', post_id = new_post.id)
	else:
		form = PostModel()
	return render(request, 'project/create.html', { 'form': form })

def comment(request,post_id):
	post = get_object_or_404(Post, pk = post_id)
	if not request.user.is_authenticated:
		return redirect('project:login')
	elif request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('project:detail', post_id = post_id )

	return render(request, 'project/detail.html', { 'form': form ,'post': post})

def like(request, post_id):
	if not request.user.is_authenticated:
		return redirect('project:login')

	post = Post.objects.get(id=post_id)
	is_like = Like.objects.filter(user=request.user).filter(post=post).count()
    # unlike
	if is_like > 0:
		liking = Like.objects.get(post__id=post_id, user=request.user)
		liking.delete()
		post.like_num -= 1
		post.save()
		return redirect('project:detail', post_id = post.id)
    # like
	post.like_num += 1
	post.save()
	like = Like()
	like.user = request.user
	like.post = post
	like.save()
	return redirect('project:detail', post_id = post.id)


def mypage(request):
	if not request.user.is_authenticated:
		return redirect('project:login')
	return render(request, 'project/mypage.html')

def edit(request):
	if request.method == 'POST':
		form = UserUpdateForm(data=request.POST, instance=request.user)
		if form.is_valid():
			user = form.save()
			return JsonResponse({ 'user': user.username })
	return HttpResponse(form)

def register(request, *arg, **kwargs):
	if request.user.is_authenticated:
		return redirect('project:index')
	elif request.method == 'POST':
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

def login_view(request):
	if request.user.is_authenticated:
		return redirect('project:index')
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('project:index')
		else:
			form = LoginForm(request)
	else:
		form = LoginForm()
	return render(request, 'registration/login.html', { 'form': form })

def logout_view(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			logout(request)
	return redirect('project:index')
