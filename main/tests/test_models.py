from django.test import TestCase
from main.models import UserData
from django.urls import reverse, resolve

# models test
print("entered file 1")
class UserDataTest(TestCase):

    def create_user_data(self, name="only a test"):
        return UserData.objects.create(name=name)

    def test_user_data_creation(self):
        w = self.create_user_data()
        self.assertTrue(isinstance(w, UserData))



