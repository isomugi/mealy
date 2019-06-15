from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from .models import Post, PostModel

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
