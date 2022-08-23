from django.urls import path
from data_table import views

urlpatterns = [
    path('', views.aboutme, name='aboutme'),
    # path('/', )
]