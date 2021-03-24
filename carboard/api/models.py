from django.db import models

# Create your models here.
# before sending data to clients, we need to serialize it - JSON as endpoint

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
