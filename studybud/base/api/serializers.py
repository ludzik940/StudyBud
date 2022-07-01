from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializier(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        