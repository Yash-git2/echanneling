from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),

]


