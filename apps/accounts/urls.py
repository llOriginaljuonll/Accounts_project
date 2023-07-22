from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('',views.sign_in)
]
