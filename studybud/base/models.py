from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Tworzymy tu table dla bazy danych

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # nie moze być puste
    participants = models.ManyToManyField(
        User, 
        related_name='participants', 
        blank=True
        ) #many to many fields in database pozwala łączyć wiele pól z innymi polami w bazie danych
    updated = models.DateTimeField(auto_now=True) # zapisuje godzine w kotrej zostało zaktualizowane
    created = models.DateTimeField(auto_now_add=True) # zapisuje tylko timestamp kiedy bylo utworzone
    
    class Meta:
        ordering = ['-updated', '-created'] #ustawia nam kolejnosc postow wzgledem update i created
    
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #łączenie w bazie danych pomeidzy modelami/ jeżeli 'rodzic' zostanie usuniety wszystko inne w pokoju zostanie usuniete
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
    
    class Meta:
        ordering = ['-updated', '-created']
    
#po utworzeniu modelu musimy migrować zmiany | tworzy wteyd nowy plik w folderze migrations