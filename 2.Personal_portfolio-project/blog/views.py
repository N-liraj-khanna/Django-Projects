from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, "blog/all_blogs.html", {'count': len(blogs),'blogs': blogs})

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/blog_details.html", {'blog': blog})