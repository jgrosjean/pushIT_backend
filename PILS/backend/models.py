from django.db import models

class Button(models.Model):
    name=models.CharField(max_length=100, default='default_name')

    def __str__(self):
        return '%s' % (self.name)

class Action(models.Model):
    id_objet_connected = models.IntegerField(default=0)  
    description = models.CharField(max_length=100, default='default_description')

    def __str__(self):
        return '%s %s' % (self.id_objet_connected, self.description)

class LinkButtonAction(models.Model):
    id_button = models.IntegerField(default=0)
    id_action = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.id_button, self.id_action)

class ObjectConnected(models.Model):
    ip = models.CharField(max_length=100, default='default_ip')
    password = models.CharField(max_length=100, default='default_password')
    id_allObject = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s %s  ' % (self.ip, self.password, self.id_allObject)

class AllObject(models.Model):
    brand = models.CharField(max_length=100, default='default_brand')
    reference = models.CharField(max_length=100, default='default_reference')

    def __str__(self):
        return '%s %s ' % (self.brand, self.reference)

