from rest_framework.views import APIView 
from rest_framework.response import Response

from main.models import UserData, AccountDetails
from main.api.serializers import UserDataSerializer, AccountDetailSerializer

class UserDataView(APIView):
	def get(self, request):
		if serializer.is_valid:
			userserializer = UserDataSerializer()
			
			return Response(userserializer.data)
