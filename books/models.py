from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(
            max_length = 1024
            )
    author_name = models.CharField(
            max_length = 1023
            )
    def __str__(self):
        return ' '.join([self.name, 'by', self.author_name])
