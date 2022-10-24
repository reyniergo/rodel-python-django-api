from rest_framework import serializers
from categorias.models import Categorias

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"