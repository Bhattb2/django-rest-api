from django.contrib import admin

# Register your models here.
from .models import ARTICLE_CATEGORIES, Articles

admin.site.register(Articles)
