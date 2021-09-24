#DJANGO
from django.contrib.auth.models import User
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.views import generic
from django.views import View
from django.forms import model_to_dict
from django.views.generic.base import TemplateView
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
from .models import Role, Users, Product, Suppliers, Category, qDetails, Quotes
from .serializers import (
    UserSerializer, CategorySerializer, QuotesSerializer, qDetailsSerializer, 
    RoleSerializer, SupplierSerializer, ProductSerializer)
import jwt, datetime

""" RUTAS DE LA API
    Métodos a usar: GET, POST, PATCH, DELETE
    "product": "http://127.0.0.1:8000/api/product/",
    "quotes": "http://127.0.0.1:8000/api/quotes/",
    "qDetails": "http://127.0.0.1:8000/api/qDetails/",
    "role": "http://127.0.0.1:8000/api/role/",
    "category": "http://127.0.0.1:8000/api/category/",
    "suppliers": "http://127.0.0.1:8000/api/suppliers/"
 """



#API DRF

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class QuotesViewSet(viewsets.ModelViewSet):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class qDetailsViewSet(viewsets.ModelViewSet):
    queryset = qDetails.objects.all()
    serializer_class = qDetailsSerializer


class UserApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            item = Users.objects.get(pk=pk)
            serializer = UserSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Users.objects.all()
        serializer = UserSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, pk=None):
        item = Users.objects.get(pk=pk)
        serializer = UserSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, pk=None):
        item = get_object_or_404(Users, pk=pk)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


#VISTAS BÁSICAS
@login_required
def index(request):
    return render(request, "./quote/index.html")

def login_plain(request):
    response = Response()
    logout(request)
    response.data = {
            'message':'Cierre de sesión exitoso'
        }
        #logout(request)
    return response
    #return render(request, "./quote/html/login.html")

@login_required
def home(request):
    return render(request, "./quote/html/sectionHome.html")

@login_required
def cotizar(request):
    #print (f"expira {datetime.datetime.fromtimestamp(int('1632366633')).strftime('%Y-%m-%d %H:%M:%S')} inicia {datetime.datetime.fromtimestamp(int('1632366433')).strftime('%Y-%m-%d %H:%M:%S')}")
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Autenticación fallida')
    
    #payload = jwt.decode(token, options={"verify_signature": False})
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        raise AuthenticationFailed('Autenticación fallida')
    
    print (f"expira {datetime.datetime.fromtimestamp(int(payload['exp'])).strftime('%Y-%m-%d %H:%M:%S')} inicia {datetime.datetime.fromtimestamp(int(payload['iat'])).strftime('%Y-%m-%d %H:%M:%S')}")
    
    #user = Users.objects.filter(id_user=payload['id']).first()
    #serializer = UserSerializer(user)

    return render(request, "./quote/html/sectionQuote.html")
""" 
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'quote/html/home.html'
    login_url = 'quo:login'
 """

#------------------------------LOGIN----------------------------------
# usuario de prueba {"username":"jaja", "password":"123123123"}
""" 
class SignInView(TemplateView):
    template_name='quote/html/login.html'
    def post(self, request):
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        user = Users.objects.filter(username=username).first()


        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Contraseña incorrecta')
        
        payload = {
            'id': user.id_user,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=3),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')#.decode('utf-8')
        print(token)
        
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'message':'Ingreso exitoso',
            'jwt': token
        }
        print(str(request.COOKIES.get('jwt')))
        login(request, user)
        #print(request)
        #return render(request, "./quote/html/sectionHome.html")
        #return redirect('quo:home')
        return response
        #return render_to_response('current_datetime.html', {'current_date': now})
 """
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


def userLogout(request):
    response = Response()
    response.delete_cookie('jwt')
    logout(request)
    response.data = {
        'message':'Cierre de sesión exitoso'
    }
    return redirect("quo:login")


class LoginView(TemplateView):
    template_name='quote/html/login.html'
    def post(self, request):
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")

        user = Users.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id_user,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')#.decode('utf-8')
        print("el token "+token)
        response = Response()

        response = redirect('quo:home')
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        print("la cookie "+str(request.COOKIES.get('jwt')))
        login(request, user)
        #return response
        
        return response
        #return redirect('quo:home')




""" class LogoutView(TemplateView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'Cierre de sesión exitoso'
        }
        logout(request)
        #logout(request)
        #return redirect('quo:login') """
""" 
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
        return JsonResponse(model_to_dict(oneProduct)) """

def Vista(request):
    return render(request, "./quote/html/sectionProducts.html")