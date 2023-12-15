from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('about/', views.About, name='about'),
    path('project/', views.Projects, name='project'),  # Corrected to 'Projects'
    path('contact/', views.Contact, name='contact'),
]
