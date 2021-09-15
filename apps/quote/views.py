from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

import jwt, datetime
#decorators
from django.contrib.auth.decorators import login_required

#local files
from .models import Users
from .serializers import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

# Create your views here.
@login_required
def index(request):
    return render(request, "./quote/index.html")

def login_plain(request):
    return render(request, "./quote/html/login.html")
@login_required
def home(request):
    return render(request, "./quote/html/home.html")

def cotizar(request):
    return render(request, "./quote/html/cotizar.html")


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'quote/html/home.html'
    login_url = 'quo:login'



#{"username":"jaja", "password":"123123123"}
class SignInView(APIView):
    template_name='quote/html/login.html'
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        print(username)
        print(password)
        user = Users.objects.filter(username=username).first()

        print(f"Lo que devuelve el user: {user}")

        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Contraseña incorrecta')

        payload = {
            'id': user.id_user,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow() 
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        return Response({
            'message': 'Ingreso exitoso',
            'jwt': token
        })


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


"""def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })"""


