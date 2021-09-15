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



#{"username":"nr", "password":"Gabibonito25."}
class SignInView(APIView):
    template_name='quote/html/login.html'
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        print(username)
        print(password)
        user = Users.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Contraseña incorrecta')
        
            """         if user:
            login(request, user)
            return Response(
                UserSerializer(Users).data,
                status=status.HTTP_200_OK) """      
        return Response({
            'message': 'Ingreso exitoso'
        })


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


"""def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })"""


