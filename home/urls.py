from django.contrib import admin
from django.urls import path
from .views import home

"""Visualizar imagens no browser"""
from django.conf import settings
from django.conf.urls.static import static

"""
Url´s onde devem ser definidas as url´s chamadas pelo browser indicando a
função à ser chamada.
"""

urlpatterns = [
    path('', home, name="home"),


]
