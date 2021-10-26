from django.shortcuts import render,redirect
from . models import produit, client
from . forms import ClientForm

# Create your views here.
def index(request):
    obj = produit.objects.all().order_by('-pk')
    taille = len(obj)
    context = {'produits':obj, 'taille':taille}
    return render(request, "comapp/index.html", context)

def on_delete(request, id):
    id = int(id)
    obj = produit.objects.get(id=id).delete()
    return redirect("comapp:index")


def details(request, id):
    pk = produit.objects.get(id=id)
    context = {'produit': pk}
    return render(request, 'comapp/details.html', context)

def pagne(request, id):
    pk = produit.objects.get(id=id)
    context = {'produit': pk}
    return render(request, 'comapp/pagne.html', context)
