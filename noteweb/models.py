from django.db import models
import datetime

# Create your models here.
class addNote(models.Model):
    username = models.TextField()
    email = models.EmailField()
    title = models.TextField()
    desc = models.TextField()
    # date = models.DateField()

    def __str__(self):
        return self.username
    