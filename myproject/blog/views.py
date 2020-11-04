from . models import Post
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,3)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    category = 'all'
    return render(request, 'index.html', {'posts': posts, 'category':'all'})
def view(request, slug_text):
    post = Post.objects.filter(slug = slug_text)
    if(post.exists()):
        post = post.first()
    #print(post.title)
    return render(request, 'view.html', {'post':post})

def programming(request):
    posts = Post.objects.filter(category = 'programming')
    paginator = Paginator(posts,3)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts, 'category':'programming'})
def tech(request):
    posts = Post.objects.filter(category = 'tech')
    paginator = Paginator(posts,3)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts,'category':'tech'})
def life(request):
    posts = Post.objects.filter(category = 'life')
    paginator = Paginator(posts,3)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts, 'category':'life'})