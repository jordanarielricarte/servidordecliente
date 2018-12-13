from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.ListaClientes.as_view()),
    path('',views.ListaCuentas.as_view()),

]
