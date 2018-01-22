from django.shortcuts import render

# Create your views here.
def index(request):
    posts = [
        {'id': 1, 'title': 'First post', 'body': 'This is my first post'},
        {'id': 2, 'title': 'Second post', 'body': 'This is my second post'},
        {'id': 3, 'title': 'Third post', 'body': 'This is my third post'},
    ]
    return render(request, 'blog/index.html', {'posts': posts})

def show(request):
    