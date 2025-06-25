from django.urls import path
from . import views

urlpatterns = [
    # CreatureCard endpoints
    path('creature/', views.manage_creature),
    path('creature/<int:pk>/', views.manage_creature),

    # Booking endpoints
    path('booking/', views.manage_booking),
    path('booking/<int:pk>/', views.manage_booking),

    # CustomerProfile endpoints
    path('customerprofile/', views.manage_customerprofile),
    path('customerprofile/<int:pk>/', views.manage_customerprofile),

    # Payment endpoints
    path('payment/', views.manage_payment),         
    path('payment/<int:pk>/', views.manage_payment),  
]
