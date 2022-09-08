from rest_framework import viewsets
from .models import Offers,Slides
from .serializers import OfferSerializer,SlidesSerializer

# Create your views here.
class TicketsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing offers.
    """
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer

class SlidesViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing offers.
    """
    queryset = Slides.objects.all()
    serializer_class = SlidesSerializer

