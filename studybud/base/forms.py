from django.forms import ModelForm
from .models import Room #importujemy model do ktorego chcemy zrobic form
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ['host', 'participants'] 
        # możemy wykluczyć rzeczy którycyh nie chcemy wyswietlać
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']