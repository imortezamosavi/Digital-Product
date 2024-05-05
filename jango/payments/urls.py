from django.urls import path

from .views import GatewayViews, PaymentViews

urlpatterns = [
    path('gateway/', GatewayViews.as_view()),
    path('pay/', PaymentViews.as_view()),
]