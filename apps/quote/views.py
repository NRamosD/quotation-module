#DJANGO
from decimal import Context
import json
from json.decoder import JSONDecoder
from re import template
import re
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
from .forms import CreateUserForm, UserForm, ProductForm, SupplierForm, CategoryForm


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
from .models import uploadedFiles, Role, Users, Product, Suppliers, Category, qDetails, Quotes, ProductSupplierJoin
from .serializers import (
    UserSerializer, CategorySerializer, QuotesSerializer, qDetailsSerializer, 
    RoleSerializer, SupplierSerializer, ProductSerializer, uploadedFilesSerializer, ProductProviderSerializer)
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

class FilesViewSet(viewsets.ModelViewSet):
    queryset = uploadedFiles.objects.all()
    serializer_class = uploadedFilesSerializer

class prosupViewSet(viewsets.ModelViewSet):
    queryset = ProductSupplierJoin.objects.raw('Select 1 as id, A.ID_PRODUCT as id, A.ID_PRODUCT, A.PRODUCT_NAME, A.PRICE, A.BRAND, A.AVAILABILITY, A.BRAND_VEHICLE, A.MODEL_VEHICLE, A.YEAR_VEHICLE, A.PART_NUMBER, B.ID_SUPPLIER, B.SUPPLIER_NAME, B.CONCTACT_NAME, B.MOBILE_PHONE, B.ADDRESS, B.CITY, B.PROVINCE, B.COUNTRY from product as A inner join suppliers as B on A.ID_SUPPLIER=B.ID_SUPPLIER;')
    serializer_class = ProductProviderSerializer


class UserApiView(APIView):
    def post(self, request):
        print(f"aqui oe 😁 {type(request.data)}-> {request.data}")
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

def uploadT(request):
    return render(request, "./quote/html/sections/sectionUploadType.html")  

def pruebaHtml(request):
    return render(request, "./quote/html/error/sectionSuppliers.html")

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

class finalizarCotizacion(TemplateView):
    #model= Product
    template_name='./quote/html/sectionQuoteElements.html'

    def get(self, request):
        formData = request.POST.dict()
        valueInput = formData.get("vS")
        print(f"😘 {valueInput}")
        #request_getdata = request.POST.get('data',None)
        dataFromArray = valueInput.split(',')
        #dataFromArray = json.loads(request_getdata)
        #print(f"A ver vea -> {dataFromArray} y el tipo {type(dataFromArray)}")
        #print(f"A ver vea 😍-> {selectedProducts} y el tipo {type(selectedProducts)}")
        i=0
        print(dataFromArray)
        #dataFromArray.pop(0)
        for x in dataFromArray:
            dataFromArray[i]=int(x)
            i+=1
        
        #print(f"A ver vea -> {dataFromArray[0]} y el tipo {type(dataFromArray[0])}")
        selectedProducts = Product.objects.filter(id_product__in=dataFromArray)
        print(f"😍 ->{selectedProducts['price']}")
    #context_object_name= 'productos'
    #queryset= Product.objects.all()
    def post(self, request):
        formData = request.POST.dict()
        valueInput = formData.get("vS")
        print(f"😘 {valueInput}")
        #request_getdata = request.POST.get('data',None)
        dataFromArray = valueInput.split(',')
        #dataFromArray = json.loads(request_getdata)
        #print(f"A ver vea -> {dataFromArray} y el tipo {type(dataFromArray)}")
        #print(f"A ver vea 😍-> {selectedProducts} y el tipo {type(selectedProducts)}")
        i=0
        print(dataFromArray)
        #dataFromArray.pop(0)
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
        ctx = {'selectedProducts': selectedProducts, 'productsToSave':valueInput}
        response = render(request, "./quote/html/sectionQuoteElements.html", ctx)
        return response



def CotizacionFinal(request):
    return render(request, './quote/html/sectionQuoteElements.html')



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

#----------------------------LOGOUT------------------------------
def userLogout(request):
    response = Response()
    response.delete_cookie('jwt')
    logout(request)
    response.data = {
        'message':'Cierre de sesión exitoso'
    }
    return redirect("quo:login")


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

#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#
#-------------                CRUDS PRINCIPALES           ----------------#
#-------------------------------------------------------------------------#
#-------------------------------------------------------------------------#

#Productos--------------------------------
class ProductosView(TemplateView):
    def get(self, request):
        response = Response()
        products = Product.objects.all()
        supplier = Suppliers.objects.all()
        category = Category.objects.all()
        productsData = {
            "products" : products,
            "suppliers" : supplier,
            "categories" : category
        }
        response = render(request, './quote/html/sections/sectionProducts.html', productsData)
        return response
    
    def post(self, request):
        print(f"aqui va 😍-> {request.POST.dict()}")
        rawData = request.POST.dict()
        dataNewProduct = {
            "product_name": rawData['name'],
            "description": rawData['description'],
            "price": rawData['price'],
            "brand": rawData['brand'],
            "availability": rawData['availability'],
            "registration_date": '2021-10-30T11:05:09Z',
            "last_modified": '2021-10-30T11:05:09Z',
            "brand_vehicle": rawData['brand_vehicle'],
            "model_vehicle": rawData['model_vehicle'],
            "year_vehicle": rawData['year_vehicle'],
            "part_number": rawData['part_number'],
            "id_supplier": rawData['supplierProduct'],
            "id_category_product": rawData['categoryProduct']
        }
        serializer = ProductSerializer(data=dataNewProduct)
        
        response = Response()
        products = Product.objects.all()
        supplier = Suppliers.objects.all()
        category = Category.objects.all()
        productsData = {
            "products" : products,
            "suppliers" : supplier,
            "categories" : category,
            "success": True
        }
        if serializer.is_valid():
            print("👏")
            serializer.save()
            response = render(request, './quote/html/sections/sectionProducts.html', productsData)
            return response
        else:
            response = Response()
            productsData['success']=False
            response = render(request, './quote/html/sections/sectionProducts.html', productsData)
            return response

class ProductosViewUpdate(UpdateView):
    model= Product
    form_class = ProductForm
    template_name= './quote/html/editProduct.html'
    context_object_name = 'productos'
    success_url=reverse_lazy('quo:products')

class ProductosViewDelete(DeleteView):
    model= Product
    context_object_name = 'productos'
    template_name= './quote/html/deleteProduct.html'
    success_url=reverse_lazy('quo:products')


#Proveedores--------------------------------
class ProveedoresView(TemplateView):
    def get(self, request):
        response = Response()
        supplier = Suppliers.objects.all()
        suppliersData = {
            "suppliers" : supplier
        }
        response = render(request, './quote/html/sections/sectionSuppliers.html', suppliersData)
        return response
    
    def post(self, request):
        print(f"aqui va 😍-> {request.POST.dict()}")
        rawData = request.POST.dict()
        dataNewSupplier = {
            "supplier_name": rawData['name'],
            "description": rawData['description'],
            "conctact_name": rawData['contacName'],
            "landline": rawData['landline'],
            "mobile_phone": rawData['mobil'],
            "email": rawData['email'],
            "address": rawData['address'],
            "city": rawData['city'],
            "province": rawData['province'],
            "country": rawData['country']
        }
        serializer = SupplierSerializer(data=dataNewSupplier)
        
        response = Response()
        supplier = Suppliers.objects.all()
        supplierData = {
            "suppliers" : supplier,
            "success": True
        }
        if serializer.is_valid():
            print("👏")
            serializer.save()
            response = render(request, './quote/html/sections/sectionSuppliers.html', supplierData)
            return response
        else:
            response = Response()
            supplierData['success']=False
            response = render(request, './quote/html/sections/sectionSuppliers.html', supplierData)
            return response

class ProveedoresViewUpdate(UpdateView):
    model= Suppliers
    form_class = SupplierForm
    template_name= './quote/html/editSupplier.html'
    context_object_name = 'suppliers'
    success_url=reverse_lazy('quo:suppliers')

class ProveedoresViewDelete(DeleteView):
    model= Suppliers
    context_object_name = 'suppliers'
    template_name= './quote/html/deleteSupplier.html'
    success_url=reverse_lazy('quo:suppliers')


#Categorias--------------------------------
class CategoriasView(TemplateView):
    def get(self, request):
        response = Response()
        category = Category.objects.all()
        categoriesData = {
            "categories" : category
        }
        response = render(request, './quote/html/sections/sectionCategories.html', categoriesData)
        return response
    
    def post(self, request):
        print(f"aqui va 😍-> {request.POST.dict()}")
        rawData = request.POST.dict()
        dataNewCategory = {
             "category_vehicle": rawData['type_vehicle'],
            "category_name": rawData['name'],
            "description": rawData['description']
        }
        serializer = CategorySerializer(data=dataNewCategory)
        
        response = Response()
        category = Category.objects.all()
        categoryData = {
            "categories" : category,
            "success": True
        }
        if serializer.is_valid():
            print("👏")
            serializer.save()
            response = render(request, './quote/html/sections/sectionCategories.html', categoryData)
            return response
        else:
            response = Response()
            categoryData['success']=False
            response = render(request, './quote/html/sections/sectionCategories.html', categoryData)
            return response

class CategoriasViewUpdate(UpdateView):
    model= Category
    form_class = CategoryForm
    template_name= './quote/html/editCategory.html'
    context_object_name = 'categoria'
    success_url=reverse_lazy('quo:categories')

class CategoriasViewDelete(DeleteView):
    model= Category
    context_object_name = 'categoria'
    template_name= './quote/html/deleteCategory.html'
    success_url=reverse_lazy('quo:categories')




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


class uploadDocument(TemplateView, APIView):
    template_name='./quote/html/sections/sectionUploadDocument.html'
    
    def get(self, request):
        if checkToken(request):
            return render(request, "./quote/html/sections/sectionUploadDocument.html")
        logout(request)
        return render(request, "./quote/html/login.html", {'showalert':True})
        
    def post(self, request):
        typeDoc = request.POST.get('typeD')
        name = request.POST.get('name')
        description = request.POST.get('description')
        file = request.FILES['file']
        body ={
            'name_file': name,
            'description_file': description,
            'uploadedfile': file
        }
        response = Response()
        serializer = uploadedFilesSerializer(data=body)
        print(f"aqui mismo --> {serializer}")
        if serializer.is_valid():
            #response = redirect('quo:uploadDocument')
            response.data = {
                'success': True 
            }
            try:
                if typeDoc=='1':
                    serializer.save()
                    uploadDataDB.uploadXlsxCategories(file)
                    response = render(request, "./quote/html/sections/sectionUploadDocument.html", {'success': True})
                    return response
                elif typeDoc=='2':
                    serializer.save()
                    uploadDataDB.uploadXlsxSuppliers(file)
                    response = render(request, "./quote/html/sections/sectionUploadDocument.html", {'success': True})
                    return response
                elif typeDoc=='3':
                    serializer.save()
                    uploadDataDB.uploadXlsxProducts(file)
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


