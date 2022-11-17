from rest_framework.serializers import ModelSerializer
from .models import AuthUser

class dataSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        fields ='__all__'