from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.title}'
