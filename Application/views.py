
from rest_framework import generics
from .models import Identity
from .serializers import IdentitySerializer
from django.shortcuts import render
# for Identity
class IdentityList(generics.ListCreateAPIView):
    queryset=Identity.objects.all()
    serializer_class=IdentitySerializer

class IdentityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Identity.objects.all()
    serializer_class=IdentitySerializer
   
   #class for displaying form

def displayForm(request):
    xyz=Identity.objects.all().values() #xyz is  QuerySet not object
    #print(xyz)
   
    #  return render(request,"App/index.html",xyz) will give following error context must be a dict rather than QuerySet.
    return render(request,"App/index.html",{"abc":xyz})
    