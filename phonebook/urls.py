from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('detail_contact/<str:pk>', views.detail_contact, name='detail_contact'),
    path('delete_contact/<str:pk>', views.delete_contact, name='delete_contact'),
]
