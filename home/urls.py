from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('pateint-entry', views.entry_form, name='entry'),
]
