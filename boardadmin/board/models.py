from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    name = models.TextField(blank=False)
    price = models.TextField(blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    descrip = models.TextField(blank=True)
    position = models.TextField(blank=False)
    date = models.DateField(auto_now_add=False)

def publish(self):
    self.published_date = timezone.now()
    self.save()
