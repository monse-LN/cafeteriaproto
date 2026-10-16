from django.shortcuts import render
from core.models import Service, Post

def home(request):
    return render(request, 'core/home.html')

def services(request):
    services_list = Service.objects.all()
    return render(request, 'core/services.html', {'services': services_list})

def blog(request):
    posts = Post.objects.all()
    return render(request, 'core/blog.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')