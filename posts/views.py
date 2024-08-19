from django.shortcuts import render, get_object_or_404
from .models import Post, CustomUser, Image


def index(request):
    # Fetch recent posts or any other data you want to display on the home page
    recent_posts = Post.objects.all()[:5]  # Display the 5 most recent posts
    return render(
        request, "index.html", {"title": "Home Page", "recent_posts": recent_posts}
    )


def about(request):
    # Example: Fetch a list of users to display on the about page
    users = CustomUser.objects.all()
    return render(request, "about.html", {"title": "About Page", "users": users})


def post_detail(request, post_id):
    # Fetch a specific post by its ID
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", {"title": post.title, "post": post})


def contact(request):
    # Typically, contact pages don't need to interact with models
    # However, you can include additional data if needed
    return render(request, "contact.html", {"title": "Contact Page"})
