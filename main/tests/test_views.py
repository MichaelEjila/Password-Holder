import imp
from django.test import TestCase, Client
from django.urls import reverse
from main.models import UserData, AccountDetails 
 

class TestViews(TestCase):
    
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('list'))
        self.assertEquals(response.status_code, 200)