#DJANGO
from decimal import Context
import json
from json.decoder import JSONDecoder
from re import template
from decouple import RepositoryEmpty
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.views import View
from django.forms import model_to_dict
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView
from .forms import CreateUserForm, UserForm


#RESTFRAMEWORK
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
#DECORATORS
from django.contrib.auth.decorators import login_required

#LOCAL FILES
from .models import ProductFiles, Role, Users, Product, Suppliers, Category, qDetails, Quotes
from .forms import ProductFilesForm
from .serializers import (
    UserSerializer, CategorySerializer, QuotesSerializer, qDetailsSerializer, 
    RoleSerializer, SupplierSerializer, ProductSerializer, ProductFileSerializer)
from .filters import ProductFilter
from apps.quote.upload import uploadDataDB
from apps.quote.reports import predefined
#PYTHON LIBRARIES
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

class productFilesViewSet(viewsets.ModelViewSet):
    queryset = ProductFiles.objects.all()
    serializer_class = ProductFileSerializer


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

def loading(request):
    return render(request, "./quote/html/LoadingSis.html")

#@login_required
def home(request):
    if checkToken(request):
        nProducts = str(Product.objects.all().count())
        nUsers = Users.objects.all().count()
        nSuppliers = Suppliers.objects.all().count()
        nCategories = Category.objects.all().count()
        nQuotes = Quotes.objects.all().count()
        data = {
            'nProducts' : nProducts,
            'nUsers' : nUsers,
            'nSuppliers': nSuppliers,
            'nCatego': nCategories,
            'nQuo': nQuotes
        }
        return render(request, "./quote/html/sections/sectionHome.html", context=data)
        
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
        print(f"aqui va 😂 {qs[1]}")
        product_searcher = request.GET.get('productname')
        product_price_since = request.GET.get('sincePrice')
        product_price_to = request.GET.get('toPrice')
        product_brand = request.GET.get('brandProduct')
        product_provider = request.GET.get('providerProduct')
        product_category = request.GET.get('categoryProduct')
        #falta el de categorias, tengo que poner en el desplegable las categorías que hay con un for

        if product_searcher != '' and product_searcher is not None:
            qs = qs.filter(product_name__icontains=product_searcher)

        if product_price_since != '' and product_price_since is not None and product_price_to != '' and product_price_to is not None:
            qs = qs.filter(price__gte=product_price_since, price__lte=product_price_to)
        elif (product_price_to == '' or product_price_to is None) and (product_price_since != '' and product_price_since is not None):
            qs = qs.filter(price__gte=product_price_since)
        elif (product_price_since == '' or product_price_since is None) and (product_price_to != '' and product_price_to is not None):
            qs = qs.filter(price__lte=product_price_to)

        if product_category != '' and product_category is not None:
            qsCategory = Category.objects.filter(id_category_product = product_category) #__icontains
            try:
                qs = qs.filter(id_category_product = qsCategory[0].id_category_product)
            except:
                pass

        if product_brand != '' and product_brand is not None:
            qsCategory = Product.objects.filter(brand = product_brand) #__icontains
            try:
                qs = qs.filter(brand = qsCategory[0].brand)
            except:
                pass
        
        if product_provider != '' and product_provider is not None:
            qsProducer = Product.objects.filter(id_supplier=product_provider) #__icontains
            try:
                qs = qs.filter(id_supplier=qsProducer[0].id_supplier)
            except:
                pass


        """ filter_products = ProductFilter(
            request.GET,
            queryset=Product.objects.all()
        ) """
        #mando los datos al frontend
        context['Categories'] = Category.objects.all()
        context['Product'] = Product.objects.all()
        context['Suppliers'] = Suppliers.objects.all()

        qs = qs.values('product_name','brand_vehicle', 'model_vehicle', 'year_vehicle').distinct()
        paginated_products = Paginator(qs, 5)
        page_number = request.GET.get('page')
        product_page_obj = paginated_products.get_page(page_number)
        
        context['product_page_obj']=product_page_obj

        
        # get the list of todos
        #response = requests.get('http://127.0.0.1:8000/api/product/')
        # transfor the response to json objects
        #todos = response.json()
        #print("respuesta " +str(todos))
        return render(request, "./quote/html/sections/sectionQuote.html", context=context)#{"todos": todos})

    return render(request, "./quote/html/login.html", {'showalert':True})
    #return redirect('quo:login')
    #return render(request, "./quote/html/sectionQuote.html")
    """ 
    class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'quote/html/home.html'
    login_url = 'quo:login'

    def SuppliersList(request):
    todo = Suppliers.objects.all()
    contexto = {'todos': todo}
    return render(request, "./quote/html/sections/sectionSuppliers.html", contexto)
    """
#bro ya aprendí :v    
def SuppliersList(request):
    # no need to do this
    # request_csrf_token = request.POST.get('csrfmiddlewaretoken', '')
    if request.method == 'GET' and request.is_ajax():
        request_getdata = request.GET.get('data',None)
        print(request_getdata)
        dataFromArray = json.loads(request_getdata)
        #print(f"A ver vea -> {dataFromArray} y el tipo {type(dataFromArray)}")
        #print(f"A ver vea 😍-> {selectedProducts} y el tipo {type(selectedProducts)}")
        i=0
        for x in dataFromArray:
            dataFromArray[i]=int(x)
            i+=1
        
        print(f"A ver vea -> {dataFromArray[0]} y el tipo {type(dataFromArray[0])}")

        #selectedProducts = Product.objects.filter(id_product__in=dataFromArray)
        selectedProducts = Product.objects.filter(id_product__in=dataFromArray)
        print(selectedProducts)
        response = Response()
        response = redirect('quo:home')
        #response.data = {'status':'Datos recibidos con éxito','selectedProducts': selectedProducts}
        #response = render(request, "./quote/html/sections/sectionSuppliers.html")
        return response
        """return JsonResponse({
            'content': {
                'status':'Datos recibidos con éxito',
                #'selectedProducts': selectedProducts
            }
        })"""
        # make sure that you serialise "request_getdata"
    if request.method == 'POST':
        formData = request.POST.dict()
        valueInput = formData.get("vS")
        #request_getdata = request.POST.get('data',None)
        dataFromArray = valueInput.split(',')
        #dataFromArray = json.loads(request_getdata)
        #print(f"A ver vea -> {dataFromArray} y el tipo {type(dataFromArray)}")
        #print(f"A ver vea 😍-> {selectedProducts} y el tipo {type(selectedProducts)}")
        i=0
        for x in dataFromArray:
            dataFromArray[i]=int(x)
            i+=1
        
        #print(f"A ver vea -> {dataFromArray[0]} y el tipo {type(dataFromArray[0])}")

        #selectedProducts = Product.objects.filter(id_product__in=dataFromArray)
        selectedProducts = Product.objects.filter(id_product__in=dataFromArray)
        print(selectedProducts)
        ctx = {'status':'Datos recibidos con éxito','selectedProducts': selectedProducts}
        return render(request, "./quote/html/sections/sectionSuppliers.html", ctx)

    return render(request, "./quote/html/sections/sectionSuppliers.html")

def CategoriesList(request):
    todo = Category.objects.all()
    contexto = {'todos': todo}
    return render(request, "./quote/html/sections/sectionCategories.html", contexto)


def ProductsList(request):
    todo = Product.objects.all()
    contexto = {'todos': todo}
    return render(request, "./quote/html/sectionProducts.html", contexto)


def userLogout(request):
    response = Response()
    response.delete_cookie('jwt')
    logout(request)
    response.data = {
        'message':'Cierre de sesión exitoso'
    }
    return redirect("quo:login")


#------------------------------LOGIN----------------------------------
# usuario de prueba {"username":"jaja", "password":"123123123"}
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
            return render(request, "./quote/html/login.html", {'notexistuser': True})
            #return render(request, "./quote/html/login.html", {'showalert':True})

        payload = {
            'id': user.id_user,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
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
"""
"""def tabla(request):
   # get the list of todos
   response = requests.get('http://127.0.0.1:8000/api/product/')
   # transfor the response to json objects
   todos = response.json()
   print("respuesta " +str(todos))
   return render(request, "./quote/html/sectionQuote.html", {"todos": todos})"""

def CreateProduct(request):
    return render(request, "./quote/html/ProductCreate.html")

#def UsersV(request):
    #todo = Users.objects.all()
    #contexto = {'todos': todo}
    #return render(request, "./quote/html/GeneralViewUser.html", contexto) 
    # 
#Listado de Productos--------------------------------
class ListadoProductos(TemplateView):
    #model= Product
    template_name='./quote/html/sectionQuoteElements.html'
    #context_object_name= 'productos'
    #queryset= Product.objects.all()
    def post(self, request):
        formData = request.POST.dict()
        valueInput = formData.get("vS")
        #request_getdata = request.POST.get('data',None)
        dataFromArray = valueInput.split(',')
        #dataFromArray = json.loads(request_getdata)
        #print(f"A ver vea -> {dataFromArray} y el tipo {type(dataFromArray)}")
        #print(f"A ver vea 😍-> {selectedProducts} y el tipo {type(selectedProducts)}")
        i=0
        print(dataFromArray)
        for x in dataFromArray:
            dataFromArray[i]=int(x)
            i+=1
        
        #print(f"A ver vea -> {dataFromArray[0]} y el tipo {type(dataFromArray[0])}")
        selectedProducts = Product.objects.filter(id_product__in=dataFromArray)
        #selectedProducts = Product.objects.filter(id_product__in=dataFromArray)
        #selectedProducts = Product.objects.filter(id_product__in=dataFromArray)
        print(selectedProducts)
        #ctx = {'status':'Datos recibidos con éxito','selectedProducts': selectedProducts}
        response = Response()
        response.data = {
            'status':True
        }
        ctx = {'selectedProducts': selectedProducts}
        response = render(request, "./quote/html/sectionQuoteElements.html", ctx)
        return response

# Listado de Usuarios-------------------------------- 
class ListadoUsuario(ListView):
    model= Users
    template_name= './quote/html/GeneralViewUser.html'
    context_object_name = 'usuarios'
    queryset= Users.objects.all()

class ActualizarUsuaio(UpdateView):
    model= Users
    form_class = UserForm
    template_name= './quote/html/editUser.html'
    context_object_name = 'usuario'
    success_url=reverse_lazy('quo:usersv')

class EliminarUsuario(DeleteView):
    model= Users
    template_name= './quote/html/deleteUser.html'
    success_url=reverse_lazy('quo:usersv')
#CreateView
class CrearUsuario(CreateView):
    model: Users
    form_class= CreateUserForm
    template_name= './quote/html/createUser.html'
    success_url=reverse_lazy('quo:usersv')

def crear_usuario(request):
    return render(request, "./quote/html/CreateUserView.html")

def ModalAddUser(request):
    return render(request, "./quote/html/AddUserModal.html")

def EliminarUser(request):
    return render(request, './quote/html/users_confirm_delete.html')

def CotizacionFinal(request):
    return render(request, './quote/html/sectionQuoteElements.html')


class uploadDocument(TemplateView, APIView):
    template_name='./quote/html/sections/sectionUploadDocument.html'
    
    def get(self, request):
        if checkToken(request):
            return render(request, "./quote/html/sections/sectionUploadDocument.html")
        logout(request)
        return render(request, "./quote/html/login.html", {'showalert':True})
        
    def post(self, request):
        name = request.POST.get('name_pfiles')
        file = request.FILES['productfile']
        #print(f"transformacion ---> {str(file)}")
        body ={
            'name_pfiles': name,
            'productfile': file
        }
        #print(body)
        response = Response()
        serializer = ProductFileSerializer(data=body)
        print(f"aqui mismo --> {serializer}")
        if serializer.is_valid():
            #response = redirect('quo:uploadDocument')
            response.data = {
                'success': True 
            }
            try:
                serializer.save()
                uploadDataDB.uploadDocumentXlsx(file)
                response = render(request, "./quote/html/sections/sectionUploadDocument.html", {'success': True})
                return response
            except:
                response = render(request, "./quote/html/sections/sectionUploadDocument.html", {'success': False})
                return response
        
            #print(Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK))
            #render(request, "./quote/html/uploadDocument.html")
        else:
            response = render(request, "./quote/html/sections/sectionUploadDocument.html", {'success': False})
            return response


class Reports(TemplateView):
    template_name = './quote/html/sections/sectionReports.html'
    response = Response()
    def get (self, request):
        if checkToken(request):

            if request.GET.get('download'):
                predefined.reportUser()

            quotes = Quotes.objects.all()
            data = {
                "quotesList" : quotes
            }
            return render(request, './quote/html/sections/sectionReports.html', data)
        logout(request)
        return render(request, "./quote/html/login.html", {'showalert':True})
    def post (self, request):
        if request.POST['download']=='dUR':
            allUsers = Users.objects.all()
            #print(f"tupla -> {a[0].first_name}")
            predefined.reportUser(allUsers)
            response = Response()
            response = redirect('http://127.0.0.1:8000/Documents/ReporteUsuarios.pdf')
            return response
            
        if request.POST['download']=='dPR':
            allProducts = Product.objects.all()
            #print(f"tupla -> {a[0].first_name}")
            predefined.reportProducts(allProducts)
            response = Response()
            response = redirect('http://127.0.0.1:8000/Documents/ReporteProductos.pdf')
            return response
        
        if request.POST['download']=='dPP':
            allSuppliers = Suppliers.objects.all()
            #print(f"tupla -> {a[0].first_name}")
            predefined.reportSuppliers(allSuppliers)
            response = Response()
            response = redirect('http://127.0.0.1:8000/Documents/ReporteProveedores.pdf')
            return response  


