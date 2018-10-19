from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addButton/<name>', views.addButton, name='addButton'),
    path('listButton', views.listButton, name='listButton'),
    path('changeNameButton/<id>/<name>', views.changeNameButton, name='changeNameButton'),
    path('deleteButton/<id>', views.deleteButton, name='deleteButton'),

    path('addAllObject/<brand>/<reference>', views.addAllObject, name='addAllObject'),
    path('listAllObject', views.listAllObject, name='listAllObject'),
    path('deleteAllObject/<id>', views.deleteAllObject, name='deleteAllObject'),

    path('addObjectConnected/<ip>/<password>/<id_all_object>', views.addObjectConnected, name='addObjectConnected'),
    path('listObjectConnected', views.listObjectConnected, name='listObjectConnected'),
    path('deleteObjectConnected/<id>', views.deleteObjectConnected, name='deleteObjectConnected'),

    path('addAction/<id_objectConnected>/<description>', views.addAction, name='addAction'),
    path('listAction', views.listAction, name='listAction'),
    path('listActionByObjectConnected/<id>', views.listActionByObjectConnected, name='listActionByObjectConnected'),



    path('addLinkButtonAction/<id_button>/<id_action>', views.addLinkButtonAction, name='addLinkButtonAction'),
    path('listLinkButtonAction', views.listLinkButtonAction, name='listLinkButtonAction'),


]   