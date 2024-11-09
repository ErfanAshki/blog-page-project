from django.db import models


class Post(models.Model):
    STATUS_CONDITION = (
        ('PUB', 'PUBLISHED'),
        ('DRF', 'DRAFT')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CONDITION, max_length=5)

