from django.shortcuts import render, redirect
from django.http import Http404
from .models import Post
from .parser import *


def posts_list(request):
    urls = Post.objects.all().order_by('timeshift').values()
    return render(request, 'blog/index.html', context={'urls': urls})


def parser(request):
    start(request)
    return redirect('http://localhost:8000/')


def view_post(request):
    url = request.build_absolute_uri()[:-1] if request.build_absolute_uri()[-1:] == '/' else request.build_absolute_uri()
    date = Post.objects.filter(url=url).values()
    if date:
        return render(request, 'blog/page_post.html', context={'date': date})
    else:
        raise Http404
