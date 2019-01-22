from django.urls import path
from powerlifters import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]
