from django.urls import path, include
from django.views import generic

from . import views
from rest_framework import routers
from .views import UsersViewSet

router = routers.DefaultRouter()
router.register('users', UsersViewSet)

urlpatterns = [
    path('',views.index, name="index"),
    path('login',views.login, name="login"),
    path('home',views.home, name="home"),
    path('api', include(router.urls)),
]


"""
path('', views.index, name="index"), 
path('view2/',
    generic.TemplateView.as_view(template_name='view2.html')),
path('',
    generic.TemplateView.as_view(template_name='view1.html')),"""