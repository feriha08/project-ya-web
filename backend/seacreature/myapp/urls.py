from django.urls import path
from . import views

urlpatterns = [
    # ✅ Login endpoint
    path('login/', views.login_view, name='login'),

    # ✅ CreatureCard endpoints
    path('creature/', views.manage_creature, name='creature-list'),
    path('creature/<int:pk>/', views.manage_creature, name='creature-detail'),

    # ✅ Booking endpoints
    path('booking/', views.manage_booking, name='booking-list'),
    path('booking/<int:pk>/', views.manage_booking, name='booking-detail'),

    # ✅ CustomerProfile endpoints
    path('customerprofile/', views.manage_customerprofile, name='customerprofile-list'),
    path('customerprofile/<int:pk>/', views.manage_customerprofile, name='customerprofile-detail'),

    # ✅ Payment endpoints
    path('payment/', views.manage_payment, name='payment-list'),
    path('payment/<int:pk>/', views.manage_payment, name='payment-detail'),
]
