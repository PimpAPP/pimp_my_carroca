from django.db import models

# Create your models here.
class Points(models.Model):
   point_id = models.IntegerField()
   nome = models.TextField()
   telefone = models.TextField()
   latitude = models.DecimalField(decimal_places=8, max_digits=11)
   longitude =  models.DecimalField(decimal_places=8, max_digits=11)
   tipo = models.TextField()
