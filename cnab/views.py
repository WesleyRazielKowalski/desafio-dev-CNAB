from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
#from models import  FilesCNAB


class ImportationView(viewsets.ModelViewSet):
    #queryset = FilesCNAB.objects.all()
    #serializer_class = NomeTabelaSerializer
    def save(self, request):
        pass