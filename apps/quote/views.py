#DJANGO
from django.http.response import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views import View
from django.forms import model_to_dict
#RESTFRAMEWORK
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
#DECORATORS
from django.contrib.auth.decorators import login_required
#LOCAL FILES
from .models import Users, Product, Suppliers, Category, qDetails, Quotes
from .serializers import UserSerializer
import jwt, datetime
#API DRF
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


#VISTAS BÁSICAS
@login_required
def index(request):
    return render(request, "./quote/index.html")

def login_plain(request):
    return render(request, "./quote/html/login.html")

@login_required
def home(request):
    return render(request, "./quote/html/sectionHome.html")

@login_required
def cotizar(request):
    return render(request, "./quote/html/sectionQuote.html")

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'quote/html/home.html'
    login_url = 'quo:login'


#------------------------------LOGIN----------------------------------
# usuario de prueba {"username":"jaja", "password":"123123123"}
class SignInView(APIView):
    template_name='quote/html/login.html'
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        print(username)
        print(password)
        user = Users.objects.filter(username=username).first()

        print(f"Lo que devuelve el user: {user.id_user}")

        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Contraseña incorrecta')

        payload = {
            'id': user.id_user,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow() 
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')#.decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt',value=token, httponly=True)

        response.data = {
            'message': 'Ingreso exitoso',
            'jwt': token
        }
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Autenticación fallida')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            raise AuthenticationFailed('Autenticación fallida')
        
        user = Users.objects.filter(id_user=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        logout(request)
        response.data = {
            'message':'Cierre de sesión exitoso'
        }
        #logout(request)
        return response

#------------------------------SUPLLIERS----------------------------------
class SuppliersListView(View):
    def get(self, request):
        suppliersList = Suppliers.objects.all()
        return JsonResponse(list(suppliersList.values()), safe=False)

class SuppliersDetailView(View):
    def get(self, request, pk):
        oneSupplier = Suppliers.objects.get(pk=pk)
        return JsonResponse(model_to_dict(oneSupplier))

#------------------------------CATEGORY----------------------------------
class CategoryListView(View):
    def get(self, request):
        categoryList = Category.objects.all()
        return JsonResponse(list(categoryList.values()), safe=False)

class CategoryDetailView(View):
    def get(self, request, pk):
        oneCategory = Category.objects.get(pk=pk)
        return JsonResponse(model_to_dict(oneCategory))

#------------------------------QUOTE DETAILS----------------------------------
class qDetailsListView(View):
    def get(self, request):
        quoteDetailsList = qDetails.objects.all()
        return JsonResponse(list(quoteDetailsList.values()), safe=False)

class qDetailDetailView(View):
    def get(self, request, pk):
        oneQuoteDetail = qDetails.objects.get(pk=pk)
        return JsonResponse(model_to_dict(oneQuoteDetail))


#------------------------------QUOTE----------------------------------
class QuoteListView(View):
    def get(self, request):
        quoteList = Quotes.objects.all()
        return JsonResponse(list(quoteList.values()), safe=False)

class QuoteDetailView(View):
    def get(self, request, pk):
        oneQuote = Quotes.objects.get(pk=pk)
        return JsonResponse(model_to_dict(oneQuote))


#------------------------------PRODUCTS----------------------------------
class ProductListView(View):
    def get(self, request):
        productList = Product.objects.all()
        return JsonResponse(list(productList.values()), safe=False)

class ProductDetailView(View):
    def get(self, request, pk):
        oneProduct = Product.objects.get(pk=pk)
        return JsonResponse(model_to_dict(oneProduct))
