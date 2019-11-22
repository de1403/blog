from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone

# Create your views here.
def home(request) :
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def detail(request, blog_id) :
    post_detail = get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request) :
    return render(request, 'new.html')

def create(request) :
    new_blog = Post()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.date = timezone.datetime.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('/app_board/'+str(new_blog.id))

def edit(request,post_id): 
    edit_post = Post.objects.get(id = post_id)
    return render(request, 'edit.html', {'post':edit_post})

def update(request,post_id):
    update_post = Post.objects.get(id = post_id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    new_blog.date = timezone.datetime.now()
    update_blog.body=request.POST['body']
    update_blog.save()
    return redirect('/app_post'+str(update_blog.id))

def delete(request, post_id):
    delete_blog = Blog.objects.get( id = post_id)
    delete_blog.delete()
    return redirect('home')


