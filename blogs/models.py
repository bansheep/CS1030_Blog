from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """A blog post written by the user"""
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'blog posts'

    def __str__(self):
        """Return a string represntation of the model"""
        return self.title
