from django.shortcuts import render , get_object_or_404
from .models import Blog

def ablog(request):
    b = Blog.objects.order_by('-date')[:1]
    return render(request , 'blog/ablog.html', {'blogs': b})

def detail(request,blog_id):
    blog = get_object_or_404(Blog , pk=blog_id)
    return render(request , 'blog/detail.html',{'id':blog})