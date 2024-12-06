from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='service_list'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('requests/new/', views.create_request, name='create_request'),
    path('requests/my/', views.my_requests, name='my_requests'),
    path('login/', views.login_page_view, name='login_page_view'),
    path('register/', views.register_page_view, name='register_page_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
