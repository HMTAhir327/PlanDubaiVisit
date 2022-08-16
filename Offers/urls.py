from django.urls import path, include, re_path
from .views import TicketsViewSet
from rest_framework import routers


router = routers.SimpleRouter()

# router.register(r'offers', OffersViewSet)
router.register(r'', TicketsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
