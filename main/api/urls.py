from django.urls  import path
from main.api import views

urlpatterns = [
    path('api/', views.UserDataView.as_view(), name = 'UserDataView')
]