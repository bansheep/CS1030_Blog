from django.db import models

class BlogPost(models.Model):
    """A blog post written by the user"""
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'blog posts'

    def __str__(self):
        """Return a string represntation of the model"""
        return self.title
