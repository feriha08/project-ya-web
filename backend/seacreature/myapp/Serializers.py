from rest_framework import serializers
from .models import Payment
from .models import CreatureCard, Booking, CustomerProfile


class CreatureCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatureCard
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

