from django.urls import path, include
from django.views import generic
from django.contrib.auth import views as auth_views

from . import views
from rest_framework import routers
from .views import UsersViewSet

router = routers.DefaultRouter()
router.register('users', UsersViewSet)

urlpatterns = [
    path('',views.index, name="index"),
    #path('login',views.login, name="login"),
    #path('login', auth_views.LoginView.as_view(template_name='quote/html/login.html'), name="login"),
    path('users/', include('django.contrib.urls')),
    path('api', include(router.urls)),
]


"""
path('', views.index, name="index"), 
path('view2/',
    generic.TemplateView.as_view(template_name='view2.html')),
path('',
    generic.TemplateView.as_view(template_name='view1.html')),"""