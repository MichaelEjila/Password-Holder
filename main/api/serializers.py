from rest_framework import serializers
from main.models import UserData, AccountDetails

class UserDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserData
		fields = ['name']

class AccountDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = AccountDetails
		fields = ['website', 'logindetail']
