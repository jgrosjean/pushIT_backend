from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Button, Action, LinkButtonAction, ObjectConnected, AllObject, ListView

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
    linkButtonAction = LinkButtonAction.objects.filter(id_button=format(id_button), id_action=format(id_action))
    if linkButtonAction :
        return HttpResponse("ce bouton fait deja cette action")
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

def listLinkButtonActionByButton(request, id_button):
    linkButtonAction = LinkButtonAction.objects.filter(id_button=format(id_button)).values()
    if linkButtonAction:
        listObject=list(linkButtonAction)
        return JsonResponse(listObject, safe=False)
    else:
        return HttpResponse("ERREUR : pas d'ation pour ce boutton")


def listView(request):
    obj = ListView()

    data = {
        'name': 'dzdzd',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }

    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')

    '''obj = ListView()
    obj.nom="jojojojo"
    obj.prenom='prenooom'
    listObject=list(obj)
    return JsonResponse(listObject, safe=False)
    '''

'''

def listView(request):

    file = open("test.txt","w")

    buttons_id = Button.objects.all().values_list('id', flat=True)

    buttons_name = Button.objects.all().values_list('name', flat=True)



    actions_idButton = LinkButtonAction.objects.all().values_list('id_button', flat=True)

    actions_idAction = LinkButtonAction.objects.all().values_list('id_action', flat=True)



    action_idAction = Action.objects.all().values_list('id', flat=True)

    action_idObject = Action.objects.all().values_list('id_objet_connected', flat=True)

    action_desc = Action.objects.all().values_list('description', flat=True)



    listButton = []

    for i in range(len(buttons_id)):

        listAction = []

        for j in range(len(actions_idButton)):

            if buttons_id[i] == actions_idButton[j]:

                for k in range(len(action_desc)):

                    if action_idAction[k] == actions_idAction[j]:

                        listAction.append(viewAction(action_idAction[k], action_idObject[k], action_desc[k]))

        listButton.append(viewButton(buttons_id[i], buttons_name[i], listAction))

    file.write(str(listButton[0]))

    file.close()

    return HttpResponse(listButton)
    '''