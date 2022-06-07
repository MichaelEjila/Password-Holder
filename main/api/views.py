from rest_framework import status 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User, auth
from rest_framework.permissions import IsAuthenticated

from main.models import UserData, AccountDetails
from main.api.serializers import UserDataSerializer, AccountDetailSerializer

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def api_user_view(request,slug):
	try: 
		userdata = UserData.objects.get(slug=slug)
	except UserData.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
 
	if request.method == 'GET': 
		serializer = UserDataSerializer(userdata)
		return Response(serializer.data )


@api_view(['PUT',])
@permission_classes([IsAuthenticated])
def api_put_view(request,slug):
	try: 
		userdata = UserData.objects.get(slug=slug)
	except UserData.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT': 
		serializer = AccountDetailSerializer(userdata, data=request.data)
		data = {}

		if serializer.is_valid():
			serializer.save()
			data["success"] = 'Update Succesful'
			return Response(data=data)


		return Response("status = HTTP_400_BAD_REQUEST")



		return Response(serializers.errors, status = HTTP_400_BAD_REQUEST)

 
@api_view(['DELETE',])
@permission_classes([IsAuthenticated])
def api_delete_view(request,slug):
	try: 
		userdata = User.objects.get(username=slug)
	except UserData.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'DELETE': 
		operation = userdata.delete()
		data = {}
		if operation:
			data["success"] = 'Delete Succesful'
		else:
			data["failure"] = "Delete Failed "

		return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)



 
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def api_create_view(request):
	user_data = UserData()

	if request.method == 'POST':
		serializer = UserDataSerializer(user_data, data = request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(status = status.HTTP_404_NOT_FOUND)



















