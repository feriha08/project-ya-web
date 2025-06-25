from rest_framework import serializers
from .models import CreatureCard, Booking, CustomerProfile, Payment

# ✅ Login serializer for authentication
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

# ✅ CreatureCard serializer
class CreatureCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatureCard
        fields = '__all__'

# ✅ Booking serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

# ✅ CustomerProfile serializer
class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'

# ✅ Payment serializer
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
