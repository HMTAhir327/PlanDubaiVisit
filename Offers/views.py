from rest_framework import viewsets
from .models import Offers
from .serializers import OfferSerializer

# Create your views here.
class TicketsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing offers.
    """
    queryset = Offers.objects.all()
    serializer_class = OfferSerializer

# class OffersViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing offers.
#     """
#     queryset = Offers.objects.filter(isOffer=True)
#     serializer_class = OfferSerializer

