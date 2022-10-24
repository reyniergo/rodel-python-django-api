from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from categorias.serializers import CategoriasSerializer
from categorias.models import Categorias

# View - Read
class readCategorias(ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

# View - Create
class createCategorias(CreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

# View - Update
class updateCategorias(UpdateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

# View - Delete
class deleteCategorias(DestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer