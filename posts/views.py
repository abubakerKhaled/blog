from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'title': 'Home Page'})

def about(request):
    return render(request, 'about.html', {'title': 'About Page'})

def post(request):
    return render(request, 'post.html', {'title': 'Post Page'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Contact Page'})