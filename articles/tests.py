from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Articles


class ArticleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username='testuser1',
            password='testing123456'
        )

        testuser1.save()

        testarticle = Articles.objects.create(
            author=testuser1,
            title='Test Title 1',
            category='Sports',
            body='Test content for test article'
        )

        testarticle.save()

    
    def test_article_content(self):
        article = Articles.objects.get(id=1)
        actual_author = str(article.author)
        actual_title = str(article.title)
        actual_category = str(article.category)
        actual_body = str(article.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_title, 'Test Title 1')
        self.assertEqual(actual_category, 'Sports')
        self.assertEqual(actual_body, 'Test content for test article')