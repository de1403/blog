from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request) :
    blogs = Post.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id) :
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog_detail})
