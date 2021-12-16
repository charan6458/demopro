from django.urls import path
from youtube import views

urlpatterns = [
    path('home/',views.home),
    path('hello',views.hello),
]