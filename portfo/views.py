from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Blog
from . forms import *

# Create your views here.
def index(request):
    return render(request, 'portfo/index.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contact')
    return render(request, 'portfo/contact.html')

def about(request):
    return render(request, 'portfo/about.html')

def project(request):
    return render(request, 'portfo/project.html')

def dash(request):
    return render(request, 'portfo/dashboard.html')

def blog(request):
    blog_post = Blog.objects.all()
    blog_content = {
        'blog_post': blog_post,
    }
    return HttpResponse(loader.get_template('portfo/blog.html').render(blog_content))
    