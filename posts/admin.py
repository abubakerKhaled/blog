from django.contrib import admin
from .models import CustomUser, Image, Post


# Register the CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )
    # Fields to search
    search_fields = ("username", "email", "first_name", "last_name")
    # Fields to filter by
    list_filter = ("is_active", "is_staff", "date_joined")


# Register the Image model
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("caption", "image")
    # Fields to search
    search_fields = ("caption",)


# Register the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("title", "author", "date")
    # Fields to search
    search_fields = ("title", "body")
    # Fields to filter by
    list_filter = ("author", "date")
