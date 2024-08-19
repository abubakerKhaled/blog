from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
