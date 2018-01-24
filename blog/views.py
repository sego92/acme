from django.shortcuts import render
from django.http import Http404

#from .mocks import Post
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def show(request, id):
    post = get_object_or_404(Post, pk=id)
    """try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404('Sorry the post #{} was not found.'.format(id))"""
    return render(request, 'blog/show.html', {'post': post})
    