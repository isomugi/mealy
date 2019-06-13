from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render

from .models import Post

def index(request):
	latest_post_list = Post.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_post_list': latest_post_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, post_id):
	try:
		Post = Post.objects.get(pk = post_id)
	except Post.DoesNotExist:
		raise Http404('Post does not exist.')
	return render(request, 'polls/detail.html', { 'post': post })
