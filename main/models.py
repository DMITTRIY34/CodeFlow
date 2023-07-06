from django.db import models

# Create your models here.

class Card(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    