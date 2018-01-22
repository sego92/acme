from django.shortcuts import render

# Create your views here.
def index(request):
    posts = ['First post', 'Second Post', 'Third Post']
    return render(request, 'blog/index.html', {'posts': posts})