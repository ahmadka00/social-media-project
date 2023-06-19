from django.urls import path
from . import views

app_name = 'musker'

urlpatterns = [
    path('', views.index, name='index')
]