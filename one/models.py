from django.db import models

# Create your models here.

class facts(models.Model):
    
    hapclients = models.IntegerField()
    project = models.IntegerField()
    hosupport = models.IntegerField()
    award = models.IntegerField()
    
class progress(models.Model):
    
    skill = models.CharField(max_length=20)
    skillnow = models.IntegerField()
    
class enquiry(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()