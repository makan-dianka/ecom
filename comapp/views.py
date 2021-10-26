from django.shortcuts import render
from . models import produit, client
from . forms import ClientForm

# Create your views here.
def index(request):
    obj = produit.objects.all()
    context = {'produits':obj}
    return render(request, "comapp/index.html", context)

def details(request, id):
    pk = produit.objects.get(id=id)
    cli = client.objects.get(item=id)
    if request.method=="POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClientForm
    context = {'produit': pk, 'form':form, 'item':cli}
    return render(request, 'comapp/details.html', context)

def pagne(request, id):
    pk = produit.objects.get(id=id)
    context = {'produit': pk}
    return render(request, 'comapp/pagne.html', context)
