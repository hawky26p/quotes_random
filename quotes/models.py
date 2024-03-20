from django.db import models

# Create your models here.

class Quote(models.Model):
    text=models.TextField()
    author=models.CharField(max_length=300)

    def __str__(self):
        return self.text