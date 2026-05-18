from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event/<int:id>/', views.event_detail, name='detail'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]