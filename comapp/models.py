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

# cette class n'est pas utilisé mais il peut dependre de forms.py, views.py avant de supprimer verifier 
# qu'il y a pas d'import dans views et forms
class client(models.Model):
    item = models.IntegerField()
    votre_nom = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.votre_nom} | {self.item}"