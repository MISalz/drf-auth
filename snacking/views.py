from rest_framework import generics
from .serializers import SnacksSerializer
from .models import Snacking
from .permissions import IsOwnerOrReadOnly

# Create your views here.
 

class SnackList(generics.ListCreateAPIView):
  queryset = Snacking.objects.all()
  serializer_class = SnacksSerializer  

class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Snacking.objects.all()
  serializer_class = SnacksSerializer  
  permission_classes = (IsOwnerOrReadOnly,)

