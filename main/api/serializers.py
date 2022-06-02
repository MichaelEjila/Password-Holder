from rest_framework import serializers
from main.models import UserData, AccountDetails

class AccountDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = AccountDetails
		fields = ['user','username','website', 'logindetail', 'password',]

class UserDataSerializer(serializers.ModelSerializer):
	account_details = AccountDetailSerializer(many=True)

	class Meta:
		model = UserData
		fields = ['name','account_details']

	def create(self, validated_data):
		users_data = validated_data.pop('account_details')
		data = UserData.objects.create(**validated_data)
		for user_data in users_data:
			AccountDetails.objects.create(user = data, **user_data)
		return data

	def update(self, instance, validated_data):
		users_data = validated_data.pop('account_details')
		users = (instance.account_details).all()
		users = list(users)
		instance.name = validated_data.get('name', instance.name)
		instance.save()

		for user_data in users_data:
			detail = users.pop(0)
			detail.website = user_data.get('website', detail.website)
			detail.logindetail = user_data.get('logindetail', detail.logindetail)
			detail.password = user_data.get('password', detail.password)
			user.save()
		return instance

 