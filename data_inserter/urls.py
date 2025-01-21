from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL of 'data_inserter' to a view
]
