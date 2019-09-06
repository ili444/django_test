from django.shortcuts import render
from .models import Post
from .parser import *


def posts_list(request):
    start(request)
    urls = Post.objects.all().order_by('timeshift').values()
    return render(request, 'blog/index.html', context={'urls': urls})

def view_post(request):
    if request.path[-1:] == '/':
        path = request.path[:-1]
    else:
        path = request.path
    url = 'http://localhost:8000' + path
    date = Post.objects.filter(url=url).values()
    if date:
        return render(request, 'blog/page_post.html', context={'date': date})
    else:
        raise Http404
