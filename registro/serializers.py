from .models import Clientes
from .models import Cuentas
from rest_framework import serializers

class ClientesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Clientes
        fields = '__all__'

class CuentasSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cuentas
        fields = '__all__'