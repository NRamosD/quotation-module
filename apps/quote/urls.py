from django.urls import path, include
from django.views import generic
from django.contrib.auth import views as auth_views

from . import views
from rest_framework import routers
from .views import Home, UsersViewSet, SignInView, LogoutView, UserView, SuppliersListView, SuppliersDetailView, CategoryListView, CategoryDetailView, qDetailsListView, qDetailDetailView, QuoteListView, QuoteDetailView, ProductDetailView, ProductListView

router = routers.DefaultRouter()
router.register('users', UsersViewSet)

""" 
    path('',views.index, name="index"),
    path('home',views.home, name="home"),
    path('',Home.as_view(), name="home"),
    path('api/', include(router.urls)),
    #path('accounts/', include('django.contrib.urls')),
    #path('login',views.login, name="login"),
    #path('',views.index, name="index"),
     """
urlpatterns = [
    #VISTAS BÁSICAS
    path('',views.home, name="home"),
    path('cotizar/',views.cotizar, name="quote"),
    path('login/', auth_views.LoginView.as_view(template_name='quote/html/login.html'), name="login"),
    
    #API USERS
    path('api/', include(router.urls)),
    path('api/suppliers/', SuppliersListView.as_view(), name='api_allsuppliers'),
    path('api/suppliers/<int:pk>', SuppliersDetailView.as_view(), name='api_onesupplier'),
    path('api/categories/', CategoryListView.as_view(), name='api_allcategories'),
    path('api/category/<int:pk>', CategoryDetailView.as_view(), name='api_onecategory'),
    path('api/qDetails/', qDetailsListView.as_view(), name='api_allqDetails'),
    path('api/qDetails/<int:pk>', qDetailDetailView.as_view(), name='api_oneqDetails'),
    path('api/quotes/', QuoteListView.as_view(), name='api_allquote'),
    path('api/quotes/<int:pk>', QuoteDetailView.as_view(), name='api_onequote'),
    path('api/products/', ProductListView.as_view(), name='api_allquote'),
    path('api/products/<int:pk>', ProductDetailView.as_view(), name='api_onequote'),
    #API INICIO DE SESIÓN
    path('api/login/', SignInView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/user/', UserView.as_view(), name='api_user_view')
]
