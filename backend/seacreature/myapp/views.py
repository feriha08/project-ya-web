from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import *
from .Serializers import *


import logging
logger = logging.getLogger(__name__)


@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(username=username, email=email)
            if user.check_password(password):
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Generic handler for all models (GET, POST, PUT, DELETE)
def generic_api(model_class, serializer_class):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    def api_handler(request, pk=None):
        logger.debug(f"Request method: {request.method}, Data: {request.data}")

        if request.method == 'GET':
            if pk:
                try:
                    instance = model_class.objects.get(pk=pk)
                    serializer = serializer_class(instance)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except model_class.DoesNotExist:
                    return Response({'error': 'The object not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instances = model_class.objects.all()
                serializer = serializer_class(instances, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            if pk:
                try:
                    instance = model_class.objects.get(pk=pk)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except model_class.DoesNotExist:
                    return Response({'error': 'The object not found'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'error': 'ID is required to update data'}, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            if pk:
                try:
                    instance = model_class.objects.get(pk=pk)
                    instance.delete()
                    return Response({'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                except model_class.DoesNotExist:
                    return Response({'error': 'The object not found'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'error': 'ID is required to delete data'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    return api_handler


# ✅ Assign views for URL routing
manage_creature = generic_api(CreatureCard, CreatureCardSerializer)
manage_booking = generic_api(Booking, BookingSerializer)
manage_customerprofile = generic_api(CustomerProfile, CustomerProfileSerializer)
manage_payment = generic_api(Payment, PaymentSerializer)
