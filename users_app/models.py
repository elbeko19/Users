from django.db import models

# Create your models here.
class UsersModel(models.Model):
    email = models.EmailField()
    username = models.CharField(unique=True, max_length=24)
    password = models.IntegerField()
    
    def __str__(self):
        return self.username
    
    