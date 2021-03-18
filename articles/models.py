from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
ARTICLE_CATEGORIES = (
    ('BF&E', 'Business, Finances & Economics'),
    ('CS&T', 'Computers, Science & Technology'),
    ('EA&C', 'Entertainment, Art & Culture'),
    ('GN', 'General News'),
    ('H&M', 'Health & Medicine'),    
    ('Sports', 'Sports')
)


class Articles(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=31, choices=ARTICLE_CATEGORIES)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}, {self.date_created}'