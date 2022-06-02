from django.urls import path
from .views import *


urlpatterns = [
    path('get_catalog/', (CatalogAPIView.as_view())),
]