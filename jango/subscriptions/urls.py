from django.urls import path

from .views import SubscriptionViews, PackageViews

urlpatterns = [
    path('packages/', PackageViews.as_view()),
    path('subscriptions/', SubscriptionViews.as_view()),
]