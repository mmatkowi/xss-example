from django.shortcuts import render
from django.http import HttpResponse

from app.models import Post

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        print(request.POST.body)

def posts(request):
    search_term = request.GET.get('searchTerm', '')
    posts = Post.objects.filter(title__contains=search_term)
    return render(request, "posts.html", {"search_term": search_term, "posts": posts})

def post(request):
    id = request.GET.get('id', '')
    post = Post.objects.get(id=id)
    return render(request, "post.html", {"post": post})