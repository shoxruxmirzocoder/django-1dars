from django.urls import path
from .views import index, kunlari
urlpatterns = [
path('', index, name="index"),
path('oylar/<int:pk>/   ', kunlari, name="man")


]