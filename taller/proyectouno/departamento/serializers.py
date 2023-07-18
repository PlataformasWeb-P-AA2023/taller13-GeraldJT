from django.contrib.auth.models import User, Group
from departamento.models import *

from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio
        fields = '__all__'

class PropietarioSerializer(serializers.HyperlinkedModelSerializer):
    departamentos = serializers.SerializerMethodField(); 
    edificios = serializers.SerializerMethodField();
    class Meta:
        model = Propietario
        fields = '__all__' 
    def get_departamentos(self,obj):
        return obj.get_departamentos()
    def get_edificios(self,obj):
        return obj.get_edificios()
    
 
class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__' 

