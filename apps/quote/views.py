#DJANGO
from decimal import Context
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
from django.core.paginator import Paginator
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
from .filters import ProductFilter

import jwt, datetime
import requests

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


#@login_required
def home(request):
    if checkToken(request):
        return render(request, "./quote/html/sectionHome.html")
        
    logout(request)
    return render(request, "./quote/html/login.html", {'showalert':True})
    
    

    """ token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Autenticación fallida')
    
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        return redirect('quo:login')
        #response = Response() "./quote/html/login.html"
        #return render(request, 'quo:login' , context=context)
        #raise AuthenticationFailed('Autenticación fallida')
    
    return render(request, "./quote/html/sectionHome.html") """


#@login_required
def cotizar(request):
    """ token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Autenticación fallida')
    
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        return redirect('quo:login')
     """
    
    
        #raise AuthenticationFailed('Autenticación fallida')
    #print (f"expira {datetime.datetime.fromtimestamp(int(payload['exp'])).strftime('%Y-%m-%d %H:%M:%S')} inicia {datetime.datetime.fromtimestamp(int(payload['iat'])).strftime('%Y-%m-%d %H:%M:%S')}")
    #user = Users.objects.filter(id_user=payload['id']).first()
    #serializer = UserSerializer(user)
    if checkToken(request):
        context = {}
        
        qs = Product.objects.all()
        product_searcher = request.GET.get('productname')

        if product_searcher != '' and product_searcher is not None:
            qs = qs.filter(product_name__icontains=product_searcher)
        """ filter_products = ProductFilter(
            request.GET,
            queryset=Product.objects.all()
        ) """
        
        context['todos'] = qs

        paginated_products = Paginator(qs, 5)
        page_number = request.GET.get('page')
        product_page_obj = paginated_products.get_page(page_number)
        
        context['product_page_obj']=product_page_obj
        # get the list of todos
        #response = requests.get('http://127.0.0.1:8000/api/product/')
        # transfor the response to json objects
        #todos = response.json()
        #print("respuesta " +str(todos))
        return render(request, "./quote/html/sectionQuote.html", context=context)#{"todos": todos})

    return render(request, "./quote/html/login.html", {'showalert':True})
    #return redirect('quo:login')
    #return render(request, "./quote/html/sectionQuote.html")
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
    def get(self, request):
        return render(request, "./quote/html/login.html")
        

    def post(self, request):
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")

        user = Users.objects.filter(username=username).first()
        response = Response()

        if user is None or not user.check_password(password):
            print("entró")
            return render(request, "./quote/html/login.html", {'notexistuser': True})
            #return render(request, "./quote/html/login.html", {'showalert':True})

        """ if not user.check_password(password):
            response = redirect('quo:home')
            response.data = {
                'notexistuser': True 
            }
            return response """


        payload = {
            'id': user.id_user,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')#.decode('utf-8')
        print("el token "+token)

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

#Devuelve falso si el usuario no esta autenticado o tiene token caducado
def checkToken(request):
    token = request.COOKIES.get('jwt')

    if request.user.is_authenticated:
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            logout(request)
            return False

        return True
        
    return False


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
"""def tabla(request):
   # get the list of todos
   response = requests.get('http://127.0.0.1:8000/api/product/')
   # transfor the response to json objects
   todos = response.json()
   print("respuesta " +str(todos))
   return render(request, "./quote/html/sectionQuote.html", {"todos": todos})"""

def Vista(request):
    return render(request, "./quote/html/sectionCategories.html")

def UsersV(request):
    return render(request, "./quote/html/GeneralViewUser.html")

def ModalAddUser(request):
    return render(request, "./quote/html/AddUserModal.html")