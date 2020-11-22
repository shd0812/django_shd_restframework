from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Interfaces
from .serializer import InterfaceSerializer
from utils.pagenations import MyPageNumberPagination
from rest_framework.response import Response
# Create your views here.


class InterfaceView(ModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = InterfaceSerializer
    pagination_class =  MyPageNumberPagination



