from django.urls import path
from categorias import views

urlpatterns = [
    path("",views.readCategorias.as_view(),name="categorias_read"), # Read
    path("create/", views.createCategorias.as_view(),name="categorias_create"), # Create
    path("update/<int:pk>/",views.updateCategorias.as_view(),name="categorias_update"), # Update
    path("delete/<int:pk>/",views.deleteCategorias.as_view(),name="categorias_delete") # Delete
]
