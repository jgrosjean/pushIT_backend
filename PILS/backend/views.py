from django.shortcuts import render
from django.http import JsonResponse
from .models import Button, Action, LinkButtonAction, ObjectConnected, AllObject

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the backend index boy.")

def addButton(request, name):
    p = Button(name=format(name))
    p.save()
    return HttpResponse("bouton ajouter par url donnes en cours")

def listButton(request):
    button = Button.objects.all().values()
    list_bouton=list(button)
    return JsonResponse(list_bouton, safe=False)

def changeNameButton(request, id, name):
    button = Button.objects.filter(id=format(id))
    if button :
        Button.objects.filter(id=format(id)).update(name=format(name))
        return HttpResponse("nom du bouton change ")
    else : 
        return HttpResponse("ERREUR : action non existante ")

def deleteButton(request, id):
    button = Button.objects.filter(id=format(id))
    if button :
        button.delete()
        return HttpResponse("bouton supprimer")
    else : 
        return HttpResponse("ERREUR : bouton non existante ")

def addAllObject(request, brand, reference):
    p = AllObject(brand=format(brand),reference=format(reference))
    p.save()
    return HttpResponse("allobjets ajouter par url donnes en cours")

def listAllObject(request):
    allObject = AllObject.objects.all().values()
    listObject=list(allObject)
    return JsonResponse(listObject, safe=False)

def deleteAllObject(request, id):
    allObject = AllObject.objects.filter(id=format(id))
    if allObject :
        allObject.delete()
        return HttpResponse("AllObject supprimer")
    else : 
        return HttpResponse("ERREUR : AllObject non existante ")

def addObjectConnected(request, ip, password, id_all_object):
    allObject=AllObject.objects.filter(id=format(id_all_object))
    if allObject:
        p = ObjectConnected(ip=format(ip), password=format(password), id_allObject=format(id_all_object))
        p.save()
        return HttpResponse("objectConnected ajouter par url donnes en cours")
    else : 
        return HttpResponse("objectConnected n a pas pu s'ajouter car pas de all object")

def listObjectConnected(request):
    objectConnected = ObjectConnected.objects.all().values()
    listObject=list(objectConnected)
    return JsonResponse(listObject, safe=False)

def deleteObjectConnected(request, id):
    objectConnected = ObjectConnected.objects.filter(id=format(id))
    if objectConnected :
        objectConnected.delete()
        return HttpResponse("objectConnected supprimer")
    else : 
        return HttpResponse("ERREUR : objectConnected non existante ")

def addAction(request, id_objectConnected, description): 
     objectConnected = ObjectConnected.objects.filter(id=format(id_objectConnected))
     if objectConnected : 
        p = Action(id_objet_connected=format(id_objectConnected), description=format(description))
        p.save()
        return HttpResponse("Action ajouter par url donnes en cours")
     else :
        return HttpResponse("ERREUR : objectConnected non existante ")

def listAction(request):
    action = Action.objects.all().values()
    listObject=list(action)
    return JsonResponse(listObject, safe=False)

def listActionByObjectConnected(request, id):                       #ne fonctionne pas
    action = Action.objects.all().values(description=format(id))
    listAction = list(action)
    return JsonResponse(listAction, safe=False)


def addLinkButtonAction(request, id_button, id_action):
    button=Button.objects.filter(id=format(id_button))
    action=Action.objects.filter(id=format(id_action))
    if button :
        if action :
            p = LinkButtonAction(id_button=format(id_button), id_action=format(id_action))
            p.save()
            return HttpResponse("linkbutonaction ajouter par url donnes en cours")
    else :
        return HttpResponse("ERREUR : button ou action non existante ")
    return HttpResponse("ERREUR : button ou action non existante ")


def listLinkButtonAction(request):
    linkbuttonAction = LinkButtonAction.objects.all().values()
    listObject=list(linkbuttonAction)
    return JsonResponse(listObject, safe=False)

