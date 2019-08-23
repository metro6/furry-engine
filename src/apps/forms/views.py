from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from .serializers import *
from .models import *

# Create your views here.

class FormCreateView(generics.CreateAPIView):
    serializer_class = FormDetailSerializer
    queryset = Form.objects.all()
    authentication_classes = (TokenAuthentication,)


class FormListView(generics.ListAPIView):
    serializer_class = FormListSerializer
    queryset = Form.objects.all()
    authentication_classes = (TokenAuthentication,)


class FormDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FormDetailSerializer
    queryset = Form.objects.all()
    authentication_classes = (TokenAuthentication,)
