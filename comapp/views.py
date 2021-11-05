from django.shortcuts import render,redirect

# table produit importer depuis models.py. voir models.py pour connaitre les champs qui contient
from . models import produit

# fonction qui controle index.html
def index(request):
    """
    - la var obj contient les objets de la tableau produit et seront ordonner inversement
    - la var taille contient la taille des objets : combien elements y sont
    - la var context est un dict contient les objets qui va être renvoyé dans le template
    """
    obj = produit.objects.all().order_by('-pk')
    taille = len(obj)
    context = {'produits':obj, 'taille':taille}
    return render(request, "comapp/index.html", context)

# fonction qui sert à supprimer l'article correspondant
def on_delete(request, id):
    """
    - cette fonction prend un parametre id qui sert à recuperer l'id dans la db et supprimer l'objet 
       puis redirecte vers index.html
    """
    produit.objects.get(id=id).delete()
    return redirect("comapp:index")

# fonction qui controle details.html
def details(request, id):
    """
    cette fonction prend un params id qui sert à faire la requete dans la table produit et renvoyé l'objet dans le template grace au
    dict context 
    """
    pk = produit.objects.get(id=id)
    context = {'produit': pk}
    return render(request, 'comapp/details.html', context)