
from django.urls import path
from . import views


app_name = 'main'


urlpatterns = [
path('', views.index, name='index'),
path('form', views.form, name='form'),
path('landing-page', views.landing, name='landing-page'),
path('thanks', views.thanksForm, name='thanks'),
]