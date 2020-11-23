"""Defines URL patterns for blogs"""
from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
        # Home page
        path('', views.index, name='index'),
        # Page to show all blog posts
        path('blog_posts/', views.blog_posts, name='blog_posts'),
        # Detail page for single blog posting
        path('blog_posts/<int:blog_post_id>/', views.blog_post, name='blog_post'),
        # Page for adding a new post
        path('new_post/', views.new_post, name='new_post'),
        # Page for editing a blog post
        path('edit_blog_post/<int:blog_post_id>/',views.edit_blog_post, name='edit_blog_post'),
        ]
