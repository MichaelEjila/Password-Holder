from django.test import TestCase
from django.urls import reverse, resolve
from main.views import index, create, view, apitoken

print("entered file 2")
class UrlTest(TestCase):

    def test_url_index_page(self):  
        url = reverse("index")
        self.assertEquals(resolve(url).func, index)

    def test_url_create_page(self):
        url = reverse("create")
        self.assertEquals(resolve(url).func, create)

    def test_url_view_page(self):
        url = reverse("view")
        self.assertEquals(resolve(url).func, view)

    def test_url_apitoken_page(self):
        url = reverse("apitoken")
        self.assertEquals(resolve(url).func, apitoken)