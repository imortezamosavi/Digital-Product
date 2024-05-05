from django.urls import path

from .views import PaymentView, GatewayView

urlpatterns = [
    path('pay/', PaymentView.as_view()),
    path('gateway', GatewayView.as_view())
]