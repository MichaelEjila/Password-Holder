from django.urls  import path
from main.api.views import (api_user_view, api_put_view, api_delete_view, api_create_view )

app_name = 'main '

urlpatterns = [
    path('<slug>/view/', api_user_view, name = 'View'),
    path('<slug>/update/', api_put_view, name = 'Update'),
    path('<slug>/delete/', api_delete_view, name = 'delete'),
    path('create/', api_create_view, name = 'create'),
] 