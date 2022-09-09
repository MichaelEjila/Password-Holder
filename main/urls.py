from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name= 'index' ),
path('create/', views.create, name= 'create' ),
path('view/', views.view, name= 'view' ),
path('apitoken/', views.apitoken, name = 'apitoken'),
path('pdf/', views.pdf, name = 'pdf')
]

