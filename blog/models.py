from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

User = settings.AUTH_USER_MODEL

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    passage = models.TextField()
    num_views = models.IntegerField(default=0, editable=False)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) #manually set publish date to make visible to viewers
    timestamp = models.DateField(auto_now_add=True) #automatically set when article first created in database
    updated = models.DateField(auto_now=True) #automatically updated each time object is saved (updated)

    class Meta:
        ordering = ["-publish_date", "-updated", "-timestamp"]

    def get_absolute_url(self):
        return str(self.slug)
