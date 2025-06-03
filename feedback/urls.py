from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mark-addressed/<int:feedback_id>/', views.mark_addressed, name='mark_addressed'),
    path('delete-feedback/<int:feedback_id>/', views.delete_feedback, name='delete_feedback'),
]
