from django.urls import path

from .views import PaymentViews, GatewayViews

urlpatterns = [
    path('pay /', PaymentViews.as_view()),
    path('gateway', GatewayViews.as_view())
]