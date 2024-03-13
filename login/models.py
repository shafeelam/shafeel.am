from django.db import models

# Create your models here.

class messages(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()