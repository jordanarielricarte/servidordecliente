from .models import Clientes
from .models import Cuentas
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientesSerializer
from .serializers import CuentasSerializer
from django.shortcuts import render

class ListaClientes(APIView):

    def get(self,request):
        clientes  = Clientes.objects.all()
        serializer = ClientesSerializer(clientes,context={"request":request},many=True)#El many true es porque donde extreamos varias fields son atributos del objectofield
                                                    #sino se pone true este extrae solo un objeto y nosotros estamos extrayendo varios objectos iterables
                                                    
        return Response(serializer.data) 
    def post(self,request):
        pass    

        
class ListaCuentas(APIView):

    def get(self,request):
        cuentas  = Cuentsa.objects.all()
        serializer = CuentasSerializer(cuentas,context={"request":request},many=True)#El many true es porque donde extreamos varias fields son atributos del objectofield
                                                    #sino se pone true este extrae solo un objeto y nosotros estamos extrayendo varios objectos iterables
                                                    
        return Response(serializer.data) 
    def post(self,request):
        pass      