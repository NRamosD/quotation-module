from re import template
from django.contrib import auth
from django.urls import path, include
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from rest_framework import routers

from . import views
from rest_framework import routers
from .views import (    
    CategoryViewSet,ProductViewSet, QuotesViewSet, RoleViewSet, FilesViewSet,
    SupplierViewSet, qDetailsViewSet, prosupViewSet,

    finalizarCotizacion,

    UserApiView, 
    
    userLogout, LoginView,
    
    uploadDocument,Reports,
    ListadoUsuario, ActualizarUsuaio, EliminarUsuario, CrearUsuario, 
    ProductosView, ProductosViewUpdate, ProductosViewDelete,
    ProveedoresView, ProveedoresViewDelete,ProveedoresViewUpdate,
    CategoriasView, CategoriasViewUpdate, CategoriasViewDelete
    
    )
router = routers.DefaultRouter()
#router.register('users', UsersViewSet)
router.register('product', ProductViewSet)
router.register('quotes', QuotesViewSet)
router.register('qDetails', qDetailsViewSet)
router.register('role', RoleViewSet)
router.register('category', CategoryViewSet)
router.register('suppliers', SupplierViewSet)
router.register('ProductFiles', FilesViewSet)
router.register('productSupplierJoin', prosupViewSet)




urlpatterns = [
    #VISTAS BÁSICAS
    #path('',views.index, name="index"),
    path('',views.home, name="home"),
    path('cotizar/',views.cotizar, name="quote"),
    path('guardar_cotizacion/', finalizarCotizacion.as_view(), name='saveQuote'),
    path('prueba/',views.pruebaHtml, name="prueba"),
    
    #API
    path('api/', include(router.urls)),
    path('api/user/', UserApiView.as_view(), name='user_api_view'),
    path('api/user/<int:pk>', UserApiView.as_view(), name='user_api_view'),
    #LOGIN / LOGOUT  
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', userLogout, name='logout'),
    #Productos
    path('productos/',ProductosView.as_view(), name="products"),
    path('productos/editar/<int:pk>',ProductosViewUpdate.as_view(), name="editProducts"),
    path('productos/eliminar/<int:pk>',ProductosViewDelete.as_view(), name="deleteProducts"),
    #Categorías
    path('categorias/',CategoriasView.as_view(), name="categories"),
    path('categorias/editar/<int:pk>',CategoriasViewUpdate.as_view(), name="editCategories"),
    path('categorias/eliminar/<int:pk>',CategoriasViewDelete.as_view(), name="deleteCategories"),
    #Proveedores
    path('proveedores/',ProveedoresView.as_view(), name="suppliers"),
    path('proveedores/editar/<int:pk>',ProveedoresViewUpdate.as_view(), name="editSuppliers"),
    path('proveedores/eliminar/<int:pk>',ProveedoresViewDelete.as_view(), name="deleteSuppliers"),
    #Users
    path('usuarios/',ListadoUsuario.as_view(), name="usersv"),
    path('editarusuario/<int:pk>',ActualizarUsuaio.as_view(), name="editUser"),
    path('eliminarusuario/<int:pk>', EliminarUsuario.as_view(), name='deleteUser'),
    path('crearusuario/', CrearUsuario.as_view(), name='createUser'),

    #upload data
    path('cargar_documento/',uploadDocument.as_view(), name="uploadDocument"),
    #reports
    path('informes/',login_required(Reports.as_view()), name="report"),
    
    #Loading
    path('loading/',views.loading, name="loading"),
    path('uploadT/',views.uploadT, name="uploadT")
]
