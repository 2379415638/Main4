from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 20)
    usermail = models.EmailField()
    userpass = models.CharField(max_length=20)
    enabled = models.BooleanField(default = True)
    def __str__(self):
        return self.username