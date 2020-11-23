from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """The home page for Blog"""
    return render(request, 'blogs/index.html')

def blog_posts(request):
    """Show all blog posts"""
    blog_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts':blog_posts}
    return render(request, 'blogs/blog_posts.html',context)

def blog_post(request, blog_post_id):
    """Show a single blog post"""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    #entry = topic.order_by('-date_added')
    context={'blog_post':blog_post}
    return render(request, 'blogs/blog_post.html', context)

def new_post(request):
    """Add a new blog post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BlogPostForm()
    else:
        # POST data submitted; process data
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_posts')

    # Display a blank or invalid form
    context = {'form':form}
    return render(request, 'blogs/new_post.html', context)
    
def edit_blog_post(request, blog_post_id):
    """Editing an existing blog post"""
    blog_post = BlogPost.objects.get(id=blog_post_id)

    if request.method != 'POST':
        # Initial requst; pre-fill form with the current entry
        form = BlogPostForm(instance=blog_post)
    else:
        # POST data submitted; process data
        form = BlogPostForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog_post', blog_post_id=blog_post.id)

    context = {'blog_post':blog_post, 'form':form}
    return render(request, 'blogs/edit_blog_post.html', context)
