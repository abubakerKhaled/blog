from django.shortcuts import render, get_object_or_404
from .models import Post, CustomUser, Image
from django.core.paginator import Paginator

def index(request):
    # Fetch all posts
    all_posts = Post.objects.all().order_by('-date')  # Order posts by date in descending order

    # Set up pagination
    paginator = Paginator(all_posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')  # Get the page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the posts for the current page

    return render(
        request, 
        "index.html", 
        {
            "title": "Home Page",
            "page_obj": page_obj,  # Pass the page object to the template
        }
    )

def about(request):
    users = CustomUser.objects.all()
    return render(request, "about.html", {"title": "About Page"})

def post_detail(request, post_id):
    # Fetch a specific post by its ID
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", {"title": post.title, "post": post})

def contact(request):
    return render(request, "contact.html", {"title": "Contact Page"})

def profile(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, "profile.html", {"title": user.username, 'user': user})