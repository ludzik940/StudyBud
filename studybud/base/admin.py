from django.contrib import admin

# Register your models here.


#importujemy z modlei tablice z bazy danych
from .models import Room, Topic, Message

#Musimy zarejestrowac tablice z bazy danych
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)