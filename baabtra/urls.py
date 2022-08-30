from django.urls import path
from . import views

urlpatterns = [
    path('main',views.baabtra_main,name='main'),
]
