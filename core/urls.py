#Add URL patterns for appointment booking and lab test booking


from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'), #Displays the homepage
    path('register/', views.register, name='register'), #Handles new user registration
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #Handles user login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), #Logs out the user
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('appointment/', views.view_appointments, name='view_appointments'),
    path('book/', views.book_appointment, name='book_appointment'), #Allows users to book doctor appointments
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'), #Allows users to cancel appointments
    path('emergency-numbers/', views.emergency_numbers, name='emergency_numbers'), #View emergency numbers
    path('lab__test/', views.lab__test, name='lab__test'),
    path('view-appointments/', views.view_appointments, name='view_appointments'),
    path('appointment/reschedule/<int:appointment_id>/', views.reschedule_appointment, name='reschedule_appointment'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),
]
