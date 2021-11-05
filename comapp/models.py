from django.db import models

# table produit
class produit(models.Model):
    """
    - champ designation str 255 caractere
    - champ img fichier image qui sera localisé dans le dossier ..image à la racine 
    - champ description est un text area de 500 caractere
    - champ price est un decimal. float
    """
    designation = models.CharField(max_length=255)
    img = models.ImageField(upload_to="images", blank=True, default='')
    description = models.TextField(max_length=500)
    price = models.FloatField()

    # produit return designation et price
    def __str__(self):
        return f"{self.designation} | {self.price}"