
from django.urls import path
from . import views
from .views import folio

app_name = 'folio'


urlpatterns = [
    path('', folio, name='index'),
    

   
]