from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    options = (
        ('draft', "Draft"),
        ("published", "Published")
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now())
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=50, choices=options, default='draft')

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse("single_post", args=[str(self.slug)])
    

    def __str__(self):
        return self.title
    