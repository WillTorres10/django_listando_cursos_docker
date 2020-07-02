from django.db import models

# Create your models here.

class Maratona(models.Model):
  titulo = models.CharField(max_length=200)