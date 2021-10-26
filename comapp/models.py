from django.db import models

# Create your models here.
class produit(models.Model):
    designation = models.CharField(max_length=255)
    image = models.URLField()
    img = models.ImageField(upload_to="image", blank=True, default='')
    description = models.TextField(max_length=500)
    price = models.FloatField()

    def __str__(self):
        return f"{self.designation} | {self.price}"

class client(models.Model):
    item = models.IntegerField()
    votre_nom = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.votre_nom} | {self.item}"