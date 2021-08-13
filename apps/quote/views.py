from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer




# Create your views here.
def index(request):
    return render(request, "quote/index.html")




"""def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })"""


