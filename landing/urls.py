from django.urls import path
from .views import HomeView,AboutView, DronesView, AddDroneView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('drones/', DronesView.as_view(), name='drones'),
    path('add_drones/', AddDroneView.as_view(), name='add_drones'),
]