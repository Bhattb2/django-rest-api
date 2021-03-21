from rest_framework import serializers

from .models import Articles


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'category', 'title', 'body', 'date_created', 'last_updated')
        model = Articles